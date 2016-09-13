from flask import Flask, jsonify, request, abort
from data_fetcher import DataFetcher
from models import DataFetchException, Study
from query_params import parse_fields_param, parse_filter_param
import study_collection_utils as sc_utils
import logging
import requests
import threading

app = Flask(__name__)
app.config.from_envvar("COPYRIGHT_EVIDENCE_API_CFG")

update_frequency = app.config["DATA_UPDATE_FREQUENCY_MINUTES"]


# Python doesn't have a 'one writer many readers' lock in the standard library.
# The app isn't heavily used at the moment so we will just lock on read
# for now and not bother trying to implement our own reader-writer lock
update_lock = threading.Lock()


def __updateData():
    data_url = app.config["DATA_URL"]
    data_fetcher = DataFetcher(data_url)

    try:
        update_lock.acquire()
        app.logger.info("Getting data from " + data_url)
        global studies_text
        studies_text = data_fetcher.get_studies_text()
        app.logger.info("Finished fetching data from " + data_url)
    except (DataFetchException, requests.exceptions.RequestException) as e:
        app.logger.info("Error fetching data from " + data_url +
                        "\nCannot update wiki data. Visualization data" +
                        "\nmay not be up to date or may be completely empty" +
                        "\nuntil the URL is successfully reachable."
                        "\nPlease ensure that the DATA_URL parameter is" +
                        " valid and restart the application." +
                        "\nMore detailed error:")

        app.logger.error(e)
    finally:
        update_lock.release()


@app.before_first_request
def setup_logging():
    if not app.debug:
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.INFO)


def get_studies_json():
    try:
        update_lock.acquire()
        global studies_text
        return [Study(text).enriched_json()
                for text in studies_text]
    finally:
        update_lock.release()


@app.route("/studies")
def studies():
    """Return a JSON list of all studies and their details."""
    app.logger.info("/studies")
    studies = get_studies_json()
    only_fields = parse_fields_param(request)
    filter_by = parse_filter_param(request)
    filtered_studies = sc_utils.filter_studies(studies, filter_by)
    sc_utils.deleted_unrequired_fields(filtered_studies, only_fields)
    return jsonify({"studies": filtered_studies})


@app.route("/properties")
def valid_study_properties():
    """
    Return all the valid properties that can be used in filters and 'field'
    query params in the REST API. Useful in combination with '/values' to allow
    the user to dynamically choose fields to generate a visualization from.
    """
    app.logger.info("/properties")
    return jsonify({"properties": Study.valid_fields(False)})


@app.route("/aggregatable_properties")
def aggregatable_study_properties():
    """
    Same behaviour as /properties, but excludes fields that it doesn't make
    sense to generate charts / aggregations from
    """
    app.logger.info("/aggregatable_properties")
    return jsonify({"properties": Study.valid_fields(True)})


@app.route("/values")
def valid_values():
    """
    Returns all the values for a given field - useful for populating dropdown
    menus or populating an axis on a chart for example.
    """
    app.logger.info("/values")
    studies = get_studies_json()
    field = request.args.get("field")
    values = sc_utils.get_valid_values(studies, field)
    return jsonify({"values": values})


@app.errorhandler(Exception)
def unhandled_exception(e):
    """Log unexcepted exceptions."""
    app.logger.info("Unhandled Exception: %s", (e))
    return abort(500)


def keep_data_updated():
    __updateData()
    threading.Timer(update_frequency * 60, keep_data_updated).start()

if __name__ == "__main__":
    keep_data_updated()
    app.run(host="0.0.0.0", port=app.config["PORT"])

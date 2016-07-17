from flask import Flask, jsonify, request
from database import WikiDatabase
from models import Study
from query_params import parse_fields_param, parse_filter_param

from study_collection_utils import filter_studies, deleted_unrequired_fields, \
    get_valid_values

app = Flask(__name__)
app.config.from_envvar("COPYRIGHT_EVIDENCE_API_CFG")

database = WikiDatabase(app.config["DATABASE"])


def get_studies_json():
    return [Study(text).enriched_json()
            for text in database.get_studies_text()]


@app.route("/studies")
def studies():
    studies = get_studies_json()

    only_fields = parse_fields_param(request)
    filter_by = parse_filter_param(request)

    filtered_studies = filter_studies(studies, filter_by)
    deleted_unrequired_fields(filtered_studies, only_fields)

    return jsonify({"studies": filtered_studies})


@app.route("/properties")
def valid_study_properties():
    """
    Return all the valid properties that can be used in filters and 'field'
    query params in the REST API. Useful in combination with '/values' to allow
    the user to dynamically choose fields to generate a visualization from.
    """
    return jsonify({"properties": Study.valid_fields(False)})


@app.route("/aggregatable_properties")
def aggregatable_study_properties():
    """
    Same behaviour as /properties, but excludes fields that it doesn't make
    sense to generate charts / aggregations from
    """
    return jsonify({"properties": Study.valid_fields(True)})


@app.route("/values")
def valid_values():
    """
    Returns all the values for a given field - useful for populating dropdown
    menus or populating an axis on a chart for example.
    """
    studies = get_studies_json()

    field = request.args.get("field")
    values = get_valid_values(studies, field)

    return jsonify({"values": values})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=app.config["PORT"])

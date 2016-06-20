from flask import Flask, jsonify, request
from database import WikiDatabase
from models import Study
from query_params import parse_fields_param, parse_filter_param
from study_collection_utils import filter_studies, deleted_unrequired_fields

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=app.config["PORT"])

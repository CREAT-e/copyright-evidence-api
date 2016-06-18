from flask import Flask, jsonify
from database import WikiDatabase
from study_parser import StudyParser

app = Flask(__name__)
app.config.from_envvar("COPYRIGHT_EVIDENCE_API_CFG")

database = WikiDatabase(app.config["DATABASE"])


def get_studies():
    studies = []
    parser = StudyParser()
    for text in database.get_studies_text():
        study = parser.parse_study(text)
        studies.append(study)
    return studies


@app.route("/studies")
def studies():
    studies = get_studies()
    return jsonify({"studies": studies})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=app.config["PORT"])

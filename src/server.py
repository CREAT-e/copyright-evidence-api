from flask import Flask, jsonify
from database import WikiDatabase
from models import Study

app = Flask(__name__)
app.config.from_envvar("COPYRIGHT_EVIDENCE_API_CFG")

database = WikiDatabase(app.config["DATABASE"])


def get_studies_json():
    return [Study(text).enriched_json()
            for text in database.get_studies_text()]


@app.route("/studies")
def studies():
    studies = get_studies_json()
    return jsonify({"studies": studies})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=app.config["PORT"])

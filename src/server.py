from pprint import PrettyPrinter
import json
from pprint import pprint
from flask import Flask, jsonify
from study_loader import StudyLoader

app = Flask(__name__)
app.config.from_envvar('CREATE_CFG')

all_studies = []

@app.route("/studies")
def studies():

    payload = {
        "results" : all_studies
    }

    return json.dumps(payload)

if __name__ == "__main__":
    loader = StudyLoader()

    all_studies = loader.get_all_studies()
    pp = PrettyPrinter()

    for study in all_studies:
        pp.pprint(study.get('authors'))

    app.run()

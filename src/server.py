from study_loader import StudyLoader
from flask import Flask
from pprint import pprint
app = Flask(__name__)

@app.route("/studies")
def studies():
    return "Hello World!"

if __name__ == "__main__":
    loader = StudyLoader()

    all_studies = loader.get_all_studies()

    for study in all_studies:
        pprint(study.authors)

    app.run()

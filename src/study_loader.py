import sqlite3
from study_parser import StudyParser

class StudyLoader(object):

    def __init__(self):
        self.db_path = "../data/database.sqlite"
        self.pages_query = """SELECT p.page_id, p.page_title, t.old_text
                         FROM page p, text t, revision r, categorylinks cl
                         WHERE cl.cl_to = "Studies" AND cl.cl_from = p.page_id AND p.page_latest = r.rev_id AND r.rev_text_id = t.old_id"""

    def get_all_studies(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        conn.row_factory = sqlite3.Row

        page_rows = conn.execute(self.pages_query)
        study_parser = StudyParser()

        results = []
        for row in page_rows:
            page_text = row[2]
            results.append(study_parser.parse_study(page_text))

        return results

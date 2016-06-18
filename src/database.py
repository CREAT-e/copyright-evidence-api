import sqlite3


class Database(object):

    def __init__(self, path):
        self.path = path

    def connect(self):
        return sqlite3.connect(self.path)

    def query(self, query, args=(), one=False):
        with self.connect() as conn:
            cursor = conn.execute(query, args)
            rs = cursor.fetchall()
            cursor.close()
            return (rs[0] if rs else None) if one else rs


class WikiDatabase(Database):

    def __init__(self, path):
        super(WikiDatabase, self).__init__(path)

    def get_studies_text(self):
        query = """
            SELECT t.old_text
            FROM categorylinks cl,
                 page p,
                 revision r,
                 text t
            WHERE cl.cl_to = 'Studies'
              AND cl.cl_from = p.page_id
              AND p.page_latest = r.rev_id
              AND r.rev_text_id = t.old_Id
        """
        rs = self.query(query)
        return [r[0] for r in rs]

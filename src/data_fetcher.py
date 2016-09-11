import requests
import sqlite3


class DataFetcher(object):

    def __init__(self, data_url):
        self.data_url = data_url

    def get_studies_text(self):
        r = requests.get(self.data_url)
        response_json = r.json()

        return [study["data"] for study in response_json]

import requests
from models import DataFetchException


class DataFetcher(object):

    def __init__(self, data_url):
        self.data_url = data_url

    def get_studies_text(self):
        r = requests.get(self.data_url)

        if r.status_code != 200:
            raise DataFetchException(r.status_code, r.text)
        else:
            response_json = r.json()
            return [study["data"] for study in response_json]

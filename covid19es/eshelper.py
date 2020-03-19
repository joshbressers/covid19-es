
import os
import json
import elasticsearch
import elasticsearch.helpers
from elasticsearch import Elasticsearch

class ES:
    def __init__(self, idx='covid-19'):
        if 'ESURL' not in os.environ:
            es_url = "http://localhost:9200"
        else:
            es_url = os.environ['ESURL']

        es = Elasticsearch([es_url])

        # Delete the index if it exists
        if es.indices.exists(idx) is True:
            es.indices.delete(index=idx, ignore=[400, 404])

        # We have to create it and add a mapping
        fh = open('mapping.json')
        mapping = json.load(fh)
        es.indices.create(idx, body=mapping)
        fh.close()

        self.es = es

    def add(self, data):
        for ok, item in elasticsearch.helpers.streaming_bulk(self.es, data, max_retries=2):
            if not ok:
                print("ERROR:")
                print(item)


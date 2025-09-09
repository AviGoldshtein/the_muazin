from elasticsearch import Elasticsearch
import services.speech_to_text.config as conf
# from services.speech_to_text.logic.logger import Logger


class ElasticConnector:
    def __init__(self):
        self.es = Elasticsearch(conf.ELASTIC_URI)
        # self.logger = Logger.get_logger(name=__name__)

    def update_meta_on_file(self, index_name, id, text):
        self.es.update(
            index=index_name,
            id=id,
            body={
                "doc": {
                    "Transcription": text
                }
            }
        )
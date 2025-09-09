from elasticsearch import Elasticsearch, NotFoundError
import services.speech_to_text.config as conf
from services.speech_to_text.logic.logger import Logger


class ElasticConnector:
    def __init__(self):
        self.es = Elasticsearch(conf.ELASTIC_URI)
        self.logger = Logger.get_logger(name=__name__)

    def update_meta_on_file(self, index_name, id, text):
        try:
            self.es.update(
                index=index_name,
                id=id,
                body={
                    "doc": {
                        "Transcription": text
                    }
                }
            )
            self.logger.info(f"updated with transcription successfully for file: {id}.")
        except NotFoundError as e:
            self.logger.error(f"{e}")
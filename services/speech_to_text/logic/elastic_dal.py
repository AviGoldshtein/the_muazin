from elasticsearch import Elasticsearch, NotFoundError
from services.shared.config import CONFIG
from services.shared.logger import Logger


class ElasticConnector:
    def __init__(self):
        self.es = Elasticsearch(CONFIG['elastic_search']['uri'])
        self.logger = Logger.get_logger(name=__name__)

    def update_meta_on_file(self, index_name: str, file_id: str, transcription: str)-> None:
        """
        update the metadata on a file with its transcription.
        :param transcription: the text from the file.
        :param index_name: the index where the meta on the file is stored.
        :param file_id: the unique id of the file.
        """
        try:
            self.es.update(
                index=index_name,
                id=file_id,
                body={
                    "doc": {
                        "Transcription": transcription
                    }
                }
            )
            self.logger.info(f"updated with transcription successfully for file: {file_id}.")
        except NotFoundError as e:
            self.logger.error(f"{e}")
from elasticsearch import Elasticsearch
import services.data_prossesor.config as conf
from services.data_prossesor.logic.logger import Logger


class ElasticConnector:
    def __init__(self):
        self.es = Elasticsearch(conf.ELASTIC_URI)
        self.logger = Logger.get_logger(name=__name__)

    def create_index_and_mapping_if_not_exist(self, index_name: str):
        """
        create an index with mapping if it doesn't exist.
        :param index_name: the name of the index.
        """
        mapping = {
            'properties': {
                'File_path': {'type': 'keyword'},
                'File_size': {'type': 'integer'},
                'File_name': {'type': 'text'},
                'Creation_time': {'type': 'date'},
                'text': {'type': 'text'}
            }
        }
        if not self.es.indices.exists(index=index_name):
            self.es.indices.create(index=index_name, mappings=mapping)
            self.logger.info(f"index {index_name} created.")

    def index_file(self, index_name, id, metadata):
        """
        index the metadata of a file.
        :param index_name: the index name to index to.
        :param id: the id for compatibility with mongo.
        :param metadata: what to index.
        """
        self.es.index(index=index_name, id=id, document=metadata)
        self.logger.info(f"file with id: {id} indexed.")
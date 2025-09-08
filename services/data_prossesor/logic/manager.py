from services.data_prossesor.logic.consumer import Consumer
from services.data_prossesor.logic.elastic_dal import ElasticConnector
from services.data_prossesor.logic.processor import Processor
from services.data_prossesor.logic.mongo_dal import MongoDal
import logging


class Manager:
    def __init__(self, consuming_topic, index_name):
        """
        manager initialization with instances of
        Processor, ElasticConnector, MongoDal and Logger.

        :param consuming_topic: the kafka consumption topic.
        :param index_name: the name to index in elastic.
        """
        self.consuming_topic = consuming_topic
        self.index_name = index_name
        self.processor = Processor()
        self.es_connector = ElasticConnector()
        self.mongo_dal = MongoDal()
        self.logger = logging.getLogger(__name__)


    def run(self):
        """
        start listening to the kafka topic,
        and insert every file to mongo,
        then index it to elastic search.
        """
        self.es_connector.create_index_and_mapping_if_not_exist(index_name=self.index_name)
        events = Consumer.get_consumer_events(self.consuming_topic)

        for event in events:
            metadata = event.value
            self.logger.info(f"metadata received: {metadata}")
            unique_id = self.processor.generate_id(metadata['File_name'] + metadata['Creation_time'])
            self.mongo_dal.insert_file(metadata=metadata, file_id=unique_id)
            self.es_connector.index_file(index_name=self.index_name, id=unique_id, metadata=metadata)
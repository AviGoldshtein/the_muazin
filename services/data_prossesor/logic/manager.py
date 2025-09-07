from services.data_prossesor.logic.consumer import Consumer
from services.data_prossesor.logic.elastic_dal import ElasticConnector
from services.data_prossesor.logic.processor import Processor
from services.data_prossesor.logic.mongo_dal import MongoDal
import services.data_prossesor.config as conf


class Manager:
    def __init__(self, consuming_topic):
        self.consuming_topic = consuming_topic
        self.index_name = conf.INDEX_NAME
        self.collection_name = conf.COLLECTION_NAME
        self.processor = Processor()
        # self.es_connector = ElasticConnector()
        # self.mongo_dal = MongoDal()

    def run(self):
        events = Consumer.get_consumer_events(self.consuming_topic)
        # self.es_connector.create_index(index_name=self.index_name, mappings={"####", "######"})

        for event in events:
            metadata = event.value
            print(metadata)
            unique_id = self.processor.generate_id(metadata['File_name'])
            # self.es_connector.insert_document(index_name=self.index_name, id=unique_id, doc=metadata)
            # self.mongo_dal.insert_file(collection_name=self.collection_name, file_path=metadata['File_path'])


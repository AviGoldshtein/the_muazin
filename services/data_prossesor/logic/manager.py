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
        self.es_connector = ElasticConnector()
        self.mongo_dal = MongoDal()

    def run(self):
        events = Consumer.get_consumer_events(self.consuming_topic)
        mapping = {
            'properties': {
                'File_path': {
                    'type': 'keyword'
                },
                'File_size': {
                    'type': 'integer'
                },
                'File_name': {
                    'type': 'text',
                    'fields': {
                        'keyword': {
                            'type': 'keyword',
                            'ignore_above': 256
                        }
                    }
                },
                'Creation_time': {
                    'type': 'date'
                }
            }
        }
        self.es_connector.create_index_if_not_exist(index_name=self.index_name, mappings=mapping)

        for event in events:
            metadata = event.value
            print(metadata)
            unique_id = self.processor.generate_id(metadata['File_name'])
            # self.es_connector.insert_document(index_name=self.index_name, id=unique_id, doc=metadata)
            self.mongo_dal.insert_file(metadata=metadata, file_id=unique_id)




# metadata = {'File_path': 'C:\\Users\\a0548\\Studies_\\part_two\\projects\\the_muazin\\services\\data_loader_src\\data\\podcasts\\download (33).wav',
#             'File_size': 3239610,
#             'File_name': 'download (33).wav',
#             'Creation_time': '1979-12-31 23:00:00'}
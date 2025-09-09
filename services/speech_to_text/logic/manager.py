from services.speech_to_text.logic.consumer import Consumer
from services.speech_to_text.logic.producer import Producer
from services.speech_to_text.logic.convertor import Convertor
from services.speech_to_text.logic.mongo_dal import MongoDal
from services.speech_to_text.logic.elastic_dal import ElasticConnector


class Manager:
    def __init__(self, consumption_topic, index_name):
        self.consumption_topic = consumption_topic
        self.index_name = index_name
        self.producer = Producer()
        self.convertor = Convertor()
        self.mongo_dal = MongoDal()
        self.es_connector = ElasticConnector()

    def run(self):
        events = Consumer.get_consumer_events(self.consumption_topic)

        for event in events:
            print("a new event had been received.")
            file_id = event.value['file_id']
            print(file_id)
            audio_file_bytes = self.mongo_dal.fetch_file(file_id=file_id)
            text = self.convertor.speech_to_text(audio_file_bytes)
            print(text)
            self.es_connector.update_meta_on_file(index_name=self.index_name, id=file_id, text=text)

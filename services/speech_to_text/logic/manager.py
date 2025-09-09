from services.speech_to_text.logic.consumer import Consumer
from services.speech_to_text.logic.producer import Producer
from services.speech_to_text.logic.convertor import Convertor


class Manager:
    def __init__(self, consumption_topic):
        self.consumption_topic = consumption_topic
        self.producer = Producer()
        self.convertor = Convertor()

    def run(self):
        events = Consumer.get_consumer_events(self.consumption_topic)

        for event in events:
            print("a new event had been received.")
            file_id = event.value['file_id']
            print(file_id)
            audio_file = self.mongo_dal.get_file(file_id=file_id)
            text = self.convertor.speech_to_text(audio_file)
            self.es_connector.update_meta_on_file(id=file_id, text=text)


            # metadata['text'] = self.convertor.speech_to_text(file_path=metadata['File_path'])
            # print(metadata['text'])
            # self.producer.publish_event(self.publishing_topic, metadata)

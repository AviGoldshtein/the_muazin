from services.speech_to_text.logic.consumer import Consumer
from services.speech_to_text.logic.producer import Producer
from services.speech_to_text.logic.convertor import Convertor


class Manager:
    def __init__(self, consumption_topic, publishing_topic):
        self.consumption_topic = consumption_topic
        self.publishing_topic = publishing_topic
        self.producer = Producer()
        self.convertor = Convertor()

    def run(self):
        events = Consumer.get_consumer_events(self.consumption_topic)

        for event in events:
            print("a new event had been received.")
            metadata = event.value
            metadata['text'] = self.convertor.speech_to_text(file_path=metadata['File_path'])
            print(metadata['text'])
            self.producer.publish_event(self.publishing_topic, metadata)

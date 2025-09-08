from services.speech_to_text.logic.consumer import Consumer


class Manager:
    def __init__(self, consumption_topic, publishing_topic):
        self.consumption_topic = consumption_topic
        self.publishing_topic = publishing_topic
        self.publisher = ""
        self.convertor = ""

    def run(self):
        events = Consumer.get_consumer_events(self.consumption_topic)

        for event in events:
            metadata = event.value
            metadata_with_text = self.convertor.speec_to_text(file_path=metadata['File_path'])
            self.publisher.publish_event(self.publishing_topic, metadata_with_text)

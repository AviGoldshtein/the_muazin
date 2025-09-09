from services.hostility_classifier.logic.consumer import Consumer


class Manager:
    def __init__(self, consuming_topic):
        self.consuming_topic = consuming_topic

    def run(self):
        events = Consumer.get_consumer_events(self.consuming_topic)

        for event in events:
            file_id = event.value['file_id']
            print(file_id)
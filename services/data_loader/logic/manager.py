from .data_loader import DataLoader


class Manager:
    def __init__(self, producing_topic):
        self.producing_topic = producing_topic
        self.data_loader = DataLoader()
        self.meta_extractor = ""
        self.producer = ""

    def run(self):
        files = self.data_loader.list_fils()
        print(files)
        for file in files:
            metadata_on_file = self.meta_extractor.extract_metadata(file)
            self.producer.publish_event(self.producing_topic, metadata_on_file)
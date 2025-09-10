from services.data_loader_src.logic.data_loader import DataLoader
from services.data_loader_src.logic.meta_extractor import MetaExtractor
from services.shared.producer import Producer
# from services.data_loader_src.logic.logger import Logger
from services.shared.logger import Logger


class Manager:
    def __init__(self, producing_topic):
        """
        manager initialization with instances of
        DataLoader, MetaExtractor and Producer.

        :param producing_topic: the kafka topic to produce.
        """
        self.producing_topic = producing_topic
        self.data_loader = DataLoader()
        self.meta_extractor = MetaExtractor()
        self.producer = Producer()
        self.logger = Logger.get_logger(name=__name__)

    def run(self):
        """
        fetch all the files, extract metadata
        for each file and upload them to kafka.
        """
        self.logger.info("starting the process...")
        files = self.data_loader.list_fils()
        for file in files:
            metadata_on_file = self.meta_extractor.extract_metadata(file)
            self.producer.publish_event(self.producing_topic, metadata_on_file)
from services.hostility_classifier.logic.consumer import Consumer
from services.hostility_classifier.logic.elastic_dal import ElasticConnector
from services.hostility_classifier.logic.classifier import Classifier
from services.shared.logger import Logger


class Manager:
    def __init__(self, consuming_topic, index_name):
        """
        manager initialization with instances of
        Classifier, ElasticConnector, and Logger.

        :param consuming_topic: the kafka consumption topic.
        :param index_name: the name to index in elastic.
        """
        self.consuming_topic = consuming_topic
        self.index_name = index_name
        self.es_connector = ElasticConnector()
        self.classifier = Classifier()
        self.logger = Logger.get_logger(name=__name__)

    def run(self):
        """
        start listening to the kafka topic,
        and calculate for every file the bds percentage,
        if it is bsd, and th threat level.
        """
        self.logger.info(f"starting listening to topic: {self.consuming_topic}")
        events = Consumer.get_consumer_events(self.consuming_topic)

        for event in events:
            file_id = event.value['file_id']
            self.logger.info(f"received a new file: {file_id}")

            text = self.es_connector.get_text_from(index_name=self.index_name, file_id=file_id)
            if text:
                bds_percent = self.classifier.calculate_bds_percent(text) # a number 0 / 100
                is_bds = self.classifier.decide_is_bds(bds_percent) # True / False
                bds_threat_level = self.classifier.classify_bds_threat_level(bds_percent) # "medium" / "high" / "none"

                new_fields = {
                    "bds_percent": bds_percent,
                    "is_bds": is_bds,
                    "bds_threat_level": bds_threat_level
                }
                print(f"new fields: {new_fields}")

                self.es_connector.update_meta_on_file(index_name=self.index_name, file_id=file_id, new_fields=new_fields)

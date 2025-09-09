from services.hostility_classifier.logic.consumer import Consumer
from services.hostility_classifier.logic.elastic_dal import ElasticConnector


class Manager:
    def __init__(self, consuming_topic, index_name):
        self.consuming_topic = consuming_topic
        self.index_name = index_name
        self.es_connector = ElasticConnector()

    def run(self):
        events = Consumer.get_consumer_events(self.consuming_topic)

        for event in events:
            file_id = event.value['file_id']
            print(file_id)

            text = self.es_connector.get_text_from(index_name=self.index_name, file_id=file_id)
            if text:

                bds_percent = 69
                is_bds = True
                bds_threat_level = "medium" or "high" or "none"

                new_fields = {
                    "bds_percent": bds_percent,
                    "is_bds": is_bds,
                    "bds_threat_level": bds_threat_level
                }

                self.es_connector.update_meta_on_file(index_name=self.index_name, file_id=file_id, new_fields=new_fields)

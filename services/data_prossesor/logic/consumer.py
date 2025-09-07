from kafka import KafkaConsumer
from services.data_prossesor.config import KAFKA_BOOTSTRAP
import json


class Consumer:
    @staticmethod
    def get_consumer_events(topic):
        """return an object with all the last events waiting in the kafka server for the specified topic"""
        bootstrap_server = KAFKA_BOOTSTRAP
        return KafkaConsumer(topic,
                                         group_id='data-processor',
                                         value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                         bootstrap_servers=[bootstrap_server]
                                      )
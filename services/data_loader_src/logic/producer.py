from kafka import KafkaProducer
from services.data_loader_src import config
import json


class Producer:
    def __init__(self):
        """initialize with a KafkaProducer object"""
        bootstrap_server = config.KAFKA_BOOTSTRAP
        self.__producer = KafkaProducer(bootstrap_servers=[bootstrap_server],
                                         value_serializer=lambda x:
                                         json.dumps(x).encode('utf-8')
                                        )

    def publish_event(self, topic, event) -> None:
        """
        publish an event to a specific topic on the linked kafka server
        :param event: the event to upload
        :param topic: the specified topic
        """
        self.__producer.send(topic, event)
        self.__producer.flush()
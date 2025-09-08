from kafka import KafkaConsumer
import services.data_prossesor.config as conf
import json


class Consumer:
    @staticmethod
    def get_consumer_events(topic):
        """return an object with all the last events waiting in the kafka server for the specified topic"""
        bootstrap_server = conf.KAFKA_BOOTSTRAP
        group_id = conf.CONSUMING_GROUP_ID_DATA_PROCESSOR
        return KafkaConsumer(topic,
                                         group_id=group_id,
                                         value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                         bootstrap_servers=[bootstrap_server]
                                      )
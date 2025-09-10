from kafka import KafkaConsumer
import services.speech_to_text.config as conf
import json


class Consumer:
    @staticmethod
    def get_consumer_events(topic):
        """return an object with all the last events waiting in the kafka server for the specified topic"""
        bootstrap_server = conf.KAFKA_BOOTSTRAP
        group_id = conf.CONSUMING_GROUP_ID_SPEECH_TO_TEXT
        return KafkaConsumer(topic,
             group_id=group_id,
             value_deserializer=lambda m: json.loads(m.decode('ascii')),
             bootstrap_servers=[bootstrap_server],
             max_poll_records=1
             # max_poll_interval_ms= 30 * 60 * 1000,
             # session_timeout_ms= 3 * 60 * 1000,
             # auto_offset_reset= "earliest"
          )
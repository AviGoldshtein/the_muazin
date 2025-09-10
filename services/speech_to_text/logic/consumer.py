from kafka import KafkaConsumer
from services.shared.config import CONFIG
import json


class Consumer:
    @staticmethod
    def get_consumer_events(topic):
        """return an object with all the last events waiting in the kafka server for the specified topic"""
        bootstrap_server = CONFIG['kafka']['kafka_boostrap']
        group_id = CONFIG['speech_to_text']['group_id']
        return KafkaConsumer(topic,
             group_id=group_id,
             value_deserializer=lambda m: json.loads(m.decode('ascii')),
             bootstrap_servers=[bootstrap_server],
             max_poll_records=1
             # max_poll_interval_ms= 30 * 60 * 1000,
             # session_timeout_ms= 3 * 60 * 1000,
             # auto_offset_reset= "earliest"
          )
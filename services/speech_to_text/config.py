import os


#kafka
CONSUME_TOPIC = "loaded_with_meta"
PUBLISH_TOPIC = "loaded_with_text"
CONSUMING_GROUP_ID_SPEECH_TO_TEXT = "STT"
KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092")
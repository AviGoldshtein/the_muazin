import os


CONSUMING_TOPIC = "hostility_classification"
CONSUMING_GROUP_ID_HOSTILITY_CLASSIFIER = "hostility-classifier"
KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092")

import os


#kafka
CONSUMING_TOPIC = "hostility_classification"
CONSUMING_GROUP_ID_HOSTILITY_CLASSIFIER = "hostility-classifier"
KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092")

# elasticsearch
INDEX_NAME = "muazin"
INDEX_LOGS = "muazin-logs"
ELASTIC_URI = os.getenv("ELASTIC_URI", "http://localhost:9200")
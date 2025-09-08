import os

#kafka
CONSUMING_TOPIC_DATA_PROCESSOR = "loaded_with_meta"
CONSUMING_GROUP_ID_DATA_PROCESSOR = "data-processor"
KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092")

# elasticsearch
INDEX_NAME = "muazin"
INDEX_LOGS = "muazin-logs"
ELASTIC_URI = os.getenv("ELASTIC_URI", "http://localhost:9200")

# mongo
MONGO_DB = os.getenv("MONGO_DB", "mydb")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

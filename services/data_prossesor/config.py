import os


CONSUMING_TOPIC_DATA_PROCESSOR = "loaded_with_meta"
KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092")
INDEX_NAME = "muazin"
COLLECTION_NAME = "muazin_coll"
MONGO_DB = os.getenv("MONGO_DB", "mydb")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
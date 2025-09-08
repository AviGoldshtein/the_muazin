import os
import pathlib

#kafka
PRODUCING_TOPIC_DATA_LOADER = "loaded_with_meta"
KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092")

#files location
root_path = pathlib.Path(__file__).resolve().parent
FILES_PATH = root_path / "data" / "podcasts"

#elastic search
INDEX_LOGS = "muazin-logs"
ELASTIC_URI = os.getenv("ELASTIC_URI", "http://localhost:9200")
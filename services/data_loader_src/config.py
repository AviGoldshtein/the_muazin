import os
import pathlib


PRODUCING_TOPIC_DATA_LOADER = "loaded_with_meta"
KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092")

root_path = pathlib.Path(__file__).resolve().parent
FILES_PATH = root_path / "data" / "podcasts"
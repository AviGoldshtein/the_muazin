import os
import pathlib


CONFIG = {
    "mongo": {
        "uri": os.getenv("MONGO_URI", "mongodb://localhost:27017"),
        "db": os.getenv("MONGO_DB", "mydb")
    },
    "kafka": {
        "kafka_boostrap": os.getenv("KAFKA_BOOTSTRAP", "localhost:9092")
    },
    "elastic_search": {
        "index": "muazin",
        "index_logs": "muazin-logs",
        "uri": os.getenv("ELASTIC_URI", "http://localhost:9200")
    },
    "data_loader_src": {
        "producing_topic": "loaded_with_meta",
        "files_path": pathlib.Path(__file__).resolve().parent.parent / "data_loader_src" / "data" / "podcasts"
    },
    "data_prossesor": {
        "consuming_topic": "loaded_with_meta",
        "producing_topic": "for_transcription",
        "group_id": "data-processor"
    },
    "speech_to_text": {
        "consuming_topic": "for_transcription",
        "producing_topic": "hostility_classification",
        "group_id": "STT"
    },
    "hostility_classifier": {
        "consuming_topic": "hostility_classification",
        "group_id": "hostility-classifier"
    }
}


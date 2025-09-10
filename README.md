# The muazin

Welcome to the **Muazin** project — a modular system for uploading audio files, extracting their metadata, uploading them to a mongo db storage, converting the audio to text, classify the hostility level of the content, and index the metadata and the text to Elastic search for smart searching.

---

## Services

---

### Data loader

- Load a directory of WAV files.
- Extract the metadata.
- Send them to Kafka for the next service.

---

### Data processor

- Generate a unique id for each file.
- Insert the file in mongo with gridFS.
- Index the metadata to Elasticsearch.
- Send them to Kafka for the next service.

---

### Speech to text

- Fetch the file out of mongo with gridFS.
- Transcribe it into text.
- Update in Elasticsearch with new transcription.
- Send to Kafka for the next service.

---

### Hostility classifier

- Calculate the hostility level of the transcription.
- Classify if the file is hostile.
- Classify the threat level of the file.
- Update the Elasticsearch with the new details.

---

## Tach-Stack

- Kafka
- Elasticsearch
- Mongo (gridFS)
- faster_whisper (STT)

---

## Getting Started

clone the repository:
```bash
git clone https://github.com/AviGoldshtein/the_muazin.git
```

go to the root in the project:
```bash
cd the_muazin
```

build the images:
```bash
docker build -t data_loader_src -f services/data_loader_src/Dockerfile .
docker build -t data_prossesor -f services/data_prossesor/Dockerfile .
docker build -t speech_to_text -f services/speech_to_text/Dockerfile .
docker build -t hostility_classifier -f services/hostility_classifier/Dockerfile .
```


run:
```bash
docker compose up -d
```

run the rest of the containers not in the docker-compose:
```bash
docker run --name data_loader_src --network muazin-net -d -e "KAFKA_BOOTSTRAP=muazin-kafka:9092" data_loader_src:latest
docker run --name data_prossesor --network muazin-net -d -e "KAFKA_BOOTSTRAP=muazin-kafka:9092" -e "ELASTIC_URI=http://muazin-es:9200" -e "MONGO_URI=mongodb://muazin-mongo:27017" -e "MONGO_DB=mydb" data_prossesor:latest
docker run --name speech_to_text --network muazin-net -d -e "KAFKA_BOOTSTRAP=muazin-kafka:9092" -e "ELASTIC_URI=http://muazin-es:9200" -e "MONGO_URI=mongodb://muazin-mongo:27017" -e "MONGO_DB=mydb" speech_to_text:latest
docker run --name hostility_classifier --network muazin-net -d -e "KAFKA_BOOTSTRAP=muazin-kafka:9092" -e "ELASTIC_URI=http://muazin-es:9200" hostility_classifier:latest
```
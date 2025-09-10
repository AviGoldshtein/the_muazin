docker build -t data_loader_src -f services/data_loader_src/Dockerfile .
docker run --name data_loader_src --network muazin-net -d -e "KAFKA_BOOTSTRAP=muazin-kafka:9092" data_loader_src:latest


docker build -t data_prossesor -f services/data_prossesor/Dockerfile .
docker run --name data_prossesor --network muazin-net -d -e "KAFKA_BOOTSTRAP=muazin-kafka:9092" -e "ELASTIC_URI=http://muazin-es:9200" -e "MONGO_URI=mongodb://muazin-mongo:27017" -e "MONGO_DB=mydb" data_prossesor:latest



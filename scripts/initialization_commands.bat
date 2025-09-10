@REM network creation
docker network create muazin-net

@REM run kafka
docker run -d --name muazin-kafka --hostname kafka --network muazin-net -e KAFKA_CFG_NODE_ID=1 -e KAFKA_CFG_PROCESS_ROLES=broker,controller -e KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=1@kafka:9093 -e KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 -e KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092 -e KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER -e KAFKA_CFG_AUTO_CREATE_TOPICS_ENABLE=true -p 9092:9092 bitnami/kafka:3.7
docker run -d --name muazin-kafka --network muazin-net -e KAFKA_CFG_NODE_ID=1 -e KAFKA_CFG_PROCESS_ROLES=broker,controller -e KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=1@kafka:9093 -e KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 -e KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092 -e KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER -e KAFKA_CFG_AUTO_CREATE_TOPICS_ENABLE=true -p 9092:9092 bitnami/kafka:3.7
@REM local run kafka
docker run -d --name muazin-kafka --network muazin-net -p 9092:9092 apache/kafka:latest


@REM run mongo
docker run -d --name muazin-mongo -p 27017:27017 mongo:latest

@REM run elastic search
docker run -d --name muazin-es --network muazin-net -p 9200:9200 -e "discovery.type=single-node" -e "xpack.security.enabled=false" -e "ES_JAVA_OPTS=-Xms1g -Xmx1g" docker.elastic.co/elasticsearch/elasticsearch:8.15.0

@REM run kibana
docker run --name muazin-kibana --network muazin-net -e "ELASTICSEARCH_HOSTS=http://muazin-es:9200" -p 5601:5601 docker.elastic.co/kibana/kibana:8.15.0


from services.data_prossesor.logic.manager import Manager
import services.data_prossesor.config as conf
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)


def main():
    manager = Manager(consuming_topic=conf.CONSUMING_TOPIC_DATA_PROCESSOR,
                      index_name=conf.INDEX_NAME,
                      collection_name=conf.COLLECTION_NAME)
    manager.run()


if __name__ == "__main__":
    main()
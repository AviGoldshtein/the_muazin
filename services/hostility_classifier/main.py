from services.hostility_classifier.logic.manager import Manager
import services.hostility_classifier.config as conf
from services.hostility_classifier.logic.logger import Logger


def main():
    logger = Logger.get_logger("hostility_classifier")
    logger.info("hostility_classifier started...")
    manager = Manager(consuming_topic=conf.CONSUMING_TOPIC,
                      index_name=conf.INDEX_NAME)
    manager.run()


if __name__ == "__main__":
    main()
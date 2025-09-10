from services.hostility_classifier.logic.manager import Manager
from services.shared.config import CONFIG
from services.shared.logger import Logger


def main():
    logger = Logger.get_logger("hostility_classifier")
    logger.info("hostility_classifier started...")
    manager = Manager(
        consuming_topic=CONFIG['hostility_classifier']['consuming_topic'],
        index_name=CONFIG['elastic_search']['index']
    )
    manager.run()


if __name__ == "__main__":
    main()
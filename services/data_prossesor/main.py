from services.data_prossesor.logic.manager import Manager
from services.shared.logger import Logger
import services.data_prossesor.config as conf


def main():
    """initialize the manager and run server"""
    logger = Logger.get_logger(name="processor")
    logger.info("data processor started...")
    manager = Manager(consuming_topic=conf.CONSUMING_TOPIC_DATA_PROCESSOR,
                      producing_topic=conf.PRODUCING_TOPIC_DATA_PROCESSOR,
                      index_name=conf.INDEX_NAME)
    manager.run()


if __name__ == "__main__":
    main()
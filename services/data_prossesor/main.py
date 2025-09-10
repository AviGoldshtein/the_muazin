from services.data_prossesor.logic.manager import Manager
from services.shared.logger import Logger
from services.shared.config import CONFIG


def main():
    """initialize the manager and run server"""
    logger = Logger.get_logger(name="processor")
    logger.info("data processor started...")
    manager = Manager(consuming_topic=CONFIG['data_prossesor']['consuming_topic'],
                      producing_topic=CONFIG['data_prossesor']['producing_topic'],
                      index_name=CONFIG['elastic_search']['index'])
    manager.run()


if __name__ == "__main__":
    main()
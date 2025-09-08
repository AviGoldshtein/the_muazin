from logic.manager import Manager
from services.data_loader_src.logic.logger import Logger
import config


def main():
    """initialize the manager and run server"""
    logger = Logger.get_logger(name="data_loader")
    logger.info("data loader started...")
    manager = Manager(config.PRODUCING_TOPIC_DATA_LOADER)
    manager.run()


if __name__ == "__main__":
    main()
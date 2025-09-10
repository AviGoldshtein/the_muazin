from logic.manager import Manager
from services.shared.logger import Logger
from services.shared.config import CONFIG


def main():
    """initialize the manager and run server"""
    logger = Logger.get_logger(name="data_loader")
    logger.info("data loader started...")
    manager = Manager(producing_topic=CONFIG['data_loader_src']['producing_topic'])
    manager.run()


if __name__ == "__main__":
    main()
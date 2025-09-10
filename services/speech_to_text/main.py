from services.speech_to_text.logic.manager import Manager
from services.shared.config import CONFIG
from services.shared.logger import Logger


def main():
    """initialize the manager and run server"""
    logger = Logger.get_logger(name="speech_to_text")
    logger.info("speech to text started...")
    manager = Manager(
        consumption_topic=CONFIG['speech_to_text']['consuming_topic'],
        publication_topic=CONFIG['speech_to_text']['producing_topic'],
        index_name=CONFIG['elastic_search']['index']
    )
    manager.run()

if __name__ == "__main__":
    main()
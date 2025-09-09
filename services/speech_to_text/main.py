from services.speech_to_text.logic.manager import Manager
import services.speech_to_text.config as conf
from services.speech_to_text.logic.logger import Logger


def main():
    logger = Logger.get_logger(name="speech_to_text")
    logger.info("speech to text started...")
    manager = Manager(
        consumption_topic=conf.CONSUME_TOPIC,
        index_name=conf.INDEX_NAME
    )
    manager.run()

if __name__ == "__main__":
    main()
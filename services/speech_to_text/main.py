from services.speech_to_text.logic.manager import Manager
import services.speech_to_text.config as conf


def main():
    manager = Manager(
        consumption_topic=conf.CONSUME_TOPIC,
        index_name=conf.INDEX_NAME
    )
    manager.run()

if __name__ == "__main__":
    main()
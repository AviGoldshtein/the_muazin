from services.speech_to_text.logic.manager import Manager
import services.speech_to_text.config as conf

#Transcription

def main():
    manager = Manager(
        consumption_topic=conf.CONSUME_TOPIC
    )
    manager.run()

if __name__ == "__main__":
    main()
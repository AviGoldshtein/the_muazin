from logic.manager import Manager
import config


def main():
    manager = Manager(config.PRODUCING_TOPIC_DATA_LOADER)
    manager.run()


if __name__ == "__main__":
    main()
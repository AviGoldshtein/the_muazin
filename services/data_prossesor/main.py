from services.data_prossesor.logic.manager import Manager
from services.data_prossesor.config import CONSUMING_TOPIC_DATA_PROCESSOR


def main():
    manager = Manager(CONSUMING_TOPIC_DATA_PROCESSOR)
    manager.run()


if __name__ == "__main__":
    main()
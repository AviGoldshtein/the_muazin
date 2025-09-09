from services.speech_to_text.logic.consumer import Consumer
from services.speech_to_text.logic.convertor import Convertor
from services.speech_to_text.logic.mongo_dal import MongoDal
from services.speech_to_text.logic.elastic_dal import ElasticConnector
from services.speech_to_text.logic.logger import Logger


class Manager:
    def __init__(self, consumption_topic, index_name):
        """
        manager initialization with instances of
        Convertor, MongoDal, ElasticConnector and Logger.

        :param consumption_topic: the kafka consumption topic.
        :param index_name: the name to index in elastic.
        """
        self.consumption_topic = consumption_topic
        self.index_name = index_name
        self.convertor = Convertor()
        self.mongo_dal = MongoDal()
        self.es_connector = ElasticConnector()
        self.logger = Logger.get_logger(name=__name__)

    def run(self):
        """
        start listening to the kafka topic,
        and fetch every file from mongo,
        then transcribe it to text,
        then update the metadata on the file in elastic search.
        """
        self.logger.info("starting listening...")
        events = Consumer.get_consumer_events(self.consumption_topic)

        for event in events:
            file_id = event.value['file_id']
            self.logger.info(f"received a new file: {file_id}")
            audio_file_bytes = self.mongo_dal.fetch_file(file_id=file_id)
            transcription = self.convertor.speech_to_text(audio_file_bytes)
            self.es_connector.update_meta_on_file(index_name=self.index_name, file_id=file_id, transcription=transcription)

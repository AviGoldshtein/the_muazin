from pymongo import MongoClient
import services.speech_to_text.config as conf
from services.shared.logger import Logger
from gridfs import GridFS


class MongoDal:
    def __init__(self):
        """
        initialize with the database name from env variable
        and the name of the collection to work with
        """
        self.db = None
        self.database = conf.MONGO_DB
        self.uri = conf.MONGO_URI
        self.logger = Logger.get_logger(name=__name__)

    def fetch_file(self, file_id: str) -> bytes | None:
        """
        fetch a file from grid-fs by its id.
        :param file_id: the id of the file.
        :return: the bytes of the file.
        """
        try:
            with MongoClient(self.uri) as client:
                self.db = client[self.database]
                fs = GridFS(self.db)
                grid_out = fs.get(file_id=file_id)
                self.logger.info(f"successfully fetched file from db, file: {file_id}.")
                return grid_out.read()
        except Exception as e:
            self.logger.error(f"error fetching file: {file_id},\n{e}.")
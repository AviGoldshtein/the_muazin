from pymongo import MongoClient
import services.speech_to_text.config as conf
from services.data_prossesor.logic.logger import Logger
import pathlib
from gridfs import GridFSBucket, GridFS
from gridfs.errors import FileExists


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

    def fetch_file(self, file_id):
        try:
            with MongoClient(self.uri) as client:
                self.db = client[self.database]
                fs = GridFS(self.db)
                grid_out = fs.get(file_id=file_id)
                return grid_out.read()
        except Exception as e:
            print(f"error: {e}")
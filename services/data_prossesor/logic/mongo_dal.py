from pymongo import MongoClient
import services.data_prossesor.config as conf
import pathlib
from gridfs import GridFSBucket
from gridfs.errors import FileExists
import logging


class MongoDal:
    def __init__(self):
        """
        initialize with the database name from env variable
        and the name of the collection to work with
        """
        self.db = None
        self.database = conf.MONGO_DB
        self.uri = conf.MONGO_URI
        self.logger = logging.getLogger(__name__)

    def insert_file(self, metadata, file_id):
        """
        insert a file into mongo,
        use the file_id to determine the _id in the mongo collection.

        :param metadata: the details of the file to attach.
        :param file_id: a unique str id
        """
        audio_file_path = pathlib.Path(metadata['File_path'])
        try:
            with MongoClient(self.uri) as client:
                self.db = client[self.database]
                fs = GridFSBucket(self.db)

                with open(audio_file_path, 'rb') as audio_file:
                    fs.upload_from_stream_with_id(
                        file_id=file_id,
                        filename=audio_file_path.name,
                        source=audio_file,
                        metadata=metadata
                    )
                self.logger.info(f"inserted file: '{metadata['File_name']}'")
        except FileExists as e:
            self.logger.error(f"{e}, filename: '{metadata['File_name']}'")

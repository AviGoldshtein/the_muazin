from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.errors import DuplicateKeyError
import services.data_prossesor.config as conf
import pathlib
from gridfs import GridFSBucket
import os
from pydub import AudioSegment
from io import BytesIO


class MongoDal:
    def __init__(self):
        """
        initialize with the database name from env variable
        and the name of the collection to work with
        """
        self.db = None
        self.database = conf.MONGO_DB
        self.uri = conf.MONGO_URI

    def insert_file(self, metadata, file_id):
        audio_file_path = pathlib.Path(metadata['File_path'])

        with MongoClient(self.uri) as client:
            self.db = client[self.database]
            # Initialize GridFSBucket
            fs = GridFSBucket(self.db)
            with open(audio_file_path, 'rb') as audio_file:
                fs.upload_from_stream_with_id(
                    file_id=file_id,
                    filename=audio_file_path.name,
                    source=audio_file,
                    metadata=metadata
                )



    # def read_file(self, file_id, pydub=None):
    #     with MongoClient(self.uri) as client:
    #         self.db = client[self.database]
    #         fs = GridFSBucket(self.db)
    #         fs.download_to_stream(
    #             file_id=file_id,
    #             destination="temp.wav"
    #         )
    #         file_id = ObjectId(file_id)  # Replace with the actual _id of your audio file
    #         grid_out = fs.open_download_stream(file_id)
    #         audio_data = grid_out.read()
    #         with open('downloaded_audio.wav', 'wb') as f:
    #             f.write(audio_data)
    #
    #             audio_segment = AudioSegment.from_file(BytesIO(audio_data))
    #             # Now you can play, modify, or export the audio_segment


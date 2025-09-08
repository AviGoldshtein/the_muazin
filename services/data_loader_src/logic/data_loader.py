import pathlib
import os
from services.data_loader_src.config import FILES_PATH
from services.data_loader_src.logic.logger import Logger


class DataLoader:
    def __init__(self):
        self.files_path = FILES_PATH
        self.logger = Logger.get_logger(name=__name__)

    def list_fils(self) -> list[pathlib.Path]:
        self.logger.info("loading all the files.")
        str_files = os.listdir(self.files_path)
        files_objects = []
        for file in str_files:
            file_object = self.files_path / file
            files_objects.append(file_object)
        return files_objects


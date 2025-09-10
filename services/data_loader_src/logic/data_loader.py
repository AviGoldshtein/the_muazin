import pathlib
import os
from services.shared.config import CONFIG
from services.shared.logger import Logger


class DataLoader:
    def __init__(self):
        """initialize with the path of the files to work with."""
        self.files_path = CONFIG['data_loader_src']['files_path']
        self.logger = Logger.get_logger(name=__name__)

    def list_fils(self) -> list[pathlib.Path]:
        """
        list a list of the files in a Path object format.
        :return: a list of pathlib.Path objects.
        """
        self.logger.info("loading all the files.")
        str_files = os.listdir(self.files_path)
        files_objects = []
        for file in str_files:
            file_object = self.files_path / file
            files_objects.append(file_object)
        return files_objects


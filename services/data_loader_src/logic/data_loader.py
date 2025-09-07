import pathlib
import os
from services.data_loader_src.config import FILES_PATH


class DataLoader:
    def __init__(self):
        self.files_path = FILES_PATH

    def list_fils(self) -> list[pathlib.Path]:
        str_files = os.listdir(self.files_path)
        files_objects = []
        for file in str_files:
            file_object = self.files_path / file
            files_objects.append(file_object)
        return files_objects


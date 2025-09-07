import pathlib
import os


class DataLoader:
    def __init__(self):
        root_path = pathlib.Path(__file__).resolve().parent.parent
        self.files_path = root_path / "data" / "podcasts"

    def list_fils(self) -> list[pathlib.Path]:
        str_files = os.listdir(self.files_path)
        files_objects = []
        for file in str_files:
            file_object = self.files_path / file
            files_objects.append(file_object)
        return files_objects


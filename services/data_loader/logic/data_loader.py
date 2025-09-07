import pathlib
import os


class DataLoader:
    def __init__(self):
        root_path = pathlib.Path(__file__).resolve().parent.parent
        self.files_path = root_path / "data" / "podcasts"

    def list_fils(self) -> list:
        return os.listdir(self.files_path)


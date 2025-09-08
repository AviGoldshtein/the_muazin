from pathlib import Path
import datetime
from dateutil import parser
from services.data_loader_src.logic.logger import Logger


class MetaExtractor:
    def __init__(self):
        self.logger = Logger.get_logger(name=__name__)

    def extract_metadata(self, file_path: Path) -> dict:
        self.logger.debug(f"extracting metadata for file: '{file_path.name}'.")
        file_stats = file_path.stat()
        metadata = {
            "File_path": str(file_path),
            "File_size": file_stats.st_size,
            "File_name": file_path.name,
            "Creation_time": self._proper_date(str(datetime.datetime.fromtimestamp(file_stats.st_ctime)))
        }
        return metadata

    def _proper_date(self, date: str) -> str:
        dt = parser.parse(date)
        return dt.isoformat()
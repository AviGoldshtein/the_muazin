from pathlib import Path
import datetime


class MetaExtractor:

    def extract_metadata(self, file_path: Path) -> dict:
        file_stats = file_path.stat()
        metadata = {
            "File_path": str(file_path),
            "File_size": file_stats.st_size,
            "File_name": file_path.name,
            "Creation_time": str(datetime.datetime.fromtimestamp(file_stats.st_ctime))
        }
        return metadata
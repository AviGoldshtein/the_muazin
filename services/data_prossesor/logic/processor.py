import hashlib


class Processor:
    @staticmethod
    def generate_id(file_name) -> str:
        return hashlib.sha256(file_name.encode('utf-8')).hexdigest()
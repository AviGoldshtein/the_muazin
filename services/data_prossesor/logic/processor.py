import hashlib


class Processor:
    @staticmethod
    def generate_id(str_parameters) -> str:
        """generate a sha256 unique id, based on unique parameters"""
        return hashlib.sha256(str_parameters.encode('utf-8')).hexdigest()
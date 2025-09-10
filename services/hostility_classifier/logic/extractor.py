import base64
import pathlib


class Extractor:
    def __init__(self):
        self.__black_lists_path = pathlib.Path(__file__).parent / "black_lists"

    def get_extracted_high_hostility_expressions(self) -> list:
        """return a decoded list of the high hostility expressions"""
        return self._open_and_extract_file("high_hostility.txt")

    def get_extracted_low_hostility_expressions(self):
        """return a decoded list of the low hostility expressions"""
        return self._open_and_extract_file("low_hostility.txt")

    def _open_and_extract_file(self, file_name: str) -> list:
        """
        extract a list of words encoded in base64.
        :return: a decoded list.
        """
        file_path = self.__black_lists_path / file_name
        with open(file_path, mode="r", encoding="utf-8") as f:
            encoded_wors_str = f.read()
            decoded_words_str = self._extractBase64(encoded_wors_str)
            high_hostility_expressions_list = decoded_words_str.lower().split(sep=",")
        return high_hostility_expressions_list


    def _extractBase64(self ,string: str) -> str:
        """the actual extraction"""
        decoded_bytes = base64.b64decode(string)
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string
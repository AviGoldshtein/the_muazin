from services.hostility_classifier.logic.extractor import Extractor
import re


class Classifier:
    def __init__(self):
        self.extractor = Extractor()

    def calculate_bds_percent(self, text: str) -> float:
        """
        calculate the cds percentage for the given text.
        :param text: the text to calculate on.
        :return: the percentage in a float number.
        """
        high_hostility_expressions = self.extractor.get_extracted_high_hostility_expressions()
        low_hostility_expressions = self.extractor.get_extracted_low_hostility_expressions()

        high_hostility_precent = self._calculate_bds_for_expressions(high_hostility_expressions, text)
        low_hostility_precent = self._calculate_bds_for_expressions(low_hostility_expressions, text)

        if low_hostility_precent > 0:
            low_hostility_precent /= 2

        bds_percent = high_hostility_precent + low_hostility_precent
        return bds_percent * 100

    def decide_is_bds(self, bds_percent: float, threshold: int = 5) -> bool:
        """return True if ist above the threshold, otherwise False."""
        return bds_percent > threshold

    def classify_bds_threat_level(self, bds_percent: float) -> str:
        """
        classify the level of the text by the bds precent, to one of three levels.
        :param bds_percent: the percentage representing the hostility of the text.
        :return: the level.
        """
        if bds_percent > 5:
            return "high"
        elif bds_percent > 0:
            return "medium"
        else:
            return "none"

    def _calculate_bds_for_expressions(self, expressions: list, text: str) -> float:
        """
        count for every expression how many times it appears in the text, and collect it together.
        divide the number of points by the number of words in the text,
        in order to get the percentage of the problematic words in the text.
        :param expressions: a list of problematic words.
        :param text: the text to search in.
        :return: the percentage of the problematic words, in a float number.
        """
        cleaned_text = self._clean_text(text)
        points = 0
        for expression in expressions:
            num_occurrences = len(re.findall(pattern=f"{expression}", string=cleaned_text))
            points += num_occurrences
        num_of_words = len(cleaned_text.split())

        if points > 0:
            points /= num_of_words
        return points

    def _clean_text(self, text: str) -> str:
        """remove dots and punctuation marks from the text, and lower the text."""
        lower_text = text.lower()
        removed_punctuation_text = lower_text.replace(".", "").replace(",", "")
        return removed_punctuation_text
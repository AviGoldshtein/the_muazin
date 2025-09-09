from services.hostility_classifier.logic.extractor import Extractor


class Classifier:
    def __init__(self):
        self.extractor = Extractor()

    def calculate_bds_percent(self, text: str) -> int:
        high_hostility_expressions = self.extractor.get_extracted_high_hostility_expressions()
        low_hostility_expressions = self.extractor.get_extracted_low_hostility_expressions()
        return 100

    def decide_is_bds(self, bds_percent: int) -> bool:
        return True

    def classify_bds_threat_level(self, bds_percent, is_bds) -> str:
        return "yes"
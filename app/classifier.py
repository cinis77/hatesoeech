import logging
from pathlib import Path

from app.result import Result
from app.svc import SVC
from app.fast_text import FastTextModel
from utils.text_utils import tokenize

logger = logging.getLogger(__name__)


class Classifier:
    file_location_model = Path("./model/supervised.bin")
    file_location_svc = Path('./model/fasttext_svc.pkl')
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Classifier.__instance is None:
            Classifier()
        return Classifier.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Classifier.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Classifier.__instance = self
            Classifier.__instance._load()

    def _load(self):
        logger.debug("Starting")
        self.svc = SVC()
        self.svc.load(str(Classifier.file_location_svc))

        self.fasttext_model = FastTextModel()
        self.fasttext_model.load_model(str(Classifier.file_location_model))

        logger.debug("Initialised")

    def check(self, text):
        logger.info("Checking: %s", text)
        tokens = tokenize(text)
        vectors = self.fasttext_model.get_vectors(tokens)
        pred = int(self.svc.predict([vectors])[0])
        logger.info("Prediction: %s", pred)
        index = 1 - pred
        probability = float(self.svc.predict_proba([vectors])[index])
        logger.info("Score: %10.4f", probability)
        return Result(probability, text, pred)

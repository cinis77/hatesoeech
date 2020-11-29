import logging
import fasttext
import numpy as np

logger = logging.getLogger(__name__)


class FastTextModel:

    def __init__(self):
        self.model = None
        logger.debug("Initialised")

    def load_model(self, filename):
        self.model = fasttext.load_model(str(filename))
        logger.debug("Loaded Model from %s", filename)

    def get_vectors(self, tokens):
        x = np.zeros(self.model.get_dimension())
        for token in tokens:
            x[:] += self.model.get_word_vector(token)
        return x

    def train_supervised(self):
        pass

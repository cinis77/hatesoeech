import logging
from sklearn.externals import joblib

logger = logging.getLogger(__name__)


class SVC:

    def __init__(self):
        self.clf = None
        logger.debug("Initialised")

    def load(self, filename):
        self.clf = joblib.load(filename)
        logger.debug("Loaded Model from %s", filename)

    def predict(self, vectors):
        return 1 - self.clf.predict(vectors)

    def predict_proba(self, vectors):
        return self.clf.predict_proba(vectors)[0]

    def fit(self):
        pass

import logging
from enum import Enum

logger = logging.getLogger(__name__)


class Type(Enum):
    NEUTRAL = 0
    HATE = 1


class Train:
    def __init__(self):
        logger.debug("Initialised")

    def add(self, text, type):
        pass

    def retrain(self):
        pass


if __name__ == "__main__":
    print("train file")
import unittest
from pathlib import Path
from unittest import TestCase

import numpy as np

from app.fast_text import FastTextModel

file_location = Path("../model/supervised.bin")


class TestFastTextModel(TestCase):

    def setUp(self):
        self.ft = FastTextModel()
        self.ft.load_model(file_location)

    def test_load_model(self):
        self.assertIsNotNone(self.ft.model)

    def test_get_vectors(self):
        vectors = self.ft.get_vectors(["medis", "aš"])
        self.assertEqual(len(vectors), 100)
        self.assertIsInstance(vectors, np.ndarray)

    # def test_train_supervised(self):
    #         self.fail()


if __name__ == '__main__':
    unittest.main()
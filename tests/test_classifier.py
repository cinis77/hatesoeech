import unittest
from pathlib import Path
from pprint import pprint
from unittest import TestCase

import numpy as np

from app.classifier import Classifier
from app.fast_text import FastTextModel

file_location = Path("../model/supervised.bin")


class TestClassifier(TestCase):

    def setUp(self):
        Classifier.file_location_model = Path("../model/supervised.bin")
        Classifier.file_location_svc = Path('../model/fasttext_svc.pkl')
        self.cl = Classifier.getInstance()

    def test_check_true(self):
        print(self.cl)
        result = self.cl.check("Putleris yra pyderastas. Supistas pyderastas.")
        print(result)
        self.assertIsNotNone(result)

    def test_check_false(self):
        print(self.cl)
        result = self.cl.check(
            "Labas, esu Jurgita is Kauno. Na o toliau tarp.")
        print(result)
        self.assertIsNotNone(result)

    def test_check_false2(self):
        print(self.cl)
        result = self.cl.check(
            "Sveiki as grįžau namo")
        print(result)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()

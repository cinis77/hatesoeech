from unittest import TestCase
import configparser
import os

import requests

import utils.config_parser as cfg


# cfg["logging"] = os.environ.get('LOGGING', config.get("DEFAULT", "Logging"))
# cfg["gui"] = bool(os.environ.get('GUI', config.get("GUI", "Enabled")))
# cfg["port"] = int(os.environ.get('PORT', config.get("GUI", "Port")))
# cfg["kafka"] = bool(os.environ.get('KAFKA', config.get("KAFKA", "Enabled")))
# cfg["timeout"] = int(os.environ.get('TIMEOUT', config.get("KAFKA", "Timeout")))
# cfg["topic"] = os.environ.get('TOPIC', config.get("KAFKA", "Topic"))


class TestLoad(TestCase):

    def setUp(self):
        self.config = configparser.ConfigParser()
        self.config.read('../config.ini')

    def test_config_parser_logging(self):
        print(self.config)


# os.putenv("LOGGING", "DEBUG")
# self.config['DEFAULT'] = {}
# self.config.has_section()
# cfg.load(self.config)
# cfg.get().get("logging")
# self.assertTrue(cfg.get().get("logging") == "DEBUG")

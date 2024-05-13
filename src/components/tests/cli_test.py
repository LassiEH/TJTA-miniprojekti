import unittest
from unittest.mock import patch
from ..cli import Cli

class TestCli(unittest.TestCase):
    def setUp(self):
        self.cli = Cli(lahteet=[])
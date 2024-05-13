import unittest
from unittest.mock import patch
from ..cli import Cli

class TestCli(unittest.TestCase):
    def setUp(self):
        self.cli = Cli(lahteet=[])

    @patch('builtins.input', side_effect=['1'])
    def test_aloitus_add_source(self, mock_input):
        with patch('builtins.print') as mock_print:
            self.assertEqual(self.cli.aloitus(), 1)
            
    @patch('builtins.input', side_effect=['2'])
    def test_aloitus_print_sources(self, mock_input):
        with patch('builtins.print') as mock_print:
            self.assertEqual(self.cli.aloitus(), 2)
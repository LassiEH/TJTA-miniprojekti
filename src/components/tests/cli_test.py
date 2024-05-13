import unittest
from unittest.mock import patch
from ..cli import Cli

class TestCli(unittest.TestCase):
    def setUp(self):
        self.cli = Cli(lahteet=[])

    """
    Testaa inputit mockeilla
    """
    @patch('builtins.input', side_effect=['1'])
    def test_aloitus_add_source(self, mock_input):
        with patch('builtins.print') as mock_print:
            self.assertEqual(self.cli.aloitus(), 1)

    @patch('builtins.input', side_effect=['2'])
    def test_aloitus_print_sources(self, mock_input):
        with patch('builtins.print') as mock_print:
            self.assertEqual(self.cli.aloitus(), 2)

    @patch('builtins.input', side_effect=['3'])
    def test_aloitus_generate_file(self, mock_input):
        with patch('builtins.print') as mock_print:
            self.assertEqual(self.cli.aloitus(), 3)

    @patch('builtins.input', side_effect=['4'])
    def test_aloitus_show_help(self, mock_input):
        with patch('builtins.print') as mock_print:
            self.assertEqual(self.cli.aloitus(), 4)

    @patch('builtins.input', side_effect=['invalid_type'])
    def test_lisaa_lahde_invalid_input(self, mock_input):
        with patch('builtins.print') as mock_print:
            self.cli.lisaa_lahde()
            mock_print.assert_called_with("Virheellinen viitetyyppi.")

import unittest
from unittest.mock import patch
from ..poweruserUI import PoweruserUI

class TestPoweruserUI(unittest.TestCase):
    def test_show_help(self):
        with patch('builtins.print') as mock_print:
            ui = PoweruserUI([], ["script_name", "--h"])
            mock_print.assert_called_with(ui.ohjeet)

    def test_add_source(self):
        pass
    #TODO luo testi
    def test_invalid_argument(self):
        with patch('builtins.print') as mock_print:
            ui = PoweruserUI([], ["script_name", "--invalid"])
            mock_print.assert_called_with(ui.ohjeet)

    def test_no_arguments(self):
        with patch('builtins.print') as mock_print:
            ui = PoweruserUI([], ["script_name"])
            mock_print.assert_called_with(ui.ohjeet)

    def test_too_many_arguments(self):
        with patch('builtins.print') as mock_print:
            ui = PoweruserUI([], ["script_name", "arg1", "arg2", "arg3"])
            #mock_print.assert_called_with("\nVirhe: Liian monta argumenttia\n")
            mock_print.assert_called_with(ui.ohjeet)
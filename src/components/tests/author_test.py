import unittest
from ..author import Author

class TestAuthor(unittest.TestCase):
    def setUp(self):
        self.testauth = Author("Virtanen", "Matti")
        self.testauthwofn = Author("Jokinen")
        self.testauthwmfn = Author("Nieminen", "Teppo Seppo")
        self.extrawhitespace = Author("Nieminen", "Teppo          Seppo")

    def test_constructor(self):
        self.assertEqual(self.testauth.firstname, "Matti")
        self.assertEqual(self.testauth.lastname, "Virtanen")
    
    def test_normal_stringify(self):
        self.assertEqual(str(self.testauth), "Virtanen, Matti")
    
    def test_no_first_name_stringify(self):
        self.assertEqual(str(self.testauthwofn), "Jokinen")
    
    def test_many_first_names_stringify(self):
        self.assertEqual(str(self.testauthwmfn), "Nieminen, Teppo Seppo")
    
    def test_apa_stringify(self):
        self.assertEqual(self.testauth.apastr(), "Virtanen, M.")
        self.assertEqual(self.testauthwofn.apastr(), "Jokinen")
        self.assertEqual(self.testauthwmfn.apastr(), "Nieminen, T. S.")
        self.assertEqual(self.extrawhitespace.apastr(), "Nieminen, T. S.")
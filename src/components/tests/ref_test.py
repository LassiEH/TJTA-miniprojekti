import unittest
from ..ref import Ref
from ..references import References
from ..author import Author

class TestRef(unittest.TestCase):

    def setUp(self):
        self.testauthor1 = Author("Author1")
        self.testauthor2 = Author("Author2")
        self.references = References()
        self.ref1 = Ref([self.testauthor1, self.testauthor2], "Test Article", 2020, 3, "3-5", ["userkey1", "userkey2"], "testarticle2020", journal = "Test Journal")
        self.ref2 = Ref([self.testauthor1, self.testauthor2], "Test Article", 2020, 3, "3-5", ["userkey1", "userkey2"], "testarticle2021", conf_name = "Test Conf", location = "Turku", organization = "Test Org", publisher = "Test Publisher")


    def test_constructor(self):
        self.assertEqual([self.testauthor1, self.testauthor2], self.ref1.author)
        self.assertEqual("Test Article", self.ref1.title)
        self.assertEqual("Test Journal", self.ref1.journal)
        self.assertEqual(2020, self.ref1.year)
        self.assertEqual(3, self.ref1.volume)
        self.assertEqual("3-5", self.ref1.pages)
        self.assertEqual(["userkey1", "userkey2"], self.ref1.userkeys)
        self.assertEqual("testarticle2020", self.ref1.bibtexkey)
        self.assertEqual("Test Conf", self.ref2.conf_name)
        self.assertEqual("Turku", self.ref2.location)
        self.assertEqual("Test Org", self.ref2.organization)
        self.assertEqual("Test Publisher", self.ref2.publisher)


    def test_string_representation(self):
        expected_output1 = "Author1, Author2. (2020). Test Article. Test Journal, 3: 3-5."
        self.assertEqual(expected_output1, str(self.ref1))
        expected_output2 = "Author1, Author2. (2020). Test Article. Test Conf, volume 3, pages 3-5, Turku, Test Org, Test Publisher."
        self.assertEqual(expected_output2, str(self.ref2))
    
    def test_references_toString(self):
        self.assertEqual(self.references.toString(), "Lähteitä ei ole.")
        self.references.lisaaLahde(self.ref1)
        self.assertEqual(self.references.toString(), str(self.ref1))
        self.references.lisaaLahde(self.ref2)
        self.assertEqual(self.references.toString(), str(self.ref1)+"\n\n"+str(self.ref2))

    def test_is_key_taken(self):
        self.references.lisaaLahde(self.ref1)
        bool1 = self.references.is_key_taken("testarticle2020")
        self.assertEqual(bool1, True)
        bool2 = self.references.is_key_taken("testausartikkeli2020")
        self.assertEqual(bool2, False)

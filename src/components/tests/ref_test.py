import unittest
from ..ref import Ref
from ..references import References
from ..author import Author

class TestRef(unittest.TestCase):

    def setUp(self):
        self.testauthor1 = Author("Author1")
        self.testauthor2 = Author("Author2", "Firstname")
        self.references = References()
        self.references.remove_ref("*")
        self.ref1 = Ref("article", "testarticle2020", [self.testauthor1, self.testauthor2], dict({"title": "Test Article", "journal": "Test Journal", "year": 2020}), ["userkey1", "userkey2"])
        self.ref2 = Ref("inproceedings", "testarticle2021", [self.testauthor1, self.testauthor2], dict({"title": "Test Inproc", "journal": "Test Journal", "year": 2021, "conference": "Test Conf"}), ["userkey1", "userkey2"])
        
        author = [Author("Test", "John"), Author("Tester", "Peter")]
        bibdata = {"year": "2022", "title": "Example Title", "booktitle": "Example Book", "volume": "1", "pages": "1-10"}
        self.ref3 = Ref(artype="article", bibtexkey="Doe2022", author=author, bibdata=bibdata, userkeys=[])
        #self.ref2 = Ref([self.testauthor1, self.testauthor2], "Test Article", 2020, 3, "3-5", ["userkey1", "userkey2"], "testarticle2021", conf_name = "Test Conf", location = "Turku", organization = "Test Org", publisher = "Test Publisher")


    def test_constructor(self):
        self.assertEqual([self.testauthor1, self.testauthor2], self.ref1.author)
        self.assertEqual("Test Article", self.ref1.get_field("title"))
        self.assertEqual("Test Journal", self.ref1.get_field("journal"))
        self.assertEqual(2020, self.ref1.get_field("year"))
        self.assertEqual(["userkey1", "userkey2"], self.ref1.userkeys)
        self.assertEqual("testarticle2020", self.ref1.bibtexkey)
        self.assertEqual("Test Conf", self.ref2.get_field("conference"))
        #self.assertEqual("Turku", self.ref2.location)
        #self.assertEqual("Test Org", self.ref2.organization)
        #self.assertEqual("Test Publisher", self.ref2.publisher)

    def test_string_representation(self):
        expected_output1 = "article (testarticle2020)\nAuthor1, Author2 Firstname. \ntitle: Test Article\njournal: Test Journal\nyear: 2020\nuserkey1, userkey2\n"
        self.assertEqual(expected_output1, str(self.ref1))
        expected_output2 = "inproceedings (testarticle2021)\nAuthor1, Author2 Firstname. \ntitle: Test Inproc\njournal: Test Journal\nyear: 2021\nconference: Test Conf\nuserkey1, userkey2\n"
        self.assertEqual(expected_output2, str(self.ref2))
    
    def test_references_string(self):
        self.assertEqual(str(self.references), "Lähteitä ei ole.")
        self.references.lisaaLahde(self.ref1)
        self.assertEqual(str(self.references), str(self.ref1))
        self.references.lisaaLahde(self.ref2)
        self.assertEqual(str(self.references), str(self.ref1)+"\n\n"+str(self.ref2))

    """
    Avainsana on käytössä testaus
    """
    def test_is_key_taken(self):
        self.references.lisaaLahde(self.ref1)
        bool1 = self.references.is_key_taken("testarticle2020")
        self.assertEqual(bool1, True)
        bool2 = self.references.is_key_taken("testausartikkeli2020")
        self.assertEqual(bool2, False)

    """
    APA-testaus
    """
    def test_apa_str(self):
        expected_output = "Test, J., & Tester, P. (2022). Example Title, Example Book, 1, 1-10."
        self.assertEqual(self.ref3.apastr(), expected_output)

    """
    BibTex-merkkijonon testaus
    """
    def test_bibtex_str(self):
        expected_output = "@article{testarticle2020,\n  author={Author1 and Author2, Firstname},\n  title={Test Article},\n  journal={Test Journal},\n  year={2020}\n}"
        self.assertEqual(self.ref1.bibtexstr(), expected_output)

    """
    remove_ref-testaus
    """
    def test_remove_ref(self):
        self.references.lisaaLahde(self.ref1)
        self.references.lisaaLahde(self.ref2)
        self.references.remove_ref("testarticle2020")        
        self.assertEqual(str(self.references), str(self.ref2))
        self.references.lisaaLahde(self.ref1)
        self.references.remove_ref("*")
        self.assertEqual(str(self.references), "Lähteitä ei ole.")

    """
    generate_toml_str-testaus
    """
    def test_generate_toml_str(self):
        expected_output = ""
        tomlstr = self.references.generate_toml_str()
        self.assertEqual(expected_output, tomlstr)
        self.references.lisaaLahde(self.ref1)
        expected_output2 = "[testarticle2020]\nartype = \"article\"\nauthors = [ \"Author1\", \"Author2 Firstname\",]\nuserkeys = [ \"userkey1\", \"userkey2\",]\ntitle = \"Test Article\"\njournal = \"Test Journal\"\nyear = 2020\n\n"
        tomlstr2 = self.references.generate_toml_str()
        self.assertEqual(expected_output2, tomlstr2)
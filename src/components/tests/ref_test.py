import unittest
from ref import Ref
from references import References

class TestRef(unittest.TestCase):

    def setUp(self):
        self.references = References()
        self.ref1 = Ref(["Author1", "Author2"], "Test Article", "Test Journal", 2020, 3, 5, ["userkey1", "userkey2"])

    def test_constructor(self):
        self.assertEqual(["Author1", "Author2"], self.ref1.author)
        self.assertEqual("Test Article", self.ref1.title)
        self.assertEqual("Test Journal", self.ref1.journal)
        self.assertEqual(2020, self.ref1.year)
        self.assertEqual(3, self.ref1.volume)
        self.assertEqual(5, self.ref1.pages)
        self.assertEqual(["userkey1", "userkey2"], self.ref1.userkeys)

    def test_string_representation(self):
        expected_output = "Author1, Author2. Test Article: Test Journal, 3. 5, 2020"
        self.assertEqual(expected_output, str(self.ref1))
    
    def test_references_toString(self):
        self.assertEqual(self.references.toString(), "Lähteitä ei ole.")
        self.references.lisaaLahde(Ref(["Author3", "Author4"], "Test Article", "Test Journal", 2021, 4, 6, ["userkey1", "userkey3"]))
        self.assertEqual(self.references.toString(), "Author3, Author4. Test Article: Test Journal, 4. 6, 2021")
        self.references.lisaaLahde(self.ref1)
        self.assertEqual(self.references.toString(), "Author3, Author4. Test Article: Test Journal, 4. 6, 2021"+"\n\n"+"Author1, Author2. Test Article: Test Journal, 3. 5, 2020")

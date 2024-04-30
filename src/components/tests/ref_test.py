import unittest
from ref import Ref

class TestRef(unittest.TestCase):

    def setUp(self):
        self.ref1 = Ref(["Author1", "Author2"], "Test Article", "Test Journal", 2020, 3, 5)

    def test_constructor(self):
        self.assertEqual(["Author1", "Author2"], self.ref1.author)
        self.assertEqual("Test Article", self.ref1.title)
        self.assertEqual("Test Journal", self.ref1.journal)
        self.assertEqual(2020, self.ref1.year)
        self.assertEqual(3, self.ref1.volume)
        self.assertEqual(5, self.ref1.pages)

    def test_string_representation(self):
        expected_output = "Author1, Author2. Test Article: Test Journal, 3. 5, 2020"
        self.assertEqual(expected_output, str(self.ref1))
import unittest
from ref import Ref

class TestRef(unittest.TestCase):

    def setUp(self):
        self.ref1 = Ref("Test Author", "Test Article", "Test Journal", 2020, 3, 5)

    def test_constructor(self):
        self.assertEqual("Test Author", self.ref1.author)

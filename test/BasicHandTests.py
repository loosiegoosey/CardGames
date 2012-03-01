import unittest
from CardGame import Hand

class Tests(unittest.TestCase):

    def test_abstract_class(self):
        hand = Hand()
        self.assertRaises(Exception, hand.evaluate, [])


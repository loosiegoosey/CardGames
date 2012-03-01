import unittest
from src.CardGame import Card
from src.PokerHand import *

class Tests(unittest.TestCase):


    def setUp(self):
        self.high_card_hand_1 = [Card('4','D'), Card('K','H'), Card('3','D'), Card('10','D'), Card('J','D')]
        self.high_card_hand_2 = [Card('2','D'), Card('K','H'), Card('4','D'), Card('10','D'), Card('J','D')]
        self.one_pair = [Card('2','D'), Card('2','H'), Card('3','D'), Card('10','D'), Card('J','D')]
        self.two_pairs = [Card('2','D'), Card('2','H'), Card('3','D'), Card('10','D'), Card('10','H')]
        self.trio = [Card('2','D'), Card('2','H'), Card('2','S'), Card('10','D'), Card('J','D')]
        self.straight = [Card('2','D'), Card('3','H'), Card('4','D'), Card('5','D'), Card('6','H')]
        self.flush = [Card('2','D'), Card('3','D'), Card('7','D'), Card('10','D'), Card('J','D')]
        self.full_house = [Card('2','D'), Card('2','H'), Card('2','S'), Card('10','D'), Card('10','H')]
        self.poker = [Card('2','D'), Card('2','H'), Card('2','S'), Card('2','C'), Card('J','D')]
        self.straight_flush = [Card('5','D'), Card('6','D'), Card('7','D'), Card('8','D'), Card('9','D')]
        self.royal_flush_1 = [Card('10','D'), Card('J','D'), Card('Q','D'), Card('K','D'), Card('A','D')]
        self.royal_flush_2 = [Card('10','S'), Card('J','S'), Card('Q','S'), Card('K','S'), Card('A','S')]

        self.player_1 = Player('John', self.poker)
        self.player_2 = Player('Mary', self.flush)
        self.player_3 = Player('Peter', self.high_card_hand_1)
        self.player_4 = Player('Peter', self.high_card_hand_2)
        self.player_5 = Player('Chris', self.royal_flush_1)
        self.player_6 = Player('Joan', self.royal_flush_2)


    def test_evaluate_hand(self):
        he  = Poker_Hand_Evaluator()
        self.assertEqual(he.evaluate_hand(self.high_card_hand_1), 1)
        self.assertEqual(he.evaluate_hand(self.one_pair), 2)
        self.assertEqual(he.evaluate_hand(self.two_pairs), 3)
        self.assertEqual(he.evaluate_hand(self.trio), 4)
        self.assertEqual(he.evaluate_hand(self.straight), 5)
        self.assertEqual(he.evaluate_hand(self.flush), 6)
        self.assertEqual(he.evaluate_hand(self.full_house), 7)
        self.assertEqual(he.evaluate_hand(self.poker), 8)
        self.assertEqual(he.evaluate_hand(self.straight_flush), 9)
        self.assertEqual(he.evaluate_hand(self.royal_flush_1), 10)


    def test_if_is_flush(self):
        obj = Flush()
        self.assertTrue(obj.evaluate(self.flush))
        self.assertFalse(obj.evaluate(self.full_house))

    def test_if_is_straight(self):
        obj = Straight()
        self.assertTrue(obj.evaluate(self.straight))
        self.assertTrue(obj.evaluate(self.straight_flush))
        self.assertTrue(obj.evaluate(self.straight_flush))
        self.assertFalse(obj.evaluate(self.flush))

    def test_if_is_straight_flush(self):
        obj = Straight_Flush()
        self.assertTrue(obj.evaluate(self.straight_flush))
        self.assertTrue(obj.evaluate(self.royal_flush_1))
        self.assertFalse(obj.evaluate(self.straight))

    def test_if_is_royal_straight_flush(self):
        obj = Royal_Flush()
        self.assertTrue(obj.evaluate(self.royal_flush_2))
        self.assertFalse(obj.evaluate(self.straight_flush))
        self.assertFalse(obj.evaluate(self.straight))

    def test_if_is_high_card_hand(self):
        obj = High_Card()
        self.assertTrue(obj.evaluate(self.high_card_hand_1))
        self.assertTrue(obj.evaluate(self.high_card_hand_2))
        self.assertFalse(obj.evaluate(self.one_pair))

    def test_if_is_one_pair_hand(self):
        obj = One_Pair()
        self.assertTrue(obj.evaluate(self.one_pair))
        self.assertFalse(obj.evaluate(self.two_pairs))

    def test_if_is_two_pairs_hand(self):
        obj = Two_Pairs()
        self.assertTrue(obj.evaluate(self.two_pairs))
        self.assertFalse(obj.evaluate(self.one_pair))
        self.assertFalse(obj.evaluate(self.poker))

    def test_winner(self):
        he  = Poker_Hand_Evaluator()
        self.assertEqual(he.winner([self.player_1, self.player_2]), self.player_1)
        self.assertEqual(he.winner([self.player_4, self.player_3, self.player_1, self.player_2]), self.player_1)

    def test_ties(self):
        he  = Poker_Hand_Evaluator()
        self.assertEqual(he.winner([self.player_3, self.player_4]), self.player_4)
        self.assertEqual(he.winner([self.player_4, self.player_3]), self.player_4)

    def test_real_tie(self):
        he  = Poker_Hand_Evaluator()
        self.assertRaises(TieException, he.winner, [self.player_5, self.player_6])


class Players_Tests(unittest.TestCase):

    def test_equals(self):
        card_x = Card('J','D')
        poker = [Card('2','D'), Card('2','H'), Card('2','S'), Card('2','C'), card_x]
        p1 = Player('John', poker)
        self.assertNotEqual(p1, poker)
        self.assertNotEqual(p1, card_x)
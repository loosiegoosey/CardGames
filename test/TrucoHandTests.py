import unittest
from TrucoHand import Truco_Card, Truco_Hand_Evaluator

class Tests(unittest.TestCase):

    def setUp(self):
        self.espadao = Truco_Card('A','S')
        self.bastiao = Truco_Card('A','C')
        self.manilha_espada = Truco_Card('7','S')
        self.manilha_ouro = Truco_Card('7','D')
        self.tres_espada = Truco_Card('3','D')
        self.ovo_ouro = Truco_Card('A','D')


    def test_winner(self):
        obj = Truco_Hand_Evaluator()
        self.assertEqual(obj.winner([self.espadao,self.manilha_espada]), self.espadao)
        self.assertEqual(obj.winner([self.manilha_ouro,self.manilha_espada]), self.manilha_espada)
        self.assertEqual(obj.winner([self.ovo_ouro, self.tres_espada, self.bastiao]), self.bastiao)

    def test_different_cards(self):
        self.assertNotEqual(self.espadao, self.manilha_espada)
'''
This file was generated as an exercise for testing pyCharm, based in the Poker code.
'''

from src.CardGame import Card

class Truco_Card(Card) :

    truco_card_strength = {'4':1,'5':2,'6':3,'7':4,'10':5,'11':6,'12':7,'A':8,'2':9,'3':10}

    def __init__(self, value, suit):
        super(Truco_Card, self).__init__(value, suit)
        self.rank = self._define_rank(value,suit)

    def __cmp__(self, other):
        return self.rank - other.rank

    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return not self == other

    def _define_rank(self,value,suit):
        if self._isSpecial() :
            if value == '7' and suit == 'S' :
                return 12
            if value == 'A' :
                if suit == 'C' :
                    return 13
                else :
                    return 14
            return 11
        else :
            return self.truco_card_strength[value]


    def _isSpecial(self) :
        if self.number == 14 and (self.suit == 'C' or self.suit == 'S') :
            return True
        if self.number == 7 and (self.suit == 'D' or self.suit == 'S') :
            return True
        return False


class Truco_Hand_Evaluator(object):

    def winner(self, cards):
        return max(cards)
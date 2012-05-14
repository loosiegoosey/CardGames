from collections import defaultdict

class Card(object):

    card_values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}

    def __init__(self, value, suit):
        self.number = self.card_values[value]
        self.suit = suit


class Hand(object):

    def evaluate(self, hand):
        raise Exception('not yet implemented')

    def _get_cards_value(self, hand):
        return sorted(map(lambda card: card.number, hand))

    def _same_suit(self, hand):
        return len(set(map(lambda card: card.suit, hand))) == 1

    def _get_occurrences(self, hand):
        counter = defaultdict(int)
        for i in self._get_cards_value(hand) :
            counter[i] += 1
        return counter


'''
This file was generated inspired in Project Euler exercise number 54.
'''
from CardGame import Hand

class Poker_Ranking(object):

    def __init__(self, hand, rank):
        self.hand = hand
        self.rank = rank

    def evaluate(self, cards):
        return self.hand.evaluate(cards)

    def __cmp__(self, other):
        return self.rank - other.rank


class PokerHand(Hand):

    def _has_double_values(self, hand):
        return len(set(self._get_cards_value(hand))) < 5

    def _has_a_pair(self, hand):
        return len(filter(lambda x: x == 2, self._get_occurrences(hand).values())) == 1

    def _has_a_trio(self, hand):
        return len(filter(lambda x: x == 3, self._get_occurrences(hand).values())) == 1


class Flush(PokerHand):

    def evaluate(self, hand):
        return self._same_suit(hand)


class Straight(PokerHand):

    def _is_straight(self, hand):
        cards_value = self._get_cards_value(hand)
        return cards_value == range(cards_value[0],cards_value[0]+5)

    def evaluate(self, hand):
        return self._is_straight(hand)


class Straight_Flush(Flush, Straight):

    def evaluate(self,hand):
        return self._is_straight(hand) and self._same_suit(hand)


class Royal_Flush(Straight_Flush):

    def _is_straight(self, hand):
        cards_value = self._get_cards_value(hand)
        return cards_value == range(10,15)


class High_Card(PokerHand):

    def evaluate(self,hand):
        return not self._has_double_values(hand) and not self._same_suit(hand)


class One_Pair(PokerHand):

    def evaluate(self,hand):
        return len(set(map(lambda card: card.number, hand))) == 4


class Two_Pairs(PokerHand):

    def evaluate(self, hand):
        return len(filter(lambda x: x == 2, self._get_occurrences(hand).values())) == 2


class Trio(PokerHand):

    def evaluate(self, hand):
        return self._has_a_trio(hand) and not self._has_a_pair(hand)


class Full_House(PokerHand):

    def evaluate(self, hand):
        return self._has_a_trio(hand) and self._has_a_pair(hand)


class Poker(PokerHand):

    def evaluate(self, hand):
        return len(filter(lambda x: x == 4, self._get_occurrences(hand).values())) == 1


class TieException(Exception):
    pass


class Poker_Hand_Evaluator(object):

    rankings = [Poker_Ranking(Royal_Flush(), 10), Poker_Ranking(Straight_Flush(), 9), Poker_Ranking(Poker(), 8),\
                Poker_Ranking(Full_House(), 7), Poker_Ranking(Flush(), 6), Poker_Ranking(Straight(), 5),\
                Poker_Ranking(Trio(), 4), Poker_Ranking(Two_Pairs(), 3), Poker_Ranking(One_Pair(), 2),\
                Poker_Ranking(High_Card(), 1)]

    def evaluate_hand(self, cards):
        if len(cards) != 5 : raise Exception('Hand has not 5 cards')
        return max(filter(lambda hand: hand.evaluate(cards), self.rankings)).rank


    def winning_player(self, player1, player2):
        if self.evaluate_hand(player1.cards) == self.evaluate_hand(player2.cards):
            return self.tie_break([player1,player2])
        elif self.evaluate_hand(player1.cards) > self.evaluate_hand(player2.cards):
            return player1
        else:
            return player2

    def winner(self, players):
        return reduce(self.winning_player, players)

    def tie_break(self, players):
        p1 = sum(map(lambda card: card.number, players[0].cards))
        p2 = sum(map(lambda card: card.number, players[1].cards))
        if p1 == p2 :
            raise TieException('Tie!')
        elif p1 > p2 :
            return players[0]
        else :
            return players[1]


class Player(object) :

    def __init__(self, name, cards) :
        self.name = name
        self.cards = cards

    def __eq__(self, other):
        return (self.name == other.name) and (self.cards == self.cards)
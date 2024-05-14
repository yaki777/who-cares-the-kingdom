from rpg_cards.cards_ren import Card

"""renpy
init -100 python:
"""
from collections import Counter

STRAIGHT_FLUSH = (9, "同花顺")
FOUR_OF_A_KIND = (8, "四条")
FULL_HOUSE = (7, "葫芦")
FLUSH = (6, "同花")
STRAIGHT = (5, "顺子")
THREE_OF_A_KIND = (4, "三条")
TWO_PAIR = (3, "两对")
ONE_PAIR = (2, "一对")
HIGH_CARD = (1, "高牌")


class BattleCalculator:
    def is_straight(self, cards):
        numbers = [card.number for card in cards]
        numbers.sort()
        return numbers == list(range(numbers[0], numbers[0] + 5))

    def is_flush(self, cards):
        if len(cards) < 5:
            return False
        suits = [card.suit for card in cards]
        return len(set(suits)) == 1

    def is_four_of_a_kind(self, cards):
        numbers = [card.number for card in cards]
        counts = Counter(numbers)
        return 4 in counts.values()

    def is_full_house(self, cards):
        numbers = [card.number for card in cards]
        counts = Counter(numbers)
        return sorted(counts.values()) == [2, 3]

    def is_three_of_a_kind(self, cards):
        numbers = [card.number for card in cards]
        counts = Counter(numbers)
        return 3 in counts.values()

    def is_two_pair(self, cards):
        numbers = [card.number for card in cards]
        counts = Counter(numbers)
        return sorted(counts.values()) == [1, 2, 2]

    def is_one_pair(self, cards):
        numbers = [card.number for card in cards]
        counts = Counter(numbers)
        return 2 in counts.values()

    def get_max_table(self, cards):
        table_rank = None
        table_score = 0
        cards = [card for card in cards if card is not None and isinstance(card, Card)]
        if self.is_straight(cards) and self.is_flush(cards):
            table_rank = STRAIGHT_FLUSH
            table_score = sum(card.number for card in cards)
        elif self.is_four_of_a_kind(cards):
            table_rank = FOUR_OF_A_KIND
            numbers = [card.number for card in cards]
            counts = Counter(numbers)
            quad, single = counts.most_common()[0][0], counts.most_common()[-1][0]
            table_score = quad * 4
        elif self.is_full_house(cards):
            table_rank = FULL_HOUSE
            numbers = [card.number for card in cards]
            counts = Counter(numbers)
            triple, pair = counts.most_common()[0][0], counts.most_common()[1][0]
            table_score = triple * 3 + pair * 2
        elif self.is_flush(cards):
            table_rank = FLUSH
            table_score = sum(card.number for card in cards)
        elif self.is_straight(cards):
            table_rank = STRAIGHT
            table_score = sum(card.number for card in cards)
        elif self.is_three_of_a_kind(cards):
            table_rank = THREE_OF_A_KIND
            numbers = [card.number for card in cards]
            counts = Counter(numbers)
            triple, rest = counts.most_common()[0][0], sorted(counts.most_common()[1:], reverse=True)
            table_score = triple * 3
        elif self.is_two_pair(cards):
            table_rank = TWO_PAIR
            numbers = [card.number for card in cards]
            counts = Counter(numbers)
            pairs = [num for num, count in counts.most_common()[:2]]
            table_score = sum(num * 2 for num in pairs)
        elif self.is_one_pair(cards):
            table_rank = ONE_PAIR
            numbers = [card.number for card in cards]
            counts = Counter(numbers)
            pair, rest = counts.most_common()[0][0], sorted(counts.most_common()[1:], reverse=True)
            table_score = pair * 2
        else:
            table_rank = HIGH_CARD
            table_score = max(card.number for card in cards)

        return table_rank, table_score

from rpg_cards.cards_ren import CARD_LIBRARY

"""renpy
init -100 python:
"""
import random


class CardsController:
    def __init__(self):
        self.decks = {
            'player': [],
            'enemy_test': [],
        }
        # for test
        for card in CARD_LIBRARY:
            self.player_get_card(card)
            self.decks['enemy_test'].append(card)

    def player_get_card(self, card):
        self.decks['player'].append(card)

    def player_discard_card(self, card):
        self.decks['player'].remove(card)

    def player_deck(self):
        return self.decks['player']

    def player_shuffle_deck(self):
        random.shuffle(self.decks['player'])

    def player_draw_cards(self, number=1):
        cards = []
        for i in range(number):
            card = self.decks['player'].pop(0)
            cards.append(card)
            self.decks['player'].append(card)
        return cards

    def enemy_shuffle_deck(self, enemy_id):
        random.shuffle(self.decks[enemy_id])

    def enemy_draw_cards(self, enemy_id, number=1):
        cards = []
        for i in range(number):
            card = self.decks[enemy_id].pop(0)
            cards.append(card)
            self.decks[enemy_id].append(card)
        return cards

    def enemy_register_cards(self, enemy_id, card_list):
        self.decks[enemy_id] = card_list

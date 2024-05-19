from rpg_battle.battle_actions_ren import ACTION_LIBRARY, BattleAction
from rpg_cards.cards_ren import CARD_SUITS

"""renpy
init -90 python:
"""
import random


class BattleActionController:
    def __init__(self):
        self.decks = {
            'player': [],
            'enemy_test': [],
        }
        # for test
        actions = random.sample(ACTION_LIBRARY, 20)
        for action in actions:
            self.decks['player'].append(BattleAction(*action, level=random.randint(2, 14),
                                                     suit=random.choice(CARD_SUITS)))

    def player_get_action(self, card):
        self.decks['player'].append(card)

    def player_discard_action(self, card):
        self.decks['player'].remove(card)

    def player_deck(self):
        return self.decks['player']

    def player_shuffle_deck(self):
        random.shuffle(self.decks['player'])

    def player_draw_cards(self, number=1):
        cards = []
        for i in range(number):
            action = self.decks['player'].pop(0)
            cards.append(action.card())
            self.decks['player'].append(action)
        return cards

    def enemy_shuffle_deck(self, enemy_id):
        random.shuffle(self.decks[enemy_id])

    def enemy_draw_cards(self, enemy_id, number=1):
        cards = []
        for i in range(number):
            action = self.decks[enemy_id].pop(0)
            cards.append(action.card())
            self.decks[enemy_id].append(action)
        return cards

    def enemy_register_actions(self, enemy_id, card_list):
        self.decks[enemy_id] = card_list

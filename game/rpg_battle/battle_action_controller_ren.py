from rpg_battle.battle_action_machine_ren import MACHINE_ACTION_LIBRARY
from rpg_battle.battle_actions_ren import ACTION_LIBRARY, BattleAction, THEME_LOVE
from rpg_cards.cards_ren import CARD_SUITS

"""renpy
init -90 python:
"""
import random


class BattleActionController:
    def __init__(self):
        self.decks = {
            'player': {
                THEME_LOVE: []
            },
        }
        # for test
        actions = random.sample(ACTION_LIBRARY, 20)
        for action in actions:
            self.decks['player'][THEME_LOVE].append(BattleAction(*action, level=random.randint(2, 14),
                                                                 suit=random.choice(CARD_SUITS)))

    def _apply_filter(self, action_library, ban_toys, ban_organs):
        ban_actions = set()
        for toy in ban_toys:
            for action in action_library:
                if len(action) > 7 and toy in action[7]:
                    ban_actions.add(action[0])

        for organ in ban_organs:
            for action in action_library:
                if len(action) > 6 and organ == action[6]:
                    ban_actions.add(action[0])
        action_library[:] = [action for action in action_library if action[0] not in ban_actions]

    def apply_filters(self, ban_toys, ban_organs):
        self._apply_filter(ACTION_LIBRARY, ban_toys, ban_organs)
        self._apply_filter(MACHINE_ACTION_LIBRARY, ban_toys, ban_organs)

    def player_get_action(self, action):
        if action.theme not in self.decks['player']:
            self.decks['player'][action.theme] = []
        self.decks['player'][action.theme].append(action)

    def player_discard_action(self, action):
        self.decks['player'][action.theme].remove(action)

    def player_deck(self):
        return self.decks['player']

    def player_shuffle_deck(self):
        for k, v in self.decks['player'].items():
            random.shuffle(v)

    def player_draw_cards(self, number=1, theme=THEME_LOVE):
        cards = []
        if theme not in self.decks['player']:
            theme = THEME_LOVE
        for i in range(number):
            action = self.decks['player'][theme].pop(0)
            cards.append(action.card())
            self.decks['player'][theme].append(action)
        return cards

    def enemy_shuffle_deck(self, enemy_id):
        for k, v in self.decks[enemy_id].items():
            random.shuffle(v)

    def enemy_draw_cards(self, enemy_id, number=1, theme=THEME_LOVE):
        cards = []
        if theme not in self.decks[enemy_id]:
            theme = THEME_LOVE
        for i in range(number):
            action = self.decks[enemy_id][theme].pop(0)
            cards.append(action.card())
            self.decks[enemy_id][theme].append(action)
        return cards

    def enemy_register_actions(self, enemy_id, action_list):
        if enemy_id not in self.decks:
            self.decks[enemy_id] = {}
        for action in action_list:
            if action.theme not in self.decks[enemy_id]:
                self.decks[enemy_id][action.theme] = []
            self.decks[enemy_id][action.theme].append(action)

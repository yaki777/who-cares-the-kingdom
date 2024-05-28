from rpg_battle.battle_action_library_ren import THEME_LOVE_LIBRARY, THEME_MACHINE_LIBRARY, THEME_SELF_LIBRARY, \
    THEME_GOBLIN_LIBRARY
from rpg_battle.battle_actions_ren import BattleAction, THEME_LOVE, THEME_SELF
from rpg_cards.cards_ren import CARD_SUITS
from rpg_world.organs_ren import ORGAN_LIBRARY
from rpg_world.toys_ren import TOY_LIBRARY

"""renpy
init -90 python:
"""
import random


class BattleActionController:
    def __init__(self):
        self.decks = {
            'player': {},
        }

    def _apply_filter(self, action_library, ban_toys, ban_organs):
        ban_actions = set()
        for toy in ban_toys:
            for action in action_library:
                if len(action) > 7 and action[7] is not None and isinstance(action[7], list) and toy in action[7]:
                    ban_actions.add(action[0])

        for organ in ban_organs:
            for action in action_library:
                if len(action) > 6 and action[6] is not None and isinstance(action[6], list) and organ in action[6]:
                    ban_actions.add(action[0])
        action_library[:] = [action for action in action_library if action[0] not in ban_actions]

    def apply_filters(self, allowed_toys, allowed_organs):
        ban_toys = list(filter(lambda toy: toy not in allowed_toys, TOY_LIBRARY))
        ban_organs = list(filter(lambda organ: organ not in allowed_organs, ORGAN_LIBRARY))
        self._apply_filter(THEME_LOVE_LIBRARY, ban_toys, ban_organs)
        self._apply_filter(THEME_MACHINE_LIBRARY, ban_toys, ban_organs)
        self._apply_filter(THEME_SELF_LIBRARY, ban_toys, ban_organs)
        self._apply_filter(THEME_GOBLIN_LIBRARY, ban_toys, ban_organs)

    def player_get_action(self, action):
        if action.theme not in self.decks['player']:
            self.decks['player'][action.theme] = []
        self.decks['player'][action.theme].append(action)

    def player_discard_action(self, action):
        self.decks['player'][action.theme].remove(action)

    def player_deck(self, theme=None):
        if theme is not None:
            return self.decks['player'][theme]
        else:
            return [item for sublist in self.decks['player'].values() for item in sublist]

    def player_shuffle_deck(self):
        for k, v in self.decks['player'].items():
            random.shuffle(v)

    def player_draw_cards(self, number, themes):
        cards = []
        available_themes = [theme for theme in themes if theme in self.decks['player']]
        available_themes.append(THEME_SELF)
        for i in range(number):
            available_themes = [theme for theme in themes
                                if theme in self.decks['player'] and len(self.decks['player'][theme]) > 0]
            if len(available_themes) == 0:
                break
            theme = random.choice(available_themes)
            action = self.decks['player'][theme].pop(0)
            cards.append(action.card())
        for card in cards:
            self.decks['player'][card.addition.theme].append(card.addition)
        return cards

    def enemy_shuffle_deck(self, enemy_id):
        for k, v in self.decks[enemy_id].items():
            random.shuffle(v)

    def enemy_draw_cards(self, enemy_id, number, themes):
        cards = []
        available_themes = [theme for theme in themes if theme in self.decks[enemy_id]]
        for i in range(number):
            theme = random.choice(available_themes)
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

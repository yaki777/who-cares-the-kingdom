import random

from rpg_battle.battle_actions_ren import TAGS, BattleAction, THEME_LOVE_LIBRARY
from rpg_cards.cards_ren import Card, CARD_SUITS
from rpg_dungeon.dungeon_area_ren import DungeonArea, DUNGEON_AREAS
from rpg_npc.npc_ren import NPC
from rpg_role.dungeon_roles_ren import *
from rpg_system.renpy_constant import renpy, npc_controller, battle_action_controller

"""renpy
init -50 python:
"""


class DungeonController:
    def __init__(self):
        self.available_area = {}
        for area in DUNGEON_AREAS:
            if area.theme not in self.available_area:
                self.available_area[area.theme] = []
            self.available_area[area.theme].append(area)
        self.current_area = self.available_area['base'][0]
        self.current_theme = 'base'
        self.dungeon_level = 1
        self.current_floor = 2
        self.player_hands = []
        self.placed_card = None
        self.failed = False

    def gen_enemy_list(self, enemy_count, available_roles=None):
        assert enemy_count <= 3
        enemy_list = []
        if enemy_count == 0:
            return enemy_list
        for i in range(enemy_count):
            if available_roles is None:
                available_roles = [role for role in DUNGEON_ROLES if
                                   f'dungeon_{self.current_theme}' in role.area_weights_day]

            role = random.choice(available_roles)
            weakness = random.sample(TAGS, random.randint(1, 3))
            npc_id = f'{role.code}_{i}'
            npc = NPC(npc_id, '无名', role, self.current_floor, weakness, True)
            npc.location = f'dungeon_{self.current_theme}_{self.current_floor}'
            # todo? different card pool for different role
            deck = []
            actions = random.sample(THEME_LOVE_LIBRARY, 20)
            for action in actions:
                deck.append(BattleAction(*action, level=random.randint(2, 14), suit=random.choice(CARD_SUITS)))
            battle_action_controller.enemy_register_actions(npc_id, deck)
            enemy_list.append(npc)
        return enemy_list

    def has_enemy(self):
        return any(isinstance(card.addition, NPC) and card.addition.is_enemy for card in self.player_hands)

    def start(self, dungeon_level):
        self.player_hands = []
        self.dungeon_level = dungeon_level
        self.current_floor = 2
        self.failed = False
        self.current_area = self.available_area['base'][0]
        self.current_theme = 'base'
        self.step()
        renpy.call("start_dungeon")

    def end(self):
        renpy.return_statement()

    def player_place_card(self, card):
        self.placed_card = card
        self.player_hands.remove(card)

    def player_return_card(self):
        self.player_hands.append(self.placed_card)
        self.placed_card = None

    def step(self):
        if self.placed_card is not None:
            if isinstance(self.placed_card.addition, NPC):
                card = self.placed_card
                self.placed_card = None
                npc_controller.talk_to_npc(card.addition)
                return
            elif isinstance(self.placed_card.addition, DungeonArea):
                self.current_area = self.placed_card.addition
                self.current_floor = self.placed_card.number
                if self.current_area.is_theme_entry:
                    self.current_theme = self.current_area.theme
                elif self.current_area.is_theme_exit:
                    self.current_theme = 'base'
                    self.current_floor = 2
        self.placed_card = None
        self.player_hands.clear()
        self.player_hands.append(Card(14, "Hearts", "empty", "离开", "回家了", None))
        for i in range(3):
            if self.current_theme == 'base':
                if random.randint(0, 10) < 3:
                    area = random.choice(list(self.available_area.values()))[0]  # area entry
                else:
                    area = random.choice(self.available_area['base'])
            else:
                if random.randint(0, 10) < 1:
                    area = self.available_area[self.current_theme][-1]  # area exit
                else:
                    area = random.choice(self.available_area[self.current_theme][1:-1])
            self.player_hands.append(
                Card(self.current_floor + (
                    random.choice([0, 0, 0, 1]) if self.current_theme != 'base' and self.current_floor < 14 else 0),
                     "Clovers",
                     area.name, area.title,
                     "前往" + area.title, area))
        npc_list = npc_controller.get_area_npc_list(f'dungeon_{self.current_theme}_{self.current_floor}')
        for npc in npc_list:
            self.player_hands.append(npc.card())
        enemy_count = random.choice([0, 0, 0, 0, 1, 1, 1, 2, 2, 3])
        enemy_list = self.gen_enemy_list(enemy_count)
        for enemy in enemy_list:
            self.player_hands.append(enemy.card())

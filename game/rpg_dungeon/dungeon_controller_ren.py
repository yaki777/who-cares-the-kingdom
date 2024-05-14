import random

from rpg_cards.cards_ren import Card
from rpg_dungeon.dungeon_area_ren import DungeonArea, DUNGEON_AREAS
from rpg_npc.npc_ren import NPC
from rpg_role.roles_ren import *
from rpg_system.renpy_constant import renpy, battle_controller, cards_controller

"""renpy
init -50 python:
"""


class DungeonController:
    def __init__(self):
        self.available_roles = [
            ROLE_SLAVE,
            ROLE_CLERGY,
            ROLE_MONK,
            ROLE_THIEF,
            ROLE_HUNTER,
            ROLE_ADVENTURER,
            ROLE_BARD,
            ROLE_FARMER,
            ROLE_MERCHANT,
            ROLE_ALCHEMIST,
            ROLE_SCHOLAR,
            ROLE_MAGE,
            ROLE_SOLDIER,
            ROLE_KNIGHT,
            ROLE_PRINCE
        ]
        self.available_area = DUNGEON_AREAS
        self.current_area = self.available_area[0]
        self.dungeon_level = 1
        self.current_floor = 1
        self.current_enemy_list = []
        self.player_hands = []
        self.placed_card = None

    def create_enemy_list(self):
        enemy_count = random.choice([0, 1, 2])
        max_level = self.dungeon_level + self.current_floor
        role_list = [role for role in self.available_roles if role.level_range[0] <= max_level]
        enemy_list = []
        for i in range(enemy_count):
            enemy_role = random.choice(role_list)
            enemy_level = random.randint(enemy_role.level_range[0], enemy_role.level_range[1])
            enemy_list.append(NPC('enemy_test', "敌人", enemy_role, enemy_level, [], True))
        return enemy_list

    def start(self, dungeon_level):
        self.player_hands = []
        self.dungeon_level = dungeon_level
        self.current_floor = 1

    def player_place_card(self, card):
        self.placed_card = card
        self.player_hands.remove(card)

    def step(self):
        if self.placed_card is not None:
            if isinstance(self.placed_card.addition, NPC):
                card = self.placed_card
                self.placed_card = None
                battle_controller.start(card.addition)
                renpy.call("start_battle", "start_dungeon")
                return
            elif isinstance(self.placed_card.addition, DungeonArea):
                self.current_area = self.placed_card.addition
                self.current_floor = self.placed_card.number
        self.placed_card = None
        self.player_hands.clear()
        self.player_hands.append(Card(14, "Hearts", "empty", "离开", "回家了", None))
        area_card_size = random.randint(1, 3)
        for i in range(area_card_size):
            area = random.choice(self.available_area)
            self.player_hands.append(
                Card(self.current_floor + 1, "Clovers", area.name, area.title, "前往" + area.title, area))
        enemy_list = self.create_enemy_list()
        for enemy in enemy_list:
            self.player_hands.append(enemy.card())

    def settle_battle_result(self, battle_result):
        enemy = battle_result[0]
        player_rank = battle_result[1]
        if player_rank >= enemy.hp:
            return cards_controller.enemy_draw_cards(enemy.id, 3)

    def player_choose_reward(self, card):
        cards_controller.player_get_card(card)

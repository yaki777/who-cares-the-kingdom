import random

from rpg_battle.battle_actions_ren import TAGS
from rpg_cards.cards_ren import CARD_LIBRARY
from rpg_npc.npc_ren import NPC, NPC_MALE_NAMES
from rpg_role.roles_ren import *
from rpg_system.renpy_constant import cards_controller, world_controller

"""renpy
init -50 python:
"""


class NPCController:
    def __init__(self):
        self.npc_list = {}
        self.area_npc_map = {}

    def get_npc(self, npc_id):
        return self.npc_list[npc_id]

    def gen_npc(self, role):
        weakness = random.sample(TAGS, random.randint(1, 3))
        (npc_id, name, _) = NPC_MALE_NAMES.pop(0)
        npc = NPC(npc_id, name, role,
                  random.randint(role.level_range[0], role.level_range[1]), weakness)
        # todo? different card pool for different role
        deck = random.sample(CARD_LIBRARY, 20)
        cards_controller.enemy_register_cards(npc_id, deck)
        self.npc_list[npc_id] = npc

    def gen_world_npc(self):
        npc_mapping = [
            (ROLE_KING, 2),
            (ROLE_QUEEN, 2),
            (ROLE_PRINCE, 4),
            (ROLE_PRINCESS, 4),
            (ROLE_MINISTER, 8),
            (ROLE_ENVOY, 2),
            (ROLE_KNIGHT, 4),
            (ROLE_SOLDIER, 16),
            (ROLE_MAGE, 4),
            (ROLE_SCHOLAR, 4),
            (ROLE_ALCHEMIST, 4),
            (ROLE_DIVINER, 2),
            (ROLE_MERCHANT, 4),
            (ROLE_CRAFTSMAN, 4),
            (ROLE_FARMER, 16),
            (ROLE_ARTIST, 4),
            (ROLE_BARD, 4),
            (ROLE_ADVENTURER, 6),
            (ROLE_HUNTER, 4),
            (ROLE_THIEF, 4),
            (ROLE_PRIEST, 4),
            (ROLE_MONK, 4),
            (ROLE_NUN, 4),
            (ROLE_CLERGY, 1),
            (ROLE_SLAVE, 4),
            (ROLE_PROSTITUTE, 4)
        ]
        for (role, count) in npc_mapping:
            for i in range(count):
                self.gen_npc(role)

    def gen_dungeon_npc(self, count):
        npc_list = []
        npc_mapping = [ROLE_ADVENTURER, ROLE_THIEF, ROLE_SOLDIER, ROLE_MAGE, ROLE_HUNTER, ROLE_PRIEST, ROLE_MONK,
                       ROLE_SLAVE]
        for i in range(count):
            npc_list.append(self.gen_npc(random.choice(npc_mapping)))
        return npc_list

    def update_npc_location(self):
        self.area_npc_map.clear()
        for npc in self.npc_list.values():
            area_weights = npc.role.area_weights_day if 8 < world_controller.get_time() < 18 else npc.role.area_weights_night
            npc.location = random.choices(list(area_weights.keys()), weights=list(area_weights.values()))[0]
            if npc.location not in self.area_npc_map:
                self.area_npc_map[npc.location] = []
            self.area_npc_map[npc.location].append(npc)

    def get_area_npc_list(self, area_code):
        return self.area_npc_map.get(area_code, [])

    def talk_to_npc(self, npc_id):
        pass

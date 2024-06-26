import random

from rpg_battle.battle_action_library_ren import THEME_LOVE_LIBRARY, THEME_YURI_LIBRARY
from rpg_battle.battle_action_machine_ren import MACHINE_ACTION_LIBRARY
from rpg_battle.battle_actions_ren import TAGS, BattleAction, THEME_YURI
from rpg_cards.cards_ren import CARD_SUITS
from rpg_npc.npc_ren import NPC, NPC_MALE_NAMES, NPC_FEMALE_NAMES
from rpg_role.roles_ren import *
from rpg_system.renpy_constant import world_controller, battle_action_controller, renpy, dungeon_controller
from rpg_world.player_ren import player

"""renpy
init -50 python:
"""
from datetime import timedelta


class NPCController:
    def __init__(self):
        self.npc_list = {}
        self.area_npc_map = {}
        self.frozen_placed_npc_list = []

    def get_npc(self, npc_id):
        return self.npc_list[npc_id]

    def get_npc_by_role(self, role):
        return [npc for npc in self.npc_list.values() if npc.role.code == role.code]

    def add_npc_to_stage(self, npc_id, stage_name, intro_text):
        self.npc_list[npc_id].stages.append((intro_text, stage_name))

    def remove_npc_stages(self, npc_id, stage_name):
        self.npc_list[npc_id].stages = list(filter(lambda x: stage_name not in x[1], self.npc_list[npc_id].stages))

    def gen_npc(self, role):
        weakness = random.sample(TAGS, random.randint(1, 3))
        is_female = False
        if role == ROLE_QUEEN or role == ROLE_PRINCESS or role == ROLE_PROSTITUTE:
            npc_names = NPC_FEMALE_NAMES
            is_female = True
        elif role == ROLE_ENVOY or role == ROLE_PRINCE or role == ROLE_KING or role == ROLE_ALCHEMIST:
            npc_names = NPC_MALE_NAMES
        else:
            if random.randint(0, 10) < 3:
                is_female = True
                npc_names = NPC_FEMALE_NAMES
            else:
                npc_names = NPC_MALE_NAMES
        (npc_id, name, _) = npc_names.pop(0)
        npc = NPC(npc_id, name, role,
                  random.randint(role.level_range[0], role.level_range[1]), weakness, False, is_female)
        deck = []
        if is_female:
            actions = random.sample(THEME_YURI_LIBRARY, min(20, len(THEME_YURI_LIBRARY)))
        else:
            actions = random.sample(THEME_LOVE_LIBRARY, min(20, len(THEME_LOVE_LIBRARY)))
        if role == ROLE_ALCHEMIST:
            actions += MACHINE_ACTION_LIBRARY
        if npc.level > 7:
            suits = CARD_SUITS[0:-1]
        elif npc.level > 11:
            suits = CARD_SUITS[0:-2]
        else:
            suits = CARD_SUITS
        for action in actions:
            deck.append(BattleAction(*action, level=random.randint(npc.level, 14), suit=random.choice(suits)))
        battle_action_controller.enemy_register_actions(npc_id, deck)
        return npc

    def gen_world_npc(self):
        npc_mapping = [
            (ROLE_KING, 1),
            (ROLE_QUEEN, 1),
            (ROLE_PRINCE, 2),
            (ROLE_PRINCESS, 1),
            (ROLE_MINISTER, 2),
            (ROLE_ENVOY, 1),
            (ROLE_KNIGHT, 2),
            (ROLE_SOLDIER, 4),
            (ROLE_MAGE, 2),
            (ROLE_SCHOLAR, 1),
            (ROLE_ALCHEMIST, 1),
            (ROLE_DIVINER, 1),
            (ROLE_MERCHANT, 4),
            (ROLE_CRAFTSMAN, 4),
            (ROLE_FARMER, 4),
            (ROLE_ARTIST, 4),
            (ROLE_BARD, 1),
            (ROLE_ADVENTURER, 4),
            (ROLE_HUNTER, 4),
            (ROLE_THIEF, 4),
            (ROLE_PRIEST, 4),
            (ROLE_MONK, 4),
            (ROLE_NUN, 4),
            (ROLE_CLERGY, 1),
            (ROLE_SLAVE, 2),
            (ROLE_PROSTITUTE, 2)
        ]
        for (role, count) in npc_mapping:
            if player.role == role:
                count -= 1
            for i in range(count):
                npc = self.gen_npc(role)
                self.npc_list[npc.id] = npc

    def place_npc(self, npc_id, area_code, frozen_hours=0):
        npc = self.npc_list[npc_id]
        npc.location = area_code
        for _, npc_list in self.area_npc_map.items():
            if npc in npc_list:
                npc_list.remove(npc)
        if area_code not in self.area_npc_map:
            self.area_npc_map[area_code] = []
        self.area_npc_map[area_code].append(npc)
        if frozen_hours > 0:
            unfreeze_date = world_controller.date + timedelta(hours=frozen_hours)
            self.frozen_placed_npc_list.append((npc_id, unfreeze_date))
        world_controller.step()

    def update_npc_location(self):
        freeze_npc_list = []
        unfreeze_list = []
        for npc_id, unfreeze_date in self.frozen_placed_npc_list:
            if world_controller.date >= unfreeze_date:
                unfreeze_list.append(npc_id)
            else:
                freeze_npc_list.append(npc_id)
        self.frozen_placed_npc_list = [(npc_id, unfreeze_date) for npc_id, unfreeze_date in self.frozen_placed_npc_list
                                       if npc_id not in unfreeze_list]
        self.area_npc_map.clear()
        for npc in self.npc_list.values():
            area_weights = npc.role.area_weights_day if 8 < world_controller.get_hour() < 18 else npc.role.area_weights_night
            if npc.id not in freeze_npc_list:
                npc.location = random.choices(list(area_weights.keys()), weights=list(area_weights.values()))[0]
            if npc.location not in self.area_npc_map:
                self.area_npc_map[npc.location] = []
            # 限制每个地区的最大npc数量
            if len(self.area_npc_map[npc.location]) < 5:
                self.area_npc_map[npc.location].append(npc)

    def get_area_npc_list(self, area_code):
        return self.area_npc_map.get(area_code, [])

    def talk_to_npc(self, npc):
        if 'dungeon_' in npc.location:
            background = dungeon_controller.current_area.background
        else:
            background = world_controller.current_area.background
        if len(npc.stages) > 0:
            renpy.call("npc_talk", background, npc)
            return

        npc_role_code = npc.role.code
        player_role_code = player.role.code
        base_label = npc_role_code
        next_label = f"{base_label}_{player_role_code}_{npc.location}"
        if not renpy.has_label(next_label):
            next_label = f"{base_label}_{player_role_code}"
        if not renpy.has_label(next_label):
            next_label = f"{base_label}_{npc.location}"
        if not renpy.has_label(next_label):
            next_label = f"{base_label}"
        if not renpy.has_label(next_label):
            next_label = "fallback"
        renpy.call("npc_talk", background, npc, next_label)

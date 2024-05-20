import random

from rpg_role.roles_ren import ROLE_MINISTER, ROLE_ENVOY, ROLE_PRINCESS, ROLE_KNIGHT, ROLE_SOLDIER, ROLE_ALCHEMIST, \
    ROLE_ADVENTURER
from rpg_story.story_ren import Story
from rpg_system.renpy_constant import npc_controller, world_controller
from rpg_world.area_ren import AREA_MAP

"""renpy
init -90 python:
"""


class StoryQueenSaveKingdom(Story):
    def __init__(self):
        super().__init__()
        self.minister = None
        self.name = "M_QSK"
        self.current_stage = "stage_1"
        self.init_stage = "stage_1"

    def stage_1(self):
        self.minister = npc_controller.get_npc_by_role(ROLE_MINISTER)[0]
        npc_controller.place_npc(self.minister.id, "kbr1", 12)
        world_controller.place_player("kbr1")
        npc_controller.add_npc_to_stage(self.minister.id, "M_QSK_stage_1", "关于我们的国家...")

    def stage_2(self):
        npc_controller.remove_npc_stages(self.minister.id, "M_QSK_")
        npc_controller.add_npc_to_stage(self.minister.id, "M_QSK_stage_2", "关于我们的国家...")


class StoryQueenDaughterWedding(Story):
    def __init__(self):
        super().__init__()
        self.princess = None
        self.minister = None
        self.envoy = None
        self.princess_agree = None
        self.name = "M_QDW"
        self.current_stage = "stage_1"

    def stage_1(self):
        self.minister = npc_controller.get_npc_by_role(ROLE_MINISTER)[0]
        self.envoy = npc_controller.get_npc_by_role(ROLE_ENVOY)[0]
        npc_controller.add_npc_to_stage(self.envoy.id, "M_QDW_stage_1", "关于支援我们的国家...")
        npc_controller.place_npc(self.envoy.id, "pbh1", 12)

    def stage_2(self):
        npc_controller.remove_npc_stages(self.envoy.id, "M_QDW_")
        npc_controller.add_npc_to_stage(self.envoy.id, "M_QDW_stage_2", "关于公主的婚事...")
        self.minister = npc_controller.get_npc_by_role(ROLE_MINISTER)[0]
        npc_controller.add_npc_to_stage(self.minister.id, "M_QDW_stage_2", "关于公主的婚事...")
        self.princess = npc_controller.get_npc_by_role(ROLE_PRINCESS)[0]
        npc_controller.add_npc_to_stage(self.princess.id, "M_QDW_stage_2", "关于你的婚事...")

    def stage_10(self):
        npc_controller.remove_npc_stages(self.envoy.id, "M_QDW_")
        npc_controller.remove_npc_stages(self.minister.id, "M_QDW_")
        npc_controller.add_npc_to_stage(self.minister.id, "M_QDW_stage_10", "关于我们的国家...")
        npc_controller.add_npc_to_stage(self.envoy.id, "M_QDW_stage_10", "关于支援我们的国家...")


class StoryQueenFindDaughter(Story):
    def __init__(self):
        super().__init__()
        self.the_adventurer = None
        self.adventurers = None
        self.alchemist = None
        self.find_start_date = None
        self.soldiers = None
        self.knights = None
        self.ministers = None
        self.princess = None
        self.name = "M_QFD"
        self.current_stage = "stage_1"

    def stage_1(self):
        self.princess = npc_controller.get_npc_by_role(ROLE_PRINCESS)[0]
        npc_controller.place_npc(self.princess.id, "dungeon_7", 24 * 15)
        self.ministers = npc_controller.get_npc_by_role(ROLE_MINISTER)
        for minister in self.ministers:
            npc_controller.add_npc_to_stage(minister.id, "M_QFD_stage_1", "看到我的女儿了吗...")
        self.knights = npc_controller.get_npc_by_role(ROLE_KNIGHT)
        for knight in self.knights:
            npc_controller.add_npc_to_stage(knight.id, "M_QFD_stage_1", "看到我的女儿了吗...")
        self.soldiers = npc_controller.get_npc_by_role(ROLE_SOLDIER)
        for soldier in self.soldiers:
            npc_controller.add_npc_to_stage(soldier.id, "M_QFD_stage_1", "看到我的女儿了吗...")

    def stage_2(self):
        self.find_start_date = world_controller.date.timestamp()
        for knight in self.knights:
            npc_controller.remove_npc_stages(knight.id, "M_QFD_")
            npc_controller.add_npc_to_stage(knight.id, "M_QFD_stage_2", "看到我的女儿了吗...")
        self.adventurers = npc_controller.get_npc_by_role(ROLE_ADVENTURER)
        for adventurer in self.adventurers:
            npc_controller.add_npc_to_stage(adventurer.id, "M_QFD_stage_2", "看到我的女儿了吗...")

    def stage_3(self, the_adventurer):
        for adventurer in self.adventurers:
            npc_controller.remove_npc_stages(adventurer.id, "M_QFD_")
        self.the_adventurer = the_adventurer
        npc_controller.add_npc_to_stage(the_adventurer.id, "M_QFD_stage_3", "我准备好了...")
        npc_controller.place_npc(the_adventurer.id, "g1", 24 * 3)

    def stage_5(self):
        for soldier in self.soldiers:
            npc_controller.remove_npc_stages(soldier.id, "M_QFD_")
        for knight in self.knights:
            npc_controller.remove_npc_stages(knight.id, "M_QFD_")
        for minister in self.ministers:
            npc_controller.remove_npc_stages(minister.id, "M_QFD_")
        npc_controller.place_npc(self.princess.id, "psr1", 30 * 24)
        npc_controller.remove_npc_stages(self.princess.id, "M_QFD_")
        npc_controller.add_npc_to_stage(self.princess.id, "M_QFD_stage_3", "女儿...")
        self.alchemist = npc_controller.get_npc_by_role(ROLE_ALCHEMIST)[0]
        npc_controller.add_npc_to_stage(self.alchemist.id, "M_QFD_stage_3", "迷宫中的怪物...")

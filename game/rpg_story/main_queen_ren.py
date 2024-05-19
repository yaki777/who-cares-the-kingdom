import random

from rpg_role.roles_ren import ROLE_MINISTER, ROLE_ENVOY
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
        npc_controller.remove_npc_from_stage(self.minister.id, "M_QSK_stage_1")
        npc_controller.add_npc_to_stage(self.minister.id, "M_QSK_stage_2", "关于我们的国家...")


class StoryHumbleQueen(Story):
    def __init__(self):
        super().__init__()
        self.minister = None
        self.envoy = None
        self.name = "M_HQ"
        self.current_stage = "stage_1"

    def stage_1(self):
        self.envoy = npc_controller.get_npc_by_role(ROLE_ENVOY)[0]
        npc_controller.add_npc_to_stage(self.envoy.id, f"M_HQ_stage_1", "关于支援我们的国家...")
        npc_controller.place_npc(self.envoy.id, "pbh1", 12)

    def stage_2(self):
        npc_controller.remove_npc_from_stage(self.envoy.id, "M_HQ_stage_1")
        npc_controller.add_npc_to_stage(self.envoy.id, f"M_HQ_stage_2", "关于公主的婚事...")
        self.minister = npc_controller.get_npc_by_role(ROLE_MINISTER)[0]
        npc_controller.add_npc_to_stage(self.minister.id, f"M_HQ_stage_2", "关于公主的婚事...")

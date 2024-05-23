import random

from rpg_role.dungeon_roles_ren import DUNGEON_ROLE_GOBLIN, DUNGEON_ROLE_GOBLIN_DOC
from rpg_story.story_ren import Story
from rpg_system.renpy_constant import dungeon_controller, npc_controller

"""renpy
init -90 python:
"""


class StoryGoblinSlave(Story):
    def __init__(self):
        super().__init__()
        self.name = "S_GS"
        self.current_stage = "stage_1"

    def stage_1(self):
        enemy = random.choice(dungeon_controller.gen_enemy_list(3, [DUNGEON_ROLE_GOBLIN, DUNGEON_ROLE_GOBLIN_DOC]))
        enemy.stages.append(("放我走...", "S_GS_stage_1"))
        npc_controller.talk_to_npc(enemy)

    def stage_2(self):
        enemy = random.choice(dungeon_controller.gen_enemy_list(3, [DUNGEON_ROLE_GOBLIN, DUNGEON_ROLE_GOBLIN_DOC]))
        enemy.stages.append(("放我走...", "S_GS_stage_2"))
        npc_controller.talk_to_npc(enemy)

import random

from rpg_battle.battle_action_library_ren import THEME_LOVE_LIBRARY, THEME_GOBLIN_LIBRARY, THEME_MACHINE_LIBRARY, \
    THEME_SELF_LIBRARY
from rpg_battle.battle_actions_ren import TAG_SEX, TAG_SERVANT
"""renpy
init -90 python:
"""

class Perk:
    def name(self):
        return ""

    def description(self):
        return ""

    def init_actions(self):
        return []


class PerkMasturbationLover(Perk):
    def name(self):
        return "自慰爱好者"

    def description(self):
        return "为你的初始卡组添加最多5张自慰主题卡。"

    def init_actions(self):
        action_library = THEME_SELF_LIBRARY
        if len(action_library) == 0:
            return []
        return random.sample(action_library, min(5, len(action_library)))


class PerkSexLover(Perk):
    def name(self):
        return "性爱爱好者"

    def description(self):
        return "为你的初始卡组添加最多5张性爱主题卡。如果禁用了阴道内容，将不会生效"

    def init_actions(self):
        action_library = list(filter(lambda x: '_anal' not in x[0] and TAG_SEX in x[1], THEME_LOVE_LIBRARY))
        if len(action_library) == 0:
            return []
        return random.sample(action_library, min(5, len(action_library)))


class PerkAnalLover(Perk):
    def name(self):
        return "肛交爱好者"

    def description(self):
        return "为你的初始卡组添加最多5张肛交主题卡。如果禁用了肛门内容，将不会生效"

    def init_actions(self):
        action_library = list(filter(lambda x: '_anal' in x[0] and TAG_SEX in x[1], THEME_LOVE_LIBRARY))
        if len(action_library) == 0:
            return []
        return random.sample(action_library, min(5, len(action_library)))


class PerkServantLover(Perk):
    def name(self):
        return "侍奉爱好者"

    def description(self):
        return "为你的初始卡组增加最多5张侍奉主题卡。包括：口交、手交、足交、乳交等"

    def init_actions(self):
        action_library = list(filter(lambda x: TAG_SERVANT in x[1], THEME_LOVE_LIBRARY))
        if len(action_library) == 0:
            return []
        return random.sample(action_library, min(5, len(action_library)))


class PerkGoblinLover(Perk):
    def name(self):
        return "哥布林爱好者"

    def description(self):
        return "为你的初始卡组增加最多5张哥布林主题卡。"

    def init_actions(self):
        action_library = THEME_GOBLIN_LIBRARY
        if len(action_library) == 0:
            return []
        return random.sample(action_library, min(5, len(action_library)))


class PerkMachineLover(Perk):
    def name(self):
        return "机械奸爱好者"

    def description(self):
        return "为你的初始卡组增加最多5张机械奸主题卡。"

    def init_actions(self):
        action_library = THEME_MACHINE_LIBRARY
        if len(action_library) == 0:
            return []
        return random.sample(action_library, min(5, len(action_library)))


PERK_LIBRARY = [
    PerkSexLover(),
    PerkAnalLover(),
    PerkServantLover(),
    PerkGoblinLover(),
    PerkMachineLover(),
]

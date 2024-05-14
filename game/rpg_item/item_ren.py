from rpg_human.human_organ_ren import Organs
from rpg_system.base_ren import GradeColor
"""renpy
init -90 python:
"""

class Item(object):
    def __init__(self, name="", detail="", grade="LV0", organs=[]):
        self.name = name
        self.detail = detail
        self.grade = grade
        self.organs = organs

    def get_name(self):
        return "{color=%s}%s{/color}" % (getattr(GradeColor, self.grade), self.name)

    def get_description(self):
        return self.detail

    def lock_organ(self):
        return False

    def player_interactive(self):
        return False

    def on_action(self, action):
        return

    def reality(self):
        return self.name


class Toy(Item):
    type_name = ""
    type_detail = ""
    type_organs = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = self.type_name
        self.detail = self.type_detail
        self.organs = self.type_organs


class ButtPlugL(Toy):
    type_name = "L号肛塞"
    type_detail = "L号的，用于刺激肛门和直肠的玩具。通常是圆锥形的，具有突出部分，以便在肛门里保持稳定。"
    type_organs = [Organs.ANUS]


class ButtPlugM(Toy):
    type_name = "M号肛塞"
    type_detail = "M号的，用于刺激肛门和直肠的玩具。通常是圆锥形的，具有突出部分，以便在肛门里保持稳定。"
    type_organs = [Organs.ANUS]


class ButtPlugS(Toy):
    type_name = "S号肛塞"
    type_detail = "S号的，用于刺激肛门和直肠的玩具。通常是圆锥形的，具有突出部分，以便在肛门里保持稳定。"
    type_organs = [Organs.ANUS]


class LockButtPlug(Toy):
    type_name = "带锁的肛塞"
    type_detail = "结构复杂的肛塞，底部有一个小的锁定装置，可以用特殊的钥匙打开。一旦插入，只有拥有钥匙的人才能将其拔出。"
    type_organs = [Organs.ANUS]

    def lock_organ(self):
        return True


class AnalBeadsL(Toy):
    type_name = "L号拉珠"
    type_detail = "L号的，用于刺激肛门和直肠的玩具。由多个球型珠子串成"
    type_organs = [Organs.ANUS]


class AnalBeadsM(Toy):
    type_name = "M号拉珠"
    type_detail = "M号的，用于刺激肛门和直肠的玩具。由多个球型珠子串成"
    type_organs = [Organs.ANUS]


class AnalBeadsS(Toy):
    type_name = "S号拉珠"
    type_detail = "S号的，用于刺激肛门和直肠的玩具。由多个球型珠子串成"
    type_organs = [Organs.ANUS]


class EnemaKit(Toy):
    type_name = "灌肠用具"
    type_detail = "用于清洗肛门和肠道的工具"
    type_organs = [Organs.ANUS]


class DildoL(Toy):
    type_name = "L号假阳具"
    type_detail = "L号的，模仿男性阴茎的硅胶玩具"
    type_organs = [Organs.VAGINA, Organs.ANUS]


class DildoM(Toy):
    type_name = "M号假阳具"
    type_detail = "M号的，模仿男性阴茎的硅胶玩具"
    type_organs = [Organs.VAGINA, Organs.ANUS]


class DildoS(Toy):
    type_name = "S号假阳具"
    type_detail = "S号的，模仿男性阴茎的硅胶玩具"
    type_organs = [Organs.VAGINA, Organs.ANUS]


class Vibrator(Toy):
    type_name = "跳蛋"
    type_detail = "可以振动的小玩具"
    type_organs = [Organs.CHEST, Organs.PENIS, Organs.URETHRA, Organs.VAGINA, Organs.CLITORIS, Organs.LABIA,
                   Organs.TESTICLE, Organs.ANUS]


class Clamp(Toy):
    type_name = "夹子"
    type_detail = "常常用于夹在乳头上,也可以用在别的地方"
    type_organs = [Organs.CHEST, Organs.PENIS, Organs.LABIA, Organs.CLITORIS, Organs.TESTICLE]


class Gag(Toy):
    type_name = "口球"
    type_detail = "堵住嘴巴，不能说话"
    type_organs = [Organs.MOUTH]


class Rope(Toy):
    type_name = "绳子"
    type_detail = "捆绑各个部位"
    type_organs = [Organs.ARM, Organs.HAND, Organs.LEG, Organs.FOOT]


class Handcuffs(Toy):
    type_name = "手铐"
    type_detail = "就像它的名字一样，有些也能用来铐脚"
    type_organs = [Organs.HAND, Organs.FOOT]


Toys = [
    ButtPlugL,
    ButtPlugM,
    ButtPlugS,
    LockButtPlug,
    AnalBeadsL,
    AnalBeadsM,
    AnalBeadsS,
    EnemaKit,
    DildoL,
    DildoM,
    DildoS,
    Vibrator,
    Clamp,
    Gag,
    Rope,
    Handcuffs
]



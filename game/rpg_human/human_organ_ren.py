"""renpy
init -100 python:
"""
from enum import Enum
import math


class HumanColor(Enum):
    PURPLE = ("紫色", "purple")
    RED = ("红色", "red")
    GREEN = ("绿色", "green")


class CharacterStyle(Enum):
    SOFT = ("柔弱的", 0)
    CUTE = ("可爱的", 1)
    SEXY = ("性感的", 2)
    COLD = ("冷酷的", 3)
    SHARP = ("锋利的", 4)


class BodyStyle(Enum):
    SLIM = ("瘦小的", 0)
    DELICATE = ("纤细的", 1)
    AVERAGE = ("普通的", 2)
    STRONG = ("健壮的", 3)
    PLUMP = ("丰满的", 4)


class Organs:
    HAIR = "Hair"
    EYE = "Eye"
    NOSE = "Nose"
    CHEEK = "Cheek"
    EAR = "Ear"
    MOUTH = "Mouth"
    NECK = "Neck"
    ARM = "Arm"
    HAND = "Hand"
    CHEST = "Chest"
    ABDOMEN = "Abdomen"
    ASS = "Ass"
    LEG = "Leg"
    FOOT = "Foot"
    VAGINA = "Vagina"
    CLITORIS = "Clitoris"
    LABIA = "Labia"
    URETHRA = "Urethra"
    PENIS = "Penis"
    TESTICLE = "Testicle"
    ANUS = "Anus"


class Organ(object):
    def __init__(self, experience=0, health_max=100, bound=[]):
        self.experience = experience
        self.health_max = health_max
        self.health = health_max
        self.bound = bound
        self.belong = None

    def locked(self):
        for item in self.bound:
            if item.lock_organ():
                return True
        return False

    def able(self):
        return self.health > 0

    def level(self):
        if self.experience == 0:
            return 1
        level = int(math.log2(self.experience))
        if level < 1:
            level = 1
        return level

    def image_attribute(self):
        return ''

    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        return self is other


class SexualOrgan(Organ):
    def __init__(self, experience=0, health_max=100, bound=[]):
        super().__init__(experience, health_max, bound)
        self.sensitivity = 0


# 头发
class HairStyle(Enum):
    SHORT = ("短发", "short")  # 短发
    MEDIUM = ("中长发", "medium")  # 中长发
    LONG = ("长发", "long")  # 长发


class Hair(Organ):

    def __init__(self, style=HairStyle.SHORT, color=HumanColor.GREEN, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if style not in HairStyle:
            raise ValueError(f"Invalid hairstyle '{style}'")
        if color not in HumanColor:
            raise ValueError(f"Invalid haircolor '{color}'")
        self.style = style
        self.color = color
        self.name = "头发"
        self.type = Organs.HAIR
        self.order = 0

    @staticmethod
    def all_names():
        names = []
        for style in HairStyle:
            for color in HumanColor:
                names.append(color.value[0] + style.value[0])
        return names

    def type_name(self):
        return self.color.value[0] + self.style.value[0]

    def image_attribute(self):
        return f"{self.style.value[1]}_{self.color.value[1]}"


class Eye(Organ):

    def __init__(self, left_or_right, style=CharacterStyle.SOFT, color=HumanColor.GREEN, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if style not in CharacterStyle:
            raise ValueError(f"Invalid eye style '{style}'.")
        if color not in HumanColor:
            raise ValueError(f"Invalid haircolor '{color}'")
        self.style = style
        self.color = color
        if left_or_right == 'left':
            self.name = "左眼"
        else:
            self.name = "右眼"
        self.type = Organs.EYE
        self.order = 1

    @staticmethod
    def all_names():
        names = []
        for style in CharacterStyle:
            for color in HumanColor:
                names.append(style.value[0] + color.value[0] + '眼睛')
        return names

    def type_name(self):
        return self.style.value[0] + self.color.value[0] + '眼睛'

    def image_attribute(self):
        return f"{self.color.value[1]}"


class Nose(Organ):
    inject_size = 1

    def __init__(self, style=CharacterStyle.SOFT, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if style not in CharacterStyle:
            raise ValueError(f"Invalid eye style '{style}'.")
        self.style = style
        self.name = "鼻子"
        self.type = Organs.NOSE
        self.order = 2

    @staticmethod
    def all_names():
        names = []
        for style in CharacterStyle:
            names.append(style.value[0] + '鼻子')
        return names

    def type_name(self):
        return self.style.value[0] + '鼻子'


# 脸颊
class Cheek(Organ):

    def __init__(self, left_or_right, style=CharacterStyle.SOFT, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if style not in CharacterStyle:
            raise ValueError(f"Invalid shape: {style}.")

        self.style = style
        if left_or_right == 'left':
            self.name = "左脸颊"
        else:
            self.name = "右脸颊"
        self.type = Organs.CHEEK
        self.order = 3

    @staticmethod
    def all_names():
        names = []
        for style in CharacterStyle:
            names.append(style.value[0] + '脸颊')
        return names

    def type_name(self):
        return self.style.value[0] + '脸颊'


# 耳朵
class EarStyle(Enum):
    HUMAN = "人类耳朵"
    ELF = "精灵耳朵"


class Ear(Organ):

    def __init__(self, left_or_right, style=EarStyle.HUMAN, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if style not in EarStyle:
            raise ValueError(f"Invalid shape: {style}.")
        self.style = style
        if left_or_right == 'left':
            self.name = "左耳"
        else:
            self.name = "右耳"
        self.type = Organs.EAR
        self.order = 4

    @staticmethod
    def all_names():
        names = []
        for style in EarStyle:
            names.append(style.value)
        return names

    def type_name(self):
        return self.style.value[0]


# 嘴
class Mouth(SexualOrgan):

    def __init__(self, style=CharacterStyle.SOFT, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if style not in CharacterStyle:
            raise ValueError(f"Invalid shape: {style}.")
        self.style = style
        self.name = "嘴"
        self.type = Organs.MOUTH
        self.diameter = 5
        self.order = 5

    @staticmethod
    def all_names():
        names = []
        for style in CharacterStyle:
            names.append(style.value[0] + '嘴')
        return names

    def type_name(self):
        return self.style.value[0] + '嘴'


# 颈部
class Neck(Organ):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "脖子"
        self.type = Organs.NECK
        self.order = 6

    @staticmethod
    def all_names():
        return ['脖子']

    def type_name(self):
        return '脖子'


# 手
class Hand(Organ):

    def __init__(self, left_or_right, style=BodyStyle.SLIM, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if style not in BodyStyle:
            raise ValueError(f"Invalid style: {style}.")
        self.style = style

        if left_or_right == 'left':
            self.name = "左手"
        else:
            self.name = "右手"
        self.diameter = 7.5
        self.type = Organs.HAND
        self.order = 7

    @staticmethod
    def all_names():
        names = []
        for style in BodyStyle:
            names.append(style.value[0] + '手')
        return names

    def type_name(self):
        return self.style.value[0] + '手'


# 手臂
class Arm(Organ):
    def __init__(self, left_or_right, style=BodyStyle.SLIM, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if style not in BodyStyle:
            raise ValueError(f"Invalid style: {style}.")
        self.style = style
        if left_or_right == 'left':
            self.name = "左臂"
        else:
            self.name = "右臂"
        self.type = Organs.ARM
        self.order = 8

    @staticmethod
    def all_names():
        names = []
        for style in BodyStyle:
            names.append(style.value[0] + '手臂')
        return names

    def type_name(self):
        return self.style.value[0] + '手臂'


# 胸部
class ChestStyle(Enum):
    ROUND = "圆形"
    SIDE_SET = "分开型"
    TEARDROP = "泪滴型"
    ATHLETIC = "运动型"


class CupSize(Enum):
    AA = ('AA', 0)
    A = ('A', 10)
    B = ('B', 20)
    C = ('C', 30)
    D = ('D', 40)
    DD = ('DD', 50)
    E = ('E', 60)
    F = ('F', 70)
    FF = ('FF', 80)
    G = ('G', 90)


class Chest(SexualOrgan):

    def __init__(self, left_or_right, style=ChestStyle.ROUND, cup_size=CupSize.AA, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if style not in ChestStyle:
            raise ValueError(f"Invalid chest style: {style}.")
        if cup_size not in CupSize:
            raise ValueError(f"Invalid cup size: {cup_size}.")
        self.style = style
        self.cup_size = cup_size
        if left_or_right == 'left':
            self.name = "左胸"
        else:
            self.name = "右胸"
        self.type = Organs.CHEST
        self.order = 9

    @staticmethod
    def all_names():
        names = []
        for style in ChestStyle:
            for size in CupSize:
                names.append(size.value[0] + '罩杯' + style.value[0] + '胸部')
        return names

    def type_name(self):
        return self.cup_size.value[0] + '罩杯' + self.style.value[0] + '胸部'


# 腹部
class Abdomen(Organ):

    def __init__(self, style=BodyStyle.SLIM, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if style not in BodyStyle:
            raise ValueError(f"Invalid style: {style}.")
        self.style = style
        self.name = "腹部"
        self.type = Organs.ABDOMEN
        self.order = 10

    @staticmethod
    def all_names():
        names = []
        for style in BodyStyle:
            names.append(style.value[0] + '腹部')
        return names

    def type_name(self):
        return self.style.value[0] + '腹部'


# 臀部
class Ass(SexualOrgan):
    def __init__(self, style=BodyStyle.SLIM, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if style not in BodyStyle:
            raise ValueError(f"Invalid style: {style}.")
        self.style = style
        self.name = "屁股"
        self.type = Organs.ASS
        self.order = 11

    @staticmethod
    def all_names():
        names = []
        for style in BodyStyle:
            names.append(style.value[0] + '屁股')
        return names

    def type_name(self):
        return self.style.value[0] + '屁股'


# 腿
class Leg(Organ):
    def __init__(self, left_or_right, style=BodyStyle.SLIM, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if style not in BodyStyle:
            raise ValueError(f"Invalid style: {style}.")
        self.style = style
        if left_or_right == 'left':
            self.name = "左腿"
        else:
            self.name = "右腿"
        self.type = Organs.LEG
        self.order = 12

    @staticmethod
    def all_names():
        names = []
        for style in BodyStyle:
            names.append(style.value[0] + '腿')
        return names

    def type_name(self):
        return self.style.value[0] + '腿'


# 脚
class Foot(Organ):
    def __init__(self, left_or_right, style=BodyStyle.SLIM, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if style not in BodyStyle:
            raise ValueError(f"Invalid style: {style}.")
        self.style = style
        if left_or_right == 'left':
            self.name = "左脚"
        else:
            self.name = "右脚"
        self.type = Organs.FOOT
        self.order = 13

    @staticmethod
    def all_names():
        names = []
        for style in BodyStyle:
            names.append(style.value[0] + '脚')
        return names

    def type_name(self):
        return self.style.value[0] + '脚'


class PluggableStyle(Enum):
    TIGHT = ("紧致的", 0)
    PETITE = ("小巧的", 1)
    SOFT = ("柔软的", 2)
    FLEXIBLE = ("灵活的", 3)
    STRONG = ("强健的", 4)
    LOOSE = ("松垮的", 5)


class SizeStyle(Enum):
    HUGE = ("巨大", 5, 'L号')
    LARGE = ("大号", 4, 'L号')
    MEDIUM = ("正常", 3, 'M号')
    SMALL = ("小巧", 2, 'S号')
    MINI = ("迷你", 1, 'S号')


class PubicHairStyle(Enum):
    HAIRY = ("多毛的", 0)
    SPARSE = ("稀疏的", 1)
    SMOOTH = ("光洁的", 2)


# 阴道
class Vagina(SexualOrgan):
    def __init__(self, style=PluggableStyle.TIGHT, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if style not in PluggableStyle:
            raise ValueError(f"Invalid vagina style '{style}'.")
        self.style = style
        self.name = "阴道"
        self.diameter = 3
        self.type = Organs.VAGINA
        self.order = 14

    @staticmethod
    def all_names():
        names = []
        for style in PluggableStyle:
            names.append(style.value[0] + '阴道')
        return names

    def type_name(self):
        return self.style.value[0] + '阴道'


# 阴蒂
class Clitoris(SexualOrgan):
    def __init__(self, style=SizeStyle.MINI, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if style not in SizeStyle:
            raise ValueError(f"Invalid clitoris style '{style}'.")
        self.style = style
        self.name = "阴蒂"
        self.type = Organs.CLITORIS
        self.order = 15

    @staticmethod
    def all_names():
        names = []
        for style in SizeStyle:
            names.append(style.value[0] + '阴蒂')
        return names

    def type_name(self):
        return self.style.value[0] + '阴蒂'


# 阴唇
class Labia(SexualOrgan):
    def __init__(self, style=SizeStyle.MINI, hair_style=PubicHairStyle.SMOOTH, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if style not in SizeStyle:
            raise ValueError(f"Invalid clitoris style '{style}'.")
        self.style = style
        if hair_style not in PubicHairStyle:
            raise ValueError(f"Invalid clitoris hair_style '{style}'.")
        self.hair_style = hair_style
        self.name = "阴唇"
        self.type = Organs.LABIA
        self.order = 16

    @staticmethod
    def all_names():
        names = []
        for style in SizeStyle:
            for hair_style in PubicHairStyle:
                names.append(hair_style.value[0] + style.value[0] + '阴唇')
        return names

    def type_name(self):
        return self.hair_style.value[0] + self.style.value[0] + '阴唇'


# 尿道
class Urethra(SexualOrgan):
    def __init__(self, style=PluggableStyle.TIGHT, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if style not in PluggableStyle:
            raise ValueError(f"Invalid urethra style '{style}'.")
        self.style = style
        self.name = "尿道"
        self.diameter = 0.5
        self.type = Organs.URETHRA
        self.order = 17

    @staticmethod
    def all_names():
        names = []
        for style in PluggableStyle:
            names.append(style.value[0] + '尿道')
        return names

    def type_name(self):
        return self.style.value[0] + '尿道'


# 阴茎
class Penis(SexualOrgan):
    def __init__(self, style=SizeStyle.MINI, hair_style=PubicHairStyle.SMOOTH, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if style not in SizeStyle:
            raise ValueError(f"Invalid penis style '{style}'.")
        self.style = style
        if hair_style not in PubicHairStyle:
            raise ValueError(f"Invalid penis hair_style '{style}'.")
        self.hair_style = hair_style
        self.name = "阴茎"
        self.diameter = 4
        self.type = Organs.PENIS
        self.order = 18

    @staticmethod
    def all_names():
        names = []
        for style in SizeStyle:
            for hair_style in PubicHairStyle:
                names.append(hair_style.value[0] + style.value[0] + '阴茎')
        return names

    def type_name(self):
        return self.hair_style.value[0] + self.style.value[0] + '阴茎'

    def show_name(self):
        return f"{self.style.value[0]}{self.hair_style.value[0]}的{self.name}"

    def reality(self):
        return f"{self.style.value[2]}假阳具"


# 睾丸
class Testicle(SexualOrgan):
    def __init__(self, left_or_right, style=SizeStyle.MINI, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if style not in SizeStyle:
            raise ValueError(f"Invalid clitoris style '{style}'.")
        self.style = style
        if left_or_right == 'left':
            self.name = "左睾丸"
        else:
            self.name = "右睾丸"
        self.type = Organs.TESTICLE
        self.order = 19

    @staticmethod
    def all_names():
        names = []
        for style in SizeStyle:
            names.append(style.value[0] + '睾丸')
        return names

    def type_name(self):
        return self.style.value[0] + '睾丸'


# 肛门
class Anus(SexualOrgan):
    def __init__(self, style=PluggableStyle.TIGHT, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if style not in PluggableStyle:
            raise ValueError(f"Invalid anus style '{style}'.")
        self.style = style
        self.name = "肛门"
        self.diameter = 3
        self.type = Organs.ANUS
        self.order = 20

    @staticmethod
    def all_names():
        names = []
        for style in PluggableStyle:
            names.append(style.value[0] + '肛门')
        return names

    def type_name(self):
        return self.style.value[0] + '肛门'

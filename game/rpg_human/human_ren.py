from rpg_battle.battle_skill_ren import BS_Protect, BS_Prevent, BS_Hit, BS_Kick, BS_Caress, BS_InsertFinger1, \
    BS_InsertFinger2, BS_InsertFinger3, BS_InsertFinger4, BS_InsertFinger5
from rpg_human.human_organ_ren import SexualOrgan, Organs
from rpg_human.profession_ren import adventurer
from rpg_system.renpy_constant import Character, renpy, say
"""renpy
init -90 python:
"""
import inspect
import random


class SexAttributes(object):
    def __init__(self, inyoku=0.0, s_value=0.0, hentai=0.0, dom=0.0):
        self.inyoku = inyoku
        self.s_value = s_value
        self.hentai = hentai
        self.dom = dom

    @staticmethod
    def random():
        return SexAttributes(random.uniform(0, 5000), random.uniform(0, 5000), random.uniform(0, 5000),
                             random.uniform(0, 5000))

    def plus(self, other):
        self.inyoku += other.inyoku
        self.s_value += other.s_value
        self.hentai += other.hentai
        self.dom += other.dom

    def ge(self, other):
        return self.inyoku >= other.inyoku or self.s_value >= other.s_value or self.hentai >= other.hentai or self.dom >= other.dom


class Human(object):
    def __init__(self, id=0, name="Human", gender='male', organs={}, profession=adventurer, dress=[], inventory=[],
                 money=0):
        self.name = name
        self.gender = gender
        if self.gender == 'male':
            self.gender_pron = '他'
        elif self.gender == 'female' or self.gender == 'femboy':
            self.gender_pron = '她'
        self.organs = organs
        self.profession = profession
        self.dress = dress
        self.inventory = inventory
        self.money = money
        self.faction = []
        self.features = []
        self.status = []
        self.CS = 0  # 战斗力
        self.id = id
        self.battle_skills = [
            BS_Protect(), BS_Prevent(), BS_Hit(), BS_Kick(),
            BS_Caress(), BS_InsertFinger1(), BS_InsertFinger2(), BS_InsertFinger3(), BS_InsertFinger4(),
            BS_InsertFinger5()
        ]
        self.bind_organs()
        self.character = Character(self.show_name())

    def say(self, text):
        image = self.current_image()
        renpy.show(image, at=['right'])
        say(self.character, text)
        renpy.hide(image)

    def show_name(self):
        return f"{self.profession.name()}{self.name}"

    def get_item(self, item_name):
        for item in self.inventory:
            if item.name() == item_name:
                return item
        return None

    def bind_organs(self):
        for organ in self.organs.values():
            if isinstance(organ, list):
                organ[0].belong = self
                organ[1].belong = self
            else:
                organ.belong = self

    def get_organ(self, organ_name):
        return self.organs.get(organ_name)

    def get_normal_organ_flat(self):
        organs = []
        for organ in self.organs.values():
            if isinstance(organ, list):
                if not isinstance(organ[0], SexualOrgan):
                    organs.append(organ[0])
                    organs.append(organ[1])
            elif not isinstance(organ, SexualOrgan):
                organs.append(organ)
        return organs

    def get_battle_organ_flat(self):
        return [
            self.organs[Organs.HAND][0],
            self.organs[Organs.HAND][1],
            self.organs[Organs.FOOT][0],
            self.organs[Organs.FOOT][1]
        ]

    def get_sexual_organ_flat(self):
        organs = []
        for organ in self.organs.values():
            if isinstance(organ, list):
                if isinstance(organ[0], SexualOrgan):
                    organs.append(organ[0])
                    organs.append(organ[1])
            elif isinstance(organ, SexualOrgan):
                organs.append(organ)
        return organs

    def get_organs_flat(self, organ_names):
        organs = []
        for organ_name in organ_names:
            organ = self.organs.get(organ_name)
            if organ is None:
                continue
            if isinstance(organ, list):
                organs.append(organ[0])
                organs.append(organ[1])
            else:
                organs.append(organ)
        return organs

    def current_image(self):
        image_name = 'char'
        if self.gender == 'male' or self.gender == 'femboy':
            image_name += ' boy_nake'
        if self.gender == 'female':
            image_name += ' girl_nake'
        hair_attr = self.organs[Organs.HAIR].image_attribute()
        eye_attr = self.organs[Organs.EYE][0].image_attribute()
        return image_name + ' ' + hair_attr + ' ' + eye_attr

    def has_feature(self, feature):
        for my_feature in self.features:
            if isinstance(feature, str):
                if my_feature.name() == feature:
                    return True
            if inspect.isclass(feature):
                if my_feature == feature:
                    return True
        return False


def empty_human_body_organs():
    return {
        Organs.HAIR: {
            'style': {},
            'color': {}
        },
        Organs.EYE: {
            'style': {},
            'color': {}
        },
        Organs.NOSE: {
            'style': {}
        },
        Organs.CHEEK: {
            'style': {}
        },
        Organs.EAR: {
            'style': {}
        },
        Organs.MOUTH: {
            'style': {}
        },
        Organs.ARM: {
            'style': {}
        },
        Organs.HAND: {
            'style': {}
        },
        Organs.CHEST: {
            'style': {},
            'cup_size': {}
        },
        Organs.ABDOMEN: {
            'style': {}
        },
        Organs.ASS: {
            'style': {}
        },
        Organs.LEG: {
            'style': {}
        },
        Organs.FOOT: {
            'style': {}
        }
    }


def empty_human_sexual_organs():
    return {
        Organs.VAGINA: {
            'style': {}
        },
        Organs.CLITORIS: {
            'style': {}
        },
        Organs.LABIA: {
            'style': {},
            'hair_style': {}
        },
        Organs.URETHRA: {
            'style': {}
        },
        Organs.PENIS: {
            'style': {},
            'hair_style': {}
        },
        Organs.TESTICLE: {
            'style': {}
        },
        Organs.ANUS: {
            'style': {}
        }
    }

from rpg_cards.cards_ren import Card
from rpg_system.renpy_constant import renpy
from rpg_world.player_ren import player

"""renpy
init -100 python:
"""

TAG_SEX = '淫欲'
TAG_HENTAI = '变态'
TAG_SERVANT = '侍奉'
TAG_SADISM = '虐待'
TAG_PLAY = '玩弄'

TAGS = [TAG_SEX, TAG_HENTAI, TAG_SERVANT, TAG_SADISM, TAG_PLAY]

THEME_MACHINE = '机械'
THEME_TENTACLE = '触手'
THEME_PUBLIC = '公共'
THEME_LOVE = '纯爱'
THEME_GOBLIN = '哥布林'
THEME_SLIME = '史莱姆'
THEME_GIRL_LOVE = '百合'

ORGAN_ANAL = "肛门"
ORGAN_PUSSY = "阴道"

ButtPlugL = 'ButtPlugL'
ButtPlugM = 'ButtPlugM'
ButtPlugS = 'ButtPlugS'
LockButtPlug = 'LockButtPlug'
AnalBeadsL = 'AnalBeadsL'
AnalBeadsM = 'AnalBeadsM'
AnalBeadsS = 'AnalBeadsS'
EnemaKit = 'EnemaKit'
DildoL = 'DildoL'
DildoM = 'DildoM'
DildoS = 'DildoS'
Vibrator = 'Vibrator'
Clamp = 'Clamp'
Gag = 'Gag'
Rope = 'Rope'
Handcuffs = 'Handcuffs'
Pump = 'Pump'
Speculum = 'Speculum'
Special = 'Special'

BATTLE_ACTION_EXP = {

}


class BattleAction:
    def __init__(self, name, tags, theme, title, fantasy, reality, organ_require=None, toys_require=None, level=2,
                 suit='Pikes'):
        self.name = name
        self.tags = tags
        self.title = title
        self.fantasy = fantasy
        self.reality = reality
        self.level = level
        self.suit = suit
        self.theme = theme
        self.organ_require = organ_require
        self.toys_require = toys_require
        self.image = 'images/battle_actions/' + self.name
        if player.is_femboy and renpy.loadable(self.name + '_femboy', 'images/battle_actions'):
            self.image += '_femboy'
        self.image += '.png'

    def display_text(self):
        exp_display = [
            '',
            '青涩',
            '初学',
            '熟练',
            '专家',
            '大师',
        ]
        return f"{{color=#FFC300}}Exp {exp_display[self.exp()]}{{/color}}\n{self.title}"

    def card(self):
        card_name = 'battle_' + self.name
        if '_femboy' in self.image:
            card_name += '_femboy'
        return Card(self.level, self.suit, card_name, self.display_text(), self.display_text(), self)

    def exp(self, add=0):
        if self.name not in BATTLE_ACTION_EXP:
            BATTLE_ACTION_EXP[self.name] = 1
        if add != 0:
            BATTLE_ACTION_EXP[self.name] += add
        return min(int(BATTLE_ACTION_EXP[self.name] / 10) + 1, 5)


ACTION_LIBRARY = [
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰"),
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰"),
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰"),
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰"),
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰"),
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰"),
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰"),
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰"),
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰"),
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰"),
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰"),
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰"),
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰"),
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰"),
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰"),
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰"),
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰"),
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰"),
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰"),
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰"),
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰"),
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰"),
    ("lo_masturbate", [TAG_SEX], THEME_LOVE, "自慰", "自慰", "自慰")
]

"""renpy
init -100 python:
"""
from rpg_cards.cards_ren import Card

TAG_SEX = '淫欲'
TAG_HENTAI = '变态'
TAG_SERVANT = '侍奉'
TAG_SADISM = '虐待'
TAG_PLAY = '玩弄'

TAGS = [TAG_SEX, TAG_HENTAI, TAG_SERVANT, TAG_SADISM, TAG_PLAY]


class BattleAction:
    def __init__(self, name, tags, title, fantasy, reality, level=2, suit='Pikes'):
        self.name = name
        self.tags = tags
        self.title = title
        self.fantasy = fantasy
        self.reality = reality
        self.level = level
        self.suit = suit
        self.exp = 1

    def display_text(self):
        return f"{{color=#FFC300}}Exp {self.exp}{{/color}}\n{self.title}"

    def card(self):
        return Card(self.level, self.suit, self.name, self.display_text(), self.display_text(), self)


ACTION_LIBRARY = [
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
    ("masturbate", [TAG_SEX], "自慰", "自慰", "自慰"),
]

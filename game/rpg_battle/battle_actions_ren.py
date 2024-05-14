"""renpy
init -100 python:
"""
TAG_SEX = '淫欲'
TAG_HENTAI = '变态'
TAG_SERVANT = '侍奉'
TAG_SADISM = '虐待'
TAG_PLAY = '玩弄'

TAGS = [TAG_SEX, TAG_HENTAI, TAG_SERVANT, TAG_SADISM, TAG_PLAY]


class BattleAction:
    def __init__(self, name, tags, title, fantasy, reality):
        self.name = name
        self.tags = tags
        self.title = title
        self.fantasy = fantasy
        self.reality = reality
        self.exp = 0
        self.level = 1

    def display_text(self):
        return f"{{color=#FFC300}}lv {self.level}{{/color}}\n{self.title}"


CA_MASTURBATE = BattleAction("masturbate", [TAG_SEX], "自慰", "自慰", "自慰")

"""renpy
init -90 python:
"""
from rpg_cards.cards_ren import Card


class Area:
    def __init__(self, code, level, name, description, links):
        self.code = code
        self.level = level
        self.name = name
        self.description = description
        self.links = links
        self.background = f"images/world/world_{code}.png"

    def card(self):
        return Card(self.level, "Pikes", 'world_' + self.code, self.name, self.description, self, False)


AREA_MAP = {
    "uk": Area("uk", 14, "未知区域", "NPC的默认位置，你不应该看到这段话", []),
    "g1": Area("g1", 2, "城门", "走出去就到了城外", ["m1"]),
    "mg1": Area("mg1", 6, "魔法师工会", "这里是魔法师工会，是魔法师们交流的地方", ["m1"]),
    "ag1": Area("ag1", 6, "冒险者公会", "这里是冒险者公会，是冒险者们交流的地方", ["m1"]),
    "m1": Area("m1", 2, "市场", "这里是市场，是城市的交易中心", ["cs1", "mg1", "ag1", "g1"]),
    "t1": Area("t1", 2, "酒馆", "这里是酒馆，是城市的休闲场所", ["ra1"]),
    "l1": Area("l1", 4, "图书馆", "这里是图书馆，是城市的知识中心", ["ura1"]),
    "c1": Area("c1", 4, "教会", "这里是教会，是城市的信仰中心", ["ra1"]),
    "ra1": Area("ra1", 2, "住宅区", "这里是住宅区，是城市的居住地", ["cs1", "c1"]),
    "ura1": Area("ura1", 6, "贵族区", "这里是贵族区，是城市的富人区", ["mc1", "l1","cs1"]),
    "mc1": Area("mc1", 10, "骑士团兵营", "这里是骑士团的兵营", ["ura1"]),
    "cs1": Area("cs1", 2, "中央广场", "这里是城市的中央广场，人来人往，热闹非凡",
                ["ra1", "ura1", "m1", "pg1"]),
    "pg1": Area("pg1", 7, "王宫大门", "王宫的大门，有一些守卫站着", ["cs1", "pc1"]),
    "pc1": Area("pc1", 8, "王宫内院", "王宫的内院，有一些花草树木", ["pg1", "ph1"]),
    "ph1": Area("ph1", 8, "王宫大厅", "王宫的大厅，有一些士兵在巡逻",
                ["pc1", "pbh1", "pb1", "ps1", "psr1", "kbr1", "pbr1_0", "pbr1_1"]),
    "pbh1": Area("pbh1", 9, "王宫宴会厅", "王宫的宴会厅，有一些贵族在聚会", ["ph1"]),
    "pb1": Area("pb1", 9, "王宫后院", "王宫的后院，有一些宠物在玩耍", ["ph1"]),
    "ps1": Area("ps1", 9, "王宫书房", "王宫的书房，有一些书籍", ["ph1"]),
    "psr1": Area("psr1", 13, "王宫密室", "王宫的密室，有一些宝藏", ["ph1"]),
    "kbr1": Area("kbr1", 10, "国王卧室", "国王的卧室", ["ph1"]),
    "pbr1_0": Area("pbr1_0", 10, "王子卧室", "王子们的卧室", ["ph1"]),
    "pbr1_1": Area("pbr1_1", 10, "公主卧室", "公主们的卧室", ["ph1"]),
}

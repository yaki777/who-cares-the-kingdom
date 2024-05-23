"""renpy
init -100 python:
"""


class Role:
    def __init__(self, code, name, description, level_range, area_weights_day, area_weights_night):
        self.code = code
        self.name = name
        self.description = description
        self.level_range = level_range
        weights_day_sum = sum(area_weights_day.values())
        weights_night_sum = sum(area_weights_night.values())
        self.area_weights_day = {k: v / weights_day_sum for k, v in area_weights_day.items()}
        self.area_weights_night = {k: v / weights_night_sum for k, v in area_weights_night.items()}


ROLE_KING = Role('king', '国王', '国家的统治者', (13, 13), {"uk": 1}, {"uk": 1})
ROLE_QUEEN = Role('queen', '王后', '国王的妻子', (12, 12),
                  {
                      "pg1": 0.1,
                      "pc1": 0.1,
                      "ph1": 0.1,
                      "pbh1": 2,
                      "pb1": 2,
                      "ps1": 2,
                      "psr1": 0.5,
                      "kbr1": 2,
                      "pbr1_0": 1,
                      "pbr1_1": 1
                  },
                  {
                      "pb1": 1,
                      "ps1": 1,
                      "psr1": 0.5,
                      "kbr1": 4
                  })
ROLE_PRINCE = Role('prince', '王子', '国王的儿子', (6, 10),
                   {
                       "pg1": 0.1,
                       "pc1": 0.1,
                       "ph1": 0.1,
                       "pbh1": 2,
                       "pb1": 1,
                       "ps1": 1,
                       "kbr1": 1,
                       "pbr1_0": 0.5,
                       "ag1": 0.5,
                       "mg1": 0.5,
                       "cs1": 0.5,
                       "t1": 0.5,
                       "g1": 0.5
                   },
                   {
                       "t1": 1,
                       "pbh1": 2,
                       "pb1": 1,
                       "pbr1_0": 4
                   })
ROLE_PRINCESS = Role('princess', '公主', '国王的女儿', (6, 10),
                     {
                         "pg1": 0.1,
                         "pc1": 0.1,
                         "ph1": 0.1,
                         "pbh1": 2,
                         "pb1": 1,
                         "ps1": 1,
                         "pbr1_1": 3,
                         "ag1": 0.5,
                         "mg1": 0.5,
                         "cs1": 0.5,
                         "g1": 0.5
                     },
                     {
                         "pbh1": 2,
                         "pb1": 1,
                         "pbr1_1": 4
                     })
ROLE_MINISTER = Role('minister', '大臣', '国王的重要顾问', (9, 11),
                     {
                         "pg1": 0.1,
                         "pc1": 0.1,
                         "ph1": 0.1,
                         "pbh1": 2,
                         "c1": 0.5,
                         "t1": 0.5,
                         "m1": 0.5,
                         "l1": 0.5,
                         "ura1": 0.5,
                     },
                     {
                         "pbh1": 2,
                         "pb1": 1,
                         "ura1": 4
                     })
ROLE_ENVOY = Role('envoy', '使者', '外交使节', (9, 11),
                  {
                      "pg1": 0.1,
                      "pc1": 0.1,
                      "ph1": 0.1,
                      "pbh1": 4,
                      "t1": 0.5,
                      "m1": 0.5,
                      "l1": 0.5,
                      "ura1": 0.5,
                  },
                  {
                      "pbh1": 2,
                      "pb1": 1,
                      "ura1": 4
                  })
ROLE_KNIGHT = Role('knight', '骑士', '骑士团成员', (11, 11),
                   {
                       "pg1": 0.1,
                       "pc1": 0.1,
                       "ph1": 0.1,
                       "pbh1": 1,
                       "g1": 0.5,
                       "t1": 0.5,
                       "ra1": 0.5,
                       "mc1": 2,
                   },
                   {
                       "mc1": 4,
                       "g1": 0.1,
                       "pg1": 0.1,
                       "pbh1": 0.1
                   })
ROLE_SOLDIER = Role('soldier', '士兵', '军队成员', (5, 10),
                    {
                        "g1": 0.5,
                        "t1": 0.5,
                        "m1": 0.5,
                        "cs1": 0.5,
                        "ra1": 0.5,
                        "mc1": 0.5,
                        "pg1": 0.5,
                    },
                    {
                        "g1": 0.5,
                        "t1": 0.5,
                        "m1": 0.5,
                        "cs1": 0.5,
                        "ra1": 0.5,
                        "mc1": 0.5,
                        "pg1": 0.5,
                    })
ROLE_MAGE = Role('mage', '法师', '使用魔法的人', (7, 11),
                 {
                     "g1": 0.5,
                     "t1": 0.5,
                     "m1": 0.5,
                     "mg1": 2,
                     "ra1": 0.5,
                 },
                 {
                     "mg1": 4,
                     "ra1": 4
                 })
ROLE_SCHOLAR = Role('scholar', '学者', '研究者', (7, 9),
                    {
                        "g1": 0.5,
                        "t1": 0.5,
                        "m1": 0.5,
                        "l1": 2,
                        "ra1": 0.5,
                    },
                    {
                        "l1": 4,
                        "ra1": 4
                    })
ROLE_ALCHEMIST = Role('alchemist', '炼金术师', '炼金？哦不，还有更有趣的！', (6, 8),
                      {
                          "m1": 1,
                          "mg1": 1,
                          'al1': 4,
                          "ra1": 1,
                      },
                      {
                          "al1": 4,
                      })
ROLE_DIVINER = Role('diviner', '占卜师', '预言者', (6, 8),
                    {
                        "g1": 0.5,
                        "t1": 2,
                        "m1": 2,
                        "ra1": 0.5,
                    },
                    {
                        "t1": 4,
                        "ra1": 4
                    })
ROLE_MERCHANT = Role('merchant', '商人', '贸易商', (2, 5),
                     {
                         "m1": 4,
                     },
                     {
                         "m1": 4,
                         "ura1": 4
                     })
ROLE_CRAFTSMAN = Role('craftsman', '工匠', '手工艺人', (2, 3),
                      {
                          "m1": 4,
                      },
                      {
                          "m1": 4,
                          "ra1": 4
                      })
ROLE_FARMER = Role('farmer', '农民', '种田的人', (2, 3),
                   {
                       "m1": 1,
                       "g1": 1,
                       "ra1": 1,
                   },
                   {
                       "ra1": 4
                   })
ROLE_ARTIST = Role('artist', '艺术家', '创作艺术的人', (2, 4),
                   {
                       "m1": 1,
                       "g1": 1,
                       "ra1": 1,
                       "cs1": 1,
                   },
                   {
                       "ra1": 4
                   })
ROLE_BARD = Role('bard', '吟游诗人', '演唱诗歌的人', (2, 4),
                 {
                     "m1": 1,
                     "g1": 1,
                     "ra1": 1,
                     "cs1": 1,
                 },
                 {
                     "ra1": 4
                 })
ROLE_ADVENTURER = Role('adventurer', '冒险家', '冒险的人', (2, 11),
                       {
                           "g1": 2,
                           "t1": 0.5,
                           "m1": 0.5,
                           "ag1": 2,
                       },
                       {
                           "g1": 2,
                           "t1": 0.5,
                           "m1": 0.5,
                           "ag1": 2,
                       })
ROLE_HUNTER = Role('hunter', '猎人', '狩猎的人', (2, 4),
                   {
                       "m1": 1,
                       "t1": 1,
                       "g1": 1,
                       "ra1": 1,
                       "cs1": 1,
                   },
                   {
                       "t1": 4,
                       "ra1": 4
                   })
ROLE_THIEF = Role('thief', '盗贼', '偷盗的人', (2, 4),
                  {
                      "m1": 1,
                      "t1": 1,
                      "g1": 1,
                      "ra1": 1,
                      "cs1": 1,
                  },
                  {
                      "t1": 4,
                      "ra1": 4
                  })
ROLE_PRIEST = Role('priest', '牧师', '宗教人士', (6, 10),
                   {
                       "m1": 1,
                       "ra1": 1,
                       "cs1": 1,
                       "c1": 4
                   },
                   {
                       "c1": 4
                   })
ROLE_MONK = Role('monk', '修道士', '修行的人', (6, 10),
                 {
                     "m1": 1,
                     "ra1": 1,
                     "cs1": 1,
                     "c1": 4
                 },
                 {
                     "c1": 4
                 })
ROLE_NUN = Role('nun', '修女', '修行的女性', (6, 10),
                {
                    "m1": 1,
                    "ra1": 1,
                    "cs1": 1,
                    "c1": 4
                },
                {
                    "c1": 4
                })
ROLE_CLERGY = Role('clergy', '主教', '教会的高级官员', (14, 14),
                   {
                       "m1": 1,
                       "ra1": 1,
                       "cs1": 1,
                       "c1": 4
                   },
                   {
                       "c1": 4
                   })
ROLE_SLAVE = Role('slave', '奴隶', '被奴役的人', (2, 3),
                  {
                      "m1": 1,
                      "ra1": 1,
                      "ura1": 1,
                      "cs1": 1
                  },
                  {
                      "ura1": 4
                  })
ROLE_PROSTITUTE = Role('prostitute', '娼妓', '卖淫的女性', (2, 3),
                       {
                           "m1": 1,
                           "ra1": 1,
                           "t1": 1
                       },
                       {
                           "t1": 4,
                           "ra1": 4
                       })

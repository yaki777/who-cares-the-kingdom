from rpg_role.roles_ren import Role

"""renpy
init -99 python:
"""

DUNGEON_ROLE_SLAVE = Role('dungeon_slave', '逃跑的奴隶', '逃跑的奴隶', (2, 3),
                          {
                              'dungeon_2': 5,
                              'dungeon_3': 3,
                              'dungeon_4': 1,
                          },
                          {
                              'dungeon_2': 5,
                              'dungeon_3': 3,
                              'dungeon_4': 1,
                          })

DUNGEON_ROLE_THIEF = Role('dungeon_thief', '流亡的盗贼', '流亡的盗贼', (3, 4),
                          {
                              'dungeon_2': 5,
                              'dungeon_3': 3,
                              'dungeon_4': 3,
                              'dungeon_5': 1,
                          },
                          {
                              'dungeon_2': 5,
                              'dungeon_3': 3,
                              'dungeon_4': 3,
                              'dungeon_5': 1,
                          })
DUNGEON_ROLE_HUNTER = Role('dungeon_hunter', '凶狠的猎人', '凶狠的猎人', (4, 5),
                           {
                               'dungeon_3': 2,
                               'dungeon_4': 3,
                               'dungeon_5': 3,
                               'dungeon_6': 1,
                           },
                           {
                               'dungeon_3': 2,
                               'dungeon_4': 3,
                               'dungeon_5': 3,
                               'dungeon_6': 1,
                           })
DUNGEON_ROLE_ADVENTURER = Role('dungeon_adventurer', '流氓冒险家', '流氓冒险家', (5, 7),
                               {
                                   'dungeon_4': 1,
                                   'dungeon_5': 3,
                                   'dungeon_6': 5,
                                   'dungeon_7': 3,
                                   'dungeon_8': 1
                               },
                               {
                                   'dungeon_4': 1,
                                   'dungeon_5': 3,
                                   'dungeon_6': 5,
                                   'dungeon_7': 3,
                                   'dungeon_8': 1
                               })
DUNGEON_ROLE_SOLDIER = Role('dungeon_soldier', '外国士兵', '外国士兵', (7, 11),
                            {
                                'dungeon_6': 3,
                                'dungeon_7': 5,
                                'dungeon_8': 5,
                                'dungeon_9': 3,
                                'dungeon_10': 1,
                            },
                            {
                                'dungeon_6': 3,
                                'dungeon_7': 5,
                                'dungeon_8': 5,
                                'dungeon_9': 3,
                                'dungeon_10': 1,
                            })
DUNGEON_ROLE_MAGE = Role('dungeon_mage', '邪恶法师', '邪恶法师', (8, 13),
                         {
                             'dungeon_8': 3,
                             'dungeon_9': 5,
                             'dungeon_10': 5,
                             'dungeon_11': 3,
                         },
                         {
                             'dungeon_8': 3,
                             'dungeon_9': 5,
                             'dungeon_10': 5,
                             'dungeon_11': 3,
                         })

DUNGEON_ROLES = [
    DUNGEON_ROLE_SLAVE,
    DUNGEON_ROLE_THIEF,
    DUNGEON_ROLE_HUNTER,
    DUNGEON_ROLE_ADVENTURER,
    DUNGEON_ROLE_SOLDIER,
    DUNGEON_ROLE_MAGE
]
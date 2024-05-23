from rpg_role.roles_ren import Role

"""renpy
init -99 python:
"""

DUNGEON_ROLE_THIEF = Role('dungeon_thief', '流亡的盗贼', '流亡的盗贼', (0, 0),
                          {
                              'dungeon_base': 1,
                              'dungeon_castle': 1,
                              'dungeon_cave': 1,
                          },
                          {
                              'dungeon_base': 1,
                              'dungeon_castle': 1,
                              'dungeon_cave': 1,

                          })
DUNGEON_ROLE_ADVENTURER = Role('dungeon_adventurer', '流氓冒险家', '流氓冒险家', (0, 0),
                               {
                                   'dungeon_base': 1,
                                   'dungeon_castle': 1,
                                   'dungeon_cave': 1,
                               },
                               {
                                   'dungeon_base': 1,
                                   'dungeon_castle': 1,
                                   'dungeon_cave': 1,
                               })
DUNGEON_ROLE_SOLDIER = Role('dungeon_soldier', '外国士兵', '外国士兵', (0, 0),
                            {
                                'dungeon_base': 1,
                                'dungeon_forest': 1,
                            },
                            {
                                'dungeon_base': 1,
                                'dungeon_forest': 1,
                            })
DUNGEON_ROLE_MAGE = Role('dungeon_mage', '邪恶法师', '邪恶法师', (0, 0),
                         {
                             'dungeon_castle': 1
                         },
                         {
                             'dungeon_castle': 1
                         })
DUNGEON_ROLE_GOBLIN = Role('dungeon_goblin', '哥布林', '哥布林', (0, 0),
                           {
                               'dungeon_forest': 1,
                               'dungeon_cave': 1,
                           },
                           {
                               'dungeon_forest': 1,
                               'dungeon_cave': 1,
                           })
DUNGEON_ROLE_GOBLIN_DOC = Role('dungeon_goblin_doc', '哥布林医师', '哥布林医师', (0, 0),
                               {
                                   'dungeon_forest': 1,
                                   'dungeon_cave': 1,
                               },
                               {
                                   'dungeon_forest': 1,
                                   'dungeon_cave': 1,
                               })
DUNGEON_ROLE_ELF = Role('dungeon_elf', '水精灵', '水精灵', (0, 0),
                        {
                            'dungeon_forest': 1
                        },
                        {
                            'dungeon_forest': 1
                        })
DUNGEON_ROLE_SLIME = Role('dungeon_slime', '史莱姆', '史莱姆', (0, 0),
                          {
                              'dungeon_forest': 1
                          },
                          {
                              'dungeon_forest': 1
                          })
DUNGEON_ROLE_ORC = Role('dungeon_orc', '巨魔', '巨魔', (0, 0),
                        {
                            'dungeon_forest': 1,
                            'dungeon_castle': 1,
                        },
                        {
                            'dungeon_forest': 1,
                            'dungeon_castle': 1,
                        })
DUNGEON_ROLE_TENTACLE = Role('dungeon_tentacle', '触手', '触手', (0, 0),
                             {
                                 'dungeon_cave': 1,
                             },
                             {
                                 'dungeon_cave': 1,
                             })
DUNGEON_ROLES = [
    DUNGEON_ROLE_THIEF,
    DUNGEON_ROLE_ADVENTURER,
    DUNGEON_ROLE_SOLDIER,
    DUNGEON_ROLE_MAGE,
    DUNGEON_ROLE_GOBLIN,
    DUNGEON_ROLE_GOBLIN_DOC,
    DUNGEON_ROLE_ELF,
    DUNGEON_ROLE_SLIME,
    DUNGEON_ROLE_ORC,
    DUNGEON_ROLE_TENTACLE,
]

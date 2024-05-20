label dungeon_slave(npc):
    npc.c "我看到你了！"
    $ battle_controller.start(npc)
    jump dungeon_battle_result

    return

label dungeon_thief(npc):
    npc.c "我看到你了！"
    $ battle_controller.start(npc)
    jump dungeon_battle_result

    return

label dungeon_hunter(npc):
    npc.c "我看到你了！"
    $ battle_controller.start(npc)
    jump dungeon_battle_result

    return

label dungeon_adventurer(npc):
    npc.c "我看到你了！"
    $ battle_controller.start(npc)
    jump dungeon_battle_result

    return

label dungeon_soldier(npc):
    npc.c "我看到你了！"
    $ battle_controller.start(npc)
    jump dungeon_battle_result

    return

label dungeon_mage(npc):
    npc.c "我看到你了！"
    $ battle_controller.start(npc)
    jump dungeon_battle_result
    return

label dungeon_battle_result:
    if not battle_controller.is_win():
        $ dungeon_controller.failed = True
    return
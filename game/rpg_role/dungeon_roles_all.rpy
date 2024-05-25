label dungeon_thief(npc):
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

label dungeon_goblin(npc):
    npc.c "我看到你了！"
    $ battle_controller.start(npc)
    jump dungeon_battle_result
    return

label dungeon_goblin_doc(npc):
    npc.c "我看到你了！"
    $ battle_controller.start(npc)
    jump dungeon_battle_result
    return

label dungeon_elf(npc):
    npc.c "我看到你了！"
    $ battle_controller.start(npc)
    jump dungeon_battle_result
    return

label dungeon_slime(npc):
    npc.c "咕噜...咕噜...."
    $ battle_controller.start(npc)
    jump dungeon_battle_result
    return

label dungeon_orc(npc):
    npc.c "我看到你了！"
    $ battle_controller.start(npc)
    jump dungeon_battle_result
    return
label dungeon_tentacle(npc):
    npc.c "咕噜...咕噜..."
    $ battle_controller.start(npc)
    jump dungeon_battle_result
    return


label dungeon_battle_result:
    if not battle_controller.is_win():
        $ dungeon_controller.failed = True
    return
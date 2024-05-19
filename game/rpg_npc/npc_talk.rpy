label npc_talk(bg,npc,next_label=None,battle_result=None):
    show expression bg
    show expression npc.side_image at right
    if len(npc.stages)>1:
        $ next_label = renpy.display_menu(npc.stages)
    elif len(npc.stages)>0:
        $ next_label = npc.stages[0][1]
    call expression next_label pass (story_controller.get_story(next_label),npc)
    if 'dungeon' in npc.id:
        call start_dungeon(battle_result)
    else:
        call start_world(battle_result)


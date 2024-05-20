label npc_talk(bg,npc,next_label=None):
    show expression bg
    show expression npc.side_image at right
    if len(npc.stages)>1:
        $ story_label = renpy.display_menu(npc.stages)
    elif len(npc.stages)>0:
        $ story_label = npc.stages[0][1]
    else:
        $ story_label = None
    if story_label is not None:
        call expression story_label pass (story_controller.get_story(story_label),npc)
    else:
        call expression next_label pass(npc)
    if 'dungeon' in npc.location:
        call start_dungeon
    else:
        call start_world


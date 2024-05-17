label npc_talk(bg,npc,next_label,battle_result=None):
    show expression bg
    show expression npc.side_image at right
    call expression next_label pass (npc)
    if 'dungeon' in npc.id:
        call start_dungeon(battle_result)
    else:
        call start_world(battle_result)
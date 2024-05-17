label npc_talk(bg,npc,next_label):
    show expression bg
    show expression npc.side_image at right
    call expression next_label pass (npc)
    call screen world_walk
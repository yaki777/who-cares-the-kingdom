label soldier(npc):
    npc.c "市民，你好。"
    return
label soldier_queen(npc):
    npc.c "哦！女王陛下！您好！"
    return
label soldier_queen_g1(npc):
    npc.c "女王陛下！您怎么在这里，这里不安全！"
    menu:
        "要怎么做？"
        "我会回去的。":
            return
        "调情：不安全？你会保护我吗？":
            npc.c "哦，当然，女王陛下。"
            $ battle_controller.start(npc,"start_world")
    return

label soldier_win(npc):
    npc.c "很好，市民！但是请不要告诉别人。"
    return
label soldier_lose(npc):
    npc.c "还不够，市民。"
    return
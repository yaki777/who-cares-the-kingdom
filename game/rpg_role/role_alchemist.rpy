label alchemist(npc):
    npc.c "炼金，是一门神秘的艺术。"
    return
label alchemist_al1(npc):
    npc.c "真难得，有人来这里。"
    menu:
        "要怎么做？"
        "哦，我走错了。":
            return
        "调情：嘿，你这里的机器好有趣。":
            npc.c "哦，当然，女士。你想试试吗"
            $ battle_controller.start(npc)
            npc.c "拿到了很不错的数据。"
    return
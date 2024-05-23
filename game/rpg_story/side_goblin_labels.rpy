label S_GS_stage_1(story,npc):
    DM "你中了哥布林的媚药。"
    if player.has_goblin_antidote:
        DM "不过你有解药。"
        menu:
            "使用解药":
                DM "你偷偷吃下了解药。"
                DM "没有了媚药的作用，逃离这里还是很容易的。"
                return
            "不使用解药":
                DM "看来你想玩玩。"
    if player.role == ROLE_QUEEN:
        npc.c "我知道你是谁，人类女王。"
    npc.c "不用担心。我们不歧视猎物。你只是我们最新的玩物。"
    $ battle_controller.start(npc)
    if battle_controller.is_win():
        DM "你高超的技巧很快就让它们都满意了。"
        if npc.role == DUNGEON_ROLE_GOBLIN_DOC:
            DM "你从它们身上拿到了媚药的解药。吃下解药后你逃了出来。"
            $ player.has_goblin_antidote = True
            return
        else:
            DM "这几个家伙没有解药。在解除媚药的作用前，你逃不出这里。"
    else:
        DM "你精疲力尽，但是他们还没有满足。"
    DM "你被囚禁在这里，直到你能打败他们。"
    $ story_controller.start_stage("S_GS_stage_2")
    return

label S_GS_stage_2(story,npc):
    DM "新的一轮开始了。"
    $ battle_controller.start(npc)
    if battle_controller.is_win():
        if npc.role == DUNGEON_ROLE_GOBLIN_DOC:
            DM "你从它们身上拿到了媚药的解药。吃下解药后你逃了出来。"
            $ player.has_goblin_antidote = True
            return
        else:
            DM "这几个家伙没有解药。"
    else:
        DM "你精疲力尽，但是他们还没有满足。"
        $ story_controller.start_stage("S_GS_stage_2")


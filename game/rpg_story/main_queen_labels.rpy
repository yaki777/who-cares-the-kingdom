label M_QSK_stage_1(story,npc):
    npc.c "女王陛下，我们的国家现在很危险。除非得到邻国的帮助，否则我们将无法抵抗敌人的入侵。"
    npc.c "他今天会一直在宴会厅里，您可以去找他。"
    $ story_controller.start_stage("M_QSK_stage_2")
    $ story_controller.start_stage("M_HQ_stage_1")
    return

label M_QSK_stage_2(story,npc):
    npc.c "您和使者谈过了吗？"
    return

label M_HQ_stage_1(story,npc):
    npc.c "我听说您遇到了些麻烦。有什么可以为您效劳的吗"
    menu:
        "请他提供帮助":
            $ story.require_help = True
            DM "你像[npc.name]表达了对国家的担忧，希望他能帮助你。"
        "没什么":
            $ story.require_help = False
            DM "你摇了摇头，与[npc.name]聊了一些琐事。"
    if not story.require_help:
        npc.c "祝你好运，女王陛下。"
        return
    npc.c "是的，亲爱的，我很清楚你们岌岌可危的处境。你们的国家正面临入侵，急需援助。然而，作为一个伟大帝国的使者，我的援助并非没有代价。"
    npc.c "我就直说了吧，我需要我们两国之间达成最......亲密的协议，才能全力支持你们。"
    DM "你知道他在暗示什么。但还是询问了协议的内容。"
    npc.c "我亲爱的王后，我需要的是我们两国之间最......亲密的联盟。"
    npc.c "我要求您同意将您的女儿嫁给我的王子。作为回报，我将动用我帝国的全部力量来保卫你的国家不受侵略。"
    menu:
        DM "那个王子是个残忍的混蛋，他觊觎你的女儿已经很久了。"
        "同意":
            $ story.agree_marry = True
            DM "你同意了使者的要求。并于他商定订婚的事宜"
        "拒绝":
            $ story.agree_marry = False
            DM "你严厉地拒绝了使者的要求。"
    if not story.agree_marry:
        npc.c "恐怕你别无选择，亲爱的。你们国家的存亡岌岌可危。如果你不同意我的条件，恐怕我无法保证你的人民的安全。"
        npc.c "再考虑考虑吧，亲爱的。与你所有臣民的生命相比，你女儿的生命算得了什么呢？"
        return
    npc.c "非常好，陛下。我就知道您会看到这种安排的智慧。"
    npc.c "我会立即通知我的王子，为他的到来做好准备。"
    npc.c "在他来之前，我想我们还可以商讨一下更多细节？"
    DM "你注意到使者的眼神有点不安好心。"
    npc.c "如果你要找我的话，晚上我会在上城区的房子里。"
    $ story_controller.start_stage("M_HQ_stage_2")
    return

label M_HQ_stage_2(story,npc):

label M_QSK_stage_1(story,npc):
    npc.c "女王陛下，我们的国家现在很危险。除非得到邻国的帮助，否则我们将无法抵抗敌人的入侵。"
    npc.c "他今天会一直在宴会厅里，您可以去找他。"
    $ story_controller.start_stage("M_QSK_stage_2")
    $ story_controller.start_stage("M_QDW_stage_1")
    return

label M_QSK_stage_2(story,npc):
    npc.c "您和使者谈过了吗？"
    return

label M_QDW_stage_1(story,npc):
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
    npc.c "是的，亲爱的，我很清楚你们岌岌可危的处境。"
    npc.c "我就直说了吧，我需要我们两国之间达成最......亲密的协议，才能全力支持你们。"
    DM "你知道他在暗示什么。但还是询问了协议的内容。"
    npc.c "我要求您同意将您的女儿嫁给我的王子。作为回报，我将动用我帝国的全部力量来保卫你的国家不受侵略。"
    menu:
        DM "那个王子是个残忍的混蛋，他觊觎你的女儿已经很久了。"
        "同意":
            $ story.agree_marry = True
            DM "你同意了使者的要求。并于他商定订婚的事宜"
            DM "你们决定在1周后举行婚礼。"
        "拒绝":
            $ story.agree_marry = False
            DM "你严厉地拒绝了使者的要求。"
        "寻找其他方式❤":
            DM "你示意[npc.name]跟你到无人的房间里。"
            $ battle_controller.start(npc)
            if battle_controller.is_win():
                DM "Wow,了不起。"
                npc.c "我想我们两国已经建立了...亲密的联盟，对吧？"
                $ story_controller.start_stage("M_QDW_stage_10")
                return
            else:
                npc.c "还不够好，亲爱的。"
                return
    if not story.agree_marry:
        npc.c "恐怕你别无选择，亲爱的。你们国家的存亡岌岌可危。如果你不同意我的条件，恐怕我无法保证你的人民的安全。"
        npc.c "再考虑考虑吧，亲爱的。与你所有臣民的生命相比，你女儿的生命算得了什么呢？"
        return
    npc.c "非常好，陛下。我就知道您会看到这种安排的智慧。"
    npc.c "我会立即通知我的王子，为他的到来做好准备。"
    npc.c "在他来之前，我想我们还可以商讨一下更多细节？"
    DM "你注意到使者的眼神有点不安好心。"
    npc.c "如果你要找我的话，晚上我会在上城区的房子里。"
    $ story_controller.start_stage("M_QDW_stage_2")
    $ story_controller.schedule_start_stage(story.wedding_date,"M_QDW_stage_3")
    return

label M_QDW_stage_2(story,npc):
    if npc.role == ROLE_ENVOY:
        npc.c "女王陛下，我们的王子已经准备好了。"
        npc.c "公主殿下呢？"
        DM "你告诉他你正在安排。"
        return
    elif npc.role == ROLE_MINISTER:
        npc.c "陛下！有什么可以为您效劳的吗？"
        DM "你告诉了他与使者的谈话。"
        npc.c "我明白了……陛下，这是一个非常重要的发展。我们需要加快准备速度。"
        npc.c "我会立即召集我的团队。"
        npc.c "我可以问一下您的女儿对这个消息的反应吗？"
        if player.princess_agree_marry is None:
            DM "你告诉[npc.name],公主还不知道"
        elif player.princess_agree_marry:
            DM "你告诉[npc.name],公主已经同意了婚事"
        else:
            DM "你告诉[npc.name],公主不同意婚事。但你没有办法，只能先做准备。"
        npc.c "不管如何，我会立即着手准备。"
        return
    elif npc.role == ROLE_PRINCESS:
        npc.c "妈妈，你来这里有什么事吗？"
        DM "你告诉了她使者的要求。"
        if player.princess_agree_marry == True:
            npc.c "我知道，妈妈。我会尽力配合你的安排。"
            return
        npc.c "妈妈... 你怎么能这样？我... 我要被嫁给一个陌生人？为了拯救王国？"
        $ player.princess_agree_marry = False
        menu:
            "劝告她":
                DM "你告诉[npc.name]你也没有办法，希望她能理解"
            "等一等":
                DM "你告诉她你会想别的办法。"
                return
            "劝告她(另一种方式❤)":
                DM "你靠近了[npc.name],贴着她的脸，抚摸她的肩膀。"
                $ battle_controller.start(npc)
                if battle_controller.is_win():
                    DM "[npc.name]喘着气，尽管还是不愿意，但她决定听从你的安排。"
                    $ player.princess_agree_marry = True
                    return
                else:
                    npc.c "不要这样，妈妈。我不会同意的。"
                    $ player.princess_agree_marry = False
                    return
        if not player.princess_agree_marry:
            DM "[npc.name]没有如你所愿，哭着离开了房间。"
            DM "也许你应该再去找她。"
            $ story_controller.start_stage("M_QFD_stage_1")
    return

label M_QDW_stage_3(story,npc):
    DM "今天是你的女儿结婚的日子。"
    if player.princess_agree_marry:
        DM "你们按时举行了婚礼。"
        DM "使者和王子都很满意。你可以跟使者继续谈谈援军的事情。"
        $ story_controller.start_stage("M_QDW_stage_10")
    else:
        DM "由于公主的缺席，婚礼不能按时举行。"
        story.envoy.c "陛下，我不在乎你的借口！你有最后期限，但你未能达到。"
        story.envoy.c "因此，我们取消订婚并撤回对你的支持。你的无能是不可原谅的。"
        $ story_controller.start_stage("M_QDW_stage_9")
    return

label M_QDW_stage_9(story,npc):
    if npc.role == ROLE_ENVOY:
        npc.c "女王陛下，我很抱歉。我们的国家不会再支持你们了。"
    return

label M_QDW_stage_10(story,npc):
    if npc.role == ROLE_ENVOY:
        npc.c "做得很好，女王陛下。我们的军队马上就会到达。"
    return

label M_QFD_stage_1(story,npc):
    if npc.role == ROLE_MINISTER:
        DM "你询问大臣有没有看到公主"
        npc.c "没有，陛下。"
        DM "你有些担忧，但是让大臣去找公主不是个好选择。"
        DM "也许你应该再问问骑士们。"
    elif npc.role == ROLE_SOLDIER:
        DM "你询问士兵有没有看到公主"
        npc.c "没有，陛下。"
        DM "你有些担忧，但是让士兵去找公主不是个好选择。"
        DM "也许你应该再问问骑士们。"
    elif npc.role == ROLE_KNIGHT:
        DM "你询问骑士有没有看到公主"
        npc.c "没有，陛下。"
        menu:
            "去找公主":
                DM "你让骑士们去找公主。"
                $ story_controller.start_stage("M_QFD_stage_2")
            "再等等":
                DM "你觉得还是等等吧。"
                return
        DM "骑士们出发了。"
        DM "你想到以前公主喜欢去的地方，也许你应该去那里看看。"
        DM "TIPS: 冒险者工会"
        $ story_controller.start_stage("M_QFD_stage_2")
    return

label M_QFD_stage_2(story,npc):
    if npc.role == ROLE_KNIGHT:
        if world_controller.date.timestamp()-story.find_start_date>7*24*3600:
            npc.c "陛下，我有一些令人不安的消息。"
            npc.c "经过一周的搜寻，我找到了失踪的公主，但她已经不再是原来的样子。"
            DM "你有些害怕。"
            npc.c "陛下，公主被迷宫里的怪物训练成了肉便器。她现在只懂得性交。"
            menu:
                DM "你有点不知所措"
                "去见她":
                    DM "你决定去见她。"
                    DM "骑士带着你，到了关着公主的地方。"
                    $ world_controller.place_player("psr1")
                "一定有别的办法":
                    DM "你想到城里有一位神秘的炼金术士，他可能有办法。"
            $ story_controller.start_stage("M_QFD_stage_5")
        else:
            npc.c "陛下，我们还在继续搜寻。"
            DM "你无可奈何的点头。"
    elif npc.role == ROLE_ADVENTURER:
        npc.c "您的女儿？公主？"
        npc.c "好吧，公主前跟随另一支探险队离开了城门。"
        npc.c "她叮嘱我们，不要告诉别人。但是我想既然是女王陛下，还是应该告诉你。"
        DM "你松了一口气，但是还是有些担心。"
        menu:
            DM "也许你也可以跟着探险队出去。"
            "去找她":
                DM "你告诉[npc.c]你要去找女儿。"
                npc.c "陛下，这趟旅程并不安全，他们的目的地是北方的遗弃圣所。"
                npc.c "而且我不能肯定您的参与会有帮助。"
                menu:
                    "我要去":
                        DM "你坚持要去。"
                        npc.c "我需要和我的同伴商量一下。请您在这里等候。"
                        DM "过了一会儿，他们回来了。"
                        npc.c "已经决定您可以加入我们的探险队。然而，我们必须警告您前方的旅程充满危险。"
                        npc.c "当您准备好的时候，到城门来找我们。"
                        $ story_controller.start_stage("M_QFD_stage_3",npc)
                        return
                    "我还是等等":
                        DM "你决定再等等。"
                        npc.c "过几天会有另一支探险队出发，也许他们会找到公主的。"
                        return
            "再等等":
                DM "你决定再等等。"
                npc.c "过几天会有另一支探险队出发，也许他们会找到公主的。"
                return
    return

label M_QFD_stage_3(story,npc):
    if npc.role == ROLE_ADVENTURER:
        npc.c "我们出发吧，陛下。"
        $ dungeon_controller.start(5)
    if npc.role == ROLE_PRINCESS:
        DM "你找到了公主，你让她和你一起回去。"
        npc.c "嗯...是的，我知道。但我想...我想我想再呆一会儿。"
        DM "你很不理解。"
        npc.c "妈妈，那个地精还给了我另外一样东西……一种我从未经历过的欲望。"
        npc.c "嗯...它让我想要你❤。我们能不能玩一会儿？"
        DM "哦不，公主中了哥布林的媚药！"
        if player.has_goblin_antidote:
            menu:
                DM "你碰巧有解药"
                "使用":
                    DM "你给了[npc.name]解药。"
                    DM "[npc.name]恢复了正常，你可以带她回去了。"
                    $ story_controller.start_stage("M_QFD_stage_6")
                    return
        menu:
            "强行带走公主":
                DM "你和[story.the_adventurer.name]用尽力气把[npc.name]带回了城里。"
                DM "城里有一位神秘的炼金术士，他可能有解药。"
                $ story_controller.start_stage("M_QFD_stage_5")
                return
            "接受❤":
                DM "不知道为什么，当你看着[npc.name]时，你也感到一种莫名的欲望。"
                $ battle_controller.start(npc)
                if battle_controller.is_win():
                    DM "在一阵缠绵过后，你们两人都感到了满足。"
                    npc.c "发生了什么？我们做了什么？"
                    npc.c "哦...（开始回忆起事件）不，不是！我被附身了或者什么的！感觉太不对劲了！"
                    DM "公主恢复了正常，你可以带她回去了。"
                    $ story_controller.start_stage("M_QFD_stage_6")
                else:
                    DM "就在这时，一群哥布林跳了出来。"
                    $ goblin = Character("哥布林")
                    goblin "看，我们的女王来了！我们抓到了另一个人类！"
                    goblin "我们该怎么办她？"
                    goblin "让她成为我们中的一员！现在她是我们的了，我们不能让她走。"
                    DM "你被包围了。你依然在尝试带公主离开。"
                    npc.c "妈妈，你太天真了。我们都是这里的囚徒，被自己的欲望所困。你现在才意识到这一点。"
                    $ story_controller.start_stage("S_GS_stage_1")
                return
    return

label M_QFD_stage_5(story,npc):
    if npc.role == ROLE_ALCHEMIST:
        npc.c "哦，女王陛下，您为什么来这里？"
        DM "你告诉了他你的困境。"
        npc.c "啊，媚药......我研究过它们对人类和生物的影响。"
        npc.c "不过，恐怕我没有现成的解药。但是我知道解药的配方。"
        npc.c "女性高潮的淫液和一点点乳汁。"
        menu:
            "也许我能提供...":
                $ battle_controller.start(npc)
                DM "你给了[npc.name]他需要的东西。"
                DM "他很快就调制出了解药。"
                DM "你带着解药回到了公主身边。"
                $ player.has_goblin_antidote = True
                $ story_controller.start_stage("M_QFD_stage_6")
            "这太荒谬了...":
                DM "你拒绝了[npc.name]，转身走了。"
                return
    elif npc.role == ROLE_PRINCESS:
        if player.has_goblin_antidote:
            menu:
                DM "你碰巧有解药"
                "使用":
                    DM "你给了[npc.name]解药。"
                    DM "[npc.name]一阵恍惚，过了一会儿..."
                    $ story_controller.start_stage("M_QFD_stage_6")
                    return
                "不使用":
                    DM "你决定先不使用解药。"
    return

label M_QFD_stage_6(story,npc):
    if npc.role == ROLE_PRINCESS:
        npc.c "发生了什么？我们做了什么？"
        npc.c "哦...（开始回忆起事件）不，不是！我被附身了或者什么的！感觉太不对劲了！"
        DM "你安慰了[npc.name]"
        npc.c "妈妈，我对导致这种局面的行为深感羞愧。但我对您的营救心怀感激。"
        npc.c "我不会再逃避了。我愿意不惜一切拯救我的王国。即使这意味着要嫁给那个王子。"
        DM "你成功了。去问问使者下一步的安排吧。"
        $ story_controller.start_stage("M_QFD_stage_7")
    return
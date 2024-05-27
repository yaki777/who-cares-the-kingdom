default create_character_description_text = ""
label init_player:
    DM "欢迎来到《Who cares the kingdom》"
    DM "首先请完成以下游戏设置。"
    call screen init_toys
    call screen init_profession
    call screen create_world
    DM "很好，你已经完成了基本的设置。接下去我还要问你几个问题"
    menu:
        DM "你希望在游戏中出现涉及阴道的内容吗？"
        "希望":
            DM "好的"
            $ world_controller.allowed_organs.append(ORGAN_PUSSY)
        "不希望":
            DM "好的，与阴道有关的内容将不会出现"
    menu:
        DM "你希望在游戏中出现涉及肛门的内容吗？"
        "希望":
            DM "好的"
            $ world_controller.allowed_organs.append(ORGAN_ANAL)
        "不希望":
            DM "好的，与肛门有关的内容将不会出现"
    menu:
        DM "你希望游戏中你的角色是？"
        "男性(男娘)":
            DM "好的"
            $ player.is_femboy = True
        "女性":
            DM "好的"
            $ player.is_femboy = False


screen create_world:
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        hbox:
            yalign 0.5
            spacing 20
            textbutton "普通模式":
                action [SetVariable("world_controller.game_mode", "v"),SetVariable("create_character_description_text","普通模式，你不需要在现实世界做出行动")]
            textbutton "互动模式":
                action [SetVariable("world_controller.game_mode", "r"),SetVariable("create_character_description_text","互动模式，当你的角色在游戏中行动时，你也要在现实中进行与之匹配的行动❤")]

        textbutton "继续" action Return()

        vbox:
            box_wrap True
            xsize 800
            text create_character_description_text

default init_story_description = ""
screen init_toys:
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        label "选择你愿意在游戏中使用的物品：\n(只有你选择的物品会出现在互动模式中):"

        hbox:
            spacing 10
            box_wrap True
            xmaximum 1080
            for toy in TOY_LIBRARY:
                textbutton toy.name action [AddToSet(world_controller.allowed_toys, toy),SetVariable('init_story_description',toy.description)] text_size 38 xysize (210, 100)

        label "已选择的物品:"

        hbox:
            spacing 10
            box_wrap True
            xmaximum 1080
            for toy in world_controller.allowed_toys:
                textbutton toy.name action [RemoveFromSet(world_controller.allowed_toys, toy)] text_size 38 xysize (210, 100)

        textbutton "完成" action [SetVariable('init_story_description',''),Return()]

        vbox:
            box_wrap True
            xsize 800
            text init_story_description size 34

screen init_profession:
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        label "选择你的身份:"

        hbox:
            spacing 10
            box_wrap True
            xmaximum 1080
            for role in PLAYER_ROLE_LIBRARY:
                textbutton role.name action [SetField(player,'role',role),SetVariable('init_story_description',role.description)] text_size 38 xysize (210, 100)

        label "选择的身份:"

        hbox:
            text player.role.name size 38

        textbutton "完成" action [SetVariable('init_story_description',''),Return()]

        vbox:
            box_wrap True
            xsize 800
            text init_story_description size 34
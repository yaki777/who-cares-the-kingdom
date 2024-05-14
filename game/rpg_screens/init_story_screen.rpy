
label init_story_logic:
    "初始化世界"
    call screen init_toys
    call screen init_profession
    return

screen create_world:
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        hbox:
            yalign 0.5
            spacing 20
            textbutton "虚拟":
                action [SetVariable("world.mode", "v"),SetVariable("create_character_description_text",world_mode["v"])]
            textbutton "真实":
                action [SetVariable("world.mode", "r"),SetVariable("create_character_description_text",world_mode["r"])]

        textbutton "继续" action Return()

        vbox:
            box_wrap True
            xsize 800
            text "{color=%s}%s{/color}" % (create_character_description_text[1], create_character_description_text[0])

default init_story_description = ""
screen init_toys:
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        label "选择你的物品:"

        vpgrid:
            cols 4
            draggable True
            for item in Toys:
                textbutton item.type_name action [AddToSet(inplay_toys, item),SetVariable('init_story_description',item.type_detail)] text_size 40 xysize (250, 500)
        
        label "已选择的物品:"
        
        hbox:
            spacing 10
            box_wrap True
            xmaximum 800
            for item in inplay_toys:
                textbutton item.type_name action [RemoveFromSet(inplay_toys, item)] text_size 20 xysize (150, 50)

        textbutton "完成" action Return()

        vbox:
            box_wrap True
            xsize 800
            text init_story_description size 20

screen init_profession:
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        label "选择你的职业:"

        vpgrid:
            cols 7
            draggable True
            for profession in player_profession_list:
                textbutton profession.name() action [SetField(player,'profession',profession),SetVariable('init_story_description',profession.description())] text_size 20 xysize (150, 50)
        
        label "选择的职业:"
        
        hbox:
            text player.profession.name() size 20

        textbutton "完成" action Return()

        vbox:
            box_wrap True
            xsize 800
            text init_story_description size 20
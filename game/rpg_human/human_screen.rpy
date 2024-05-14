# 头发选择

default create_character_component_active = ''

screen create_character_Hair_component():
    vbox:
        yalign 0.5
        spacing 10

        # 头发风格选择
        textbutton "头发风格: [player.organs[Hair].style.value[0]]" action [SetVariable("create_character_component_active", 'hair_style')]
        
        if create_character_component_active == 'hair_style':
            vpgrid:
                cols 1
                spacing 1
                draggable True
                for style in HairStyle:
                    textbutton style.value[0]:
                        xysize (200,50)
                        action [SetField(player.organs['Hair'], "style", style), SetVariable("create_character_component_active", '')]

        # 头发颜色选择
        textbutton "头发颜色: [player.organs[Hair].color.value[0]]" action [SetVariable("create_character_component_active", 'hair_color')]
        
        if create_character_component_active == 'hair_color':
            vpgrid:
                cols 1
                draggable True
                for color in HumanColor:
                    textbutton str(color.value[0]):
                        xysize (200,50)
                        action [SetField(player.organs['Hair'], "color", color), SetVariable("create_character_component_active", '')]

# 眼睛选择

screen create_character_eye_component():
    vbox:
        yalign 0.5
        spacing 10

        # 眼睛风格选择
        textbutton "眼睛风格: [player.organs[Eye][0].style.value[0]]" action [SetVariable("create_character_component_active", 'eye_style')]
        
        if create_character_component_active == 'eye_style':
            vpgrid:
                cols 1
                spacing 1
                draggable True
                for style in CharacterStyle:
                    textbutton style.value[0]:
                        xysize (200,50)
                        action [SetField(player.organs['Eye'][0], "style", style), SetField(player.organs['Eye'][1], "style", style), SetVariable("create_character_component_active", '')]

        # 眼睛颜色选择
        textbutton "眼睛颜色: [player.organs[Eye][0].color.value[0]]" action [SetVariable("create_character_component_active", 'eye_color')]
        
        if create_character_component_active == 'eye_color':
            vpgrid:
                cols 1
                spacing 1
                draggable True
                for color in HumanColor:
                    textbutton color.value[0]:
                        xysize (200,50)
                        action [SetField(player.organs['Eye'][0], "color", color), SetField(player.organs['Eye'][1], "color", color),SetVariable("create_character_component_active", '')]




# 鼻子选择
default create_character_nose_style_show = False
screen create_character_nose_component():
    vbox:
        yalign 0.5
        spacing 10

        # 鼻子风格选择
        textbutton "鼻子风格: [player.organs[Nose].style.value[0]]" action SetVariable("create_character_component_active", 'nose_style')
        
        if create_character_component_active == 'nose_style':
            vpgrid:
                cols 1
                spacing 1
                draggable True
                for style in CharacterStyle:
                    textbutton style.value[0]:
                        xysize (200,50)
                        action [SetField(player.organs['Nose'], "style", style), SetVariable("create_character_component_active", '')]

# 脸颊选择
default create_character_cheek_style_show = False

screen create_character_cheek_component():
    vbox:
        yalign 0.5
        spacing 10

        # 脸颊风格选择
        textbutton "脸颊风格: [player.organs[Cheek][0].style.value[0]]" action SetVariable("create_character_component_active", 'cheek_style')
        
        if create_character_component_active == 'cheek_style':
            vpgrid:
                cols 1
                spacing 1
                draggable True
                for style in CharacterStyle:
                    textbutton style.value[0]:
                        xysize (200,50)
                        action [SetField(player.organs['Cheek'][0], "style", style), SetField(player.organs['Cheek'][1], "style", style), SetVariable("create_character_component_active", '')]
# 耳朵选择
default create_character_ear_style_show = False

screen create_character_ear_component():
    vbox:
        yalign 0.5
        spacing 10

        # 耳朵风格选择
        textbutton "耳朵风格: [player.organs[Ear][0].style.value]" action SetVariable("create_character_component_active", 'ear_style')
        
        if create_character_component_active == 'ear_style':
            vpgrid:
                cols 1
                spacing 1
                draggable True
                for style in EarStyle:
                    textbutton style.value:
                        xysize (200,50)
                        action [SetField(player.organs['Ear'][0], "style", style), SetField(player.organs['Ear'][1], "style", style), SetVariable("create_character_component_active", '')]


# 嘴巴
default create_character_mouth_style_show = False

screen create_character_mouth_component():
    vbox:
        yalign 0.5
        spacing 10

        textbutton "嘴巴风格: [player.organs[Mouth].style.value[0]]" action SetVariable("create_character_component_active", 'mouth_style')
        
        if create_character_component_active == 'mouth_style':
            vpgrid:
                cols 1
                spacing 1
                draggable True
                for style in CharacterStyle:
                    textbutton style.value[0]:
                        xysize (200,50)
                        action [SetField(player.organs['Mouth'], "style", style), SetVariable("create_character_component_active", '')]

# 手
default create_character_hand_style_show = False

screen create_character_hand_component():
    vbox:
        yalign 0.5
        spacing 10

        textbutton "手风格: [player.organs[Hand][0].style.value[0]]" action SetVariable("create_character_component_active", 'hand_style')
        
        if create_character_component_active == 'hand_style':
            vpgrid:
                cols 1
                spacing 1
                draggable True
                for style in BodyStyle:
                    textbutton style.value[0]:
                        xysize (200,50)
                        action [SetField(player.organs['Hand'][0], "style", style), SetField(player.organs['Hand'][1], "style", style), SetVariable("create_character_component_active", '')]

# 手臂
default create_character_arm_style_show = False

screen create_character_arm_component():
    vbox:
        yalign 0.5
        spacing 10

        textbutton "手臂风格: [player.organs[Arm][0].style.value[0]]" action SetVariable("create_character_component_active", 'arm_style')
        
        if create_character_component_active == 'arm_style':
            vpgrid:
                cols 1
                spacing 1
                draggable True
                for style in BodyStyle:
                    textbutton style.value[0]:
                        xysize (200,50)
                        action [SetField(player.organs['Arm'][0], "style", style), SetField(player.organs['Arm'][1], "style", style), SetVariable("create_character_component_active", '')]


# 胸部选择
default create_character_chest_component_chest_style_show = False
default create_character_chest_component_chest_cup_size_show = False

screen create_character_chest_component():
    vbox:
        yalign 0.5
        spacing 10

        # 胸部风格选择
        textbutton "胸部风格: [player.organs[Chest][0].style.value]" action [SetVariable("create_character_component_active", 'chest_style')]
        
        if create_character_component_active == 'chest_style':
            vpgrid:
                cols 1
                spacing 1
                draggable True
                for style in ChestStyle:
                    textbutton style.value:
                        xysize (200,50)
                        action [SetField(player.organs['Chest'][0], "style", style),SetField(player.organs['Chest'][1], "style", style), SetVariable("create_character_component_active", '')]

        # 杯罩尺寸选择
        textbutton "杯罩尺寸: [player.organs[Chest][0].cup_size.value[0]]" action [SetVariable("create_character_component_active", 'cup_size')]
        
        if create_character_component_active == 'cup_size':
            vpgrid:
                cols 1
                draggable True
                for cup in CupSize:
                    textbutton cup.value[0]:
                        xysize (200,50)
                        action [SetField(player.organs['Chest'][0], "cup_size", cup),SetField(player.organs['Chest'][1], "cup_size", cup), SetVariable("create_character_component_active", '')]

# 腹部
default create_character_abdomen_style_show = False

screen create_character_abdomen_component():
    vbox:
        yalign 0.5
        spacing 10

        textbutton "腹部风格: [player.organs[Abdomen].style.value[0]]" action SetVariable("create_character_component_active", 'abdomen_style')
        
        if create_character_component_active == 'abdomen_style':
            vpgrid:
                cols 1
                spacing 1
                draggable True
                for style in BodyStyle:
                    textbutton style.value[0]:
                        xysize (200,50)
                        action [SetField(player.organs['Abdomen'], "style", style), SetVariable("create_character_component_active", '')]

# 臀部
default create_character_ass_style_show = False

screen create_character_ass_component():
    vbox:
        yalign 0.5
        spacing 10

        textbutton "臀部风格: [player.organs[Ass].style.value[0]]" action SetVariable("create_character_component_active", 'ass_style')
        
        if create_character_component_active == 'ass_style':
            vpgrid:
                cols 1
                spacing 1
                draggable True
                for style in BodyStyle:
                    textbutton style.value[0]:
                        xysize (200,50)
                        action [SetField(player.organs['Ass'], "style", style), SetVariable("create_character_component_active", '')]

# 腿
default create_character_leg_style_show = False

screen create_character_leg_component():
    vbox:
        yalign 0.5
        spacing 10

        textbutton "腿风格: [player.organs[Leg][0].style.value[0]]" action SetVariable("create_character_component_active", 'leg_style')
        
        if create_character_component_active == 'leg_style':
            vpgrid:
                cols 1
                spacing 1
                draggable True
                for style in BodyStyle:
                    textbutton style.value[0]:
                        xysize (200,50)
                        action [SetField(player.organs['Leg'][0], "style", style), SetField(player.organs['Leg'][1], "style", style), SetVariable("create_character_component_active", '')]

# 脚
default create_character_foot_style_show = False

screen create_character_foot_component():
    vbox:
        yalign 0.5
        spacing 10

        textbutton "脚风格: [player.organs[Foot][0].style.value[0]]" action SetVariable("create_character_component_active", 'foot_style')
        
        if create_character_component_active == 'foot_style':
            vpgrid:
                cols 1
                spacing 1
                draggable True
                for style in BodyStyle:
                    textbutton style.value[0]:
                        xysize (200,50)
                        action [SetField(player.organs['Foot'][0], "style", style), SetField(player.organs['Foot'][1], "style", style), SetVariable("create_character_component_active", '')]

# 阴道

screen create_character_vagina_component():
    vbox:
        yalign 0.5
        spacing 10

        textbutton "阴道风格: [player.organs[Vagina].style.value[0]]" action SetVariable("create_character_component_active", 'vagina_style')
        
        if create_character_component_active == 'vagina_style':
            vpgrid:
                cols 1
                spacing 20
                draggable True
                for style in PluggableStyle:
                    textbutton style.value[0]:
                        xysize (200,50)
                        action [SetField(player.organs['Vagina'], "style", style), SetVariable("create_character_component_active", '')]

# 阴蒂

screen create_character_clitoris_component():
    vbox:
        yalign 0.5
        spacing 10

        textbutton "阴蒂风格: [player.organs[Clitoris].style.value[0]]" action SetVariable("create_character_component_active", 'clitoris_style')
        
        if create_character_component_active == 'clitoris_style':
            vpgrid:
                cols 1
                spacing 20
                draggable True
                for style in SizeStyle:
                    textbutton style.value[0]:
                        xysize (200,50)
                        action [SetField(player.organs['Clitoris'], "style", style), SetVariable("create_character_component_active", '')]

# 阴唇

screen create_character_labia_component():
    vbox:
        yalign 0.5
        spacing 10

        textbutton "阴唇风格: [player.organs[Labia].style.value[0]]" action SetVariable("create_character_component_active", 'labia_style')
        
        if create_character_component_active == 'labia_style':
            vpgrid:
                cols 1
                spacing 20
                draggable True
                for style in SizeStyle:
                    textbutton style.value[0]:
                        xysize (200,50)
                        action [SetField(player.organs['Labia'], "style", style), SetVariable("create_character_component_active", '')]

        textbutton "阴唇毛发: [player.organs[Labia].hair_style.value[0]]" action SetVariable("create_character_component_active", 'labia_hair_style')
        
        if create_character_component_active == 'labia_hair_style':
            vpgrid:
                cols 1
                spacing 20
                draggable True
                for style in PubicHairStyle:
                    textbutton style.value:
                        xysize (200,50)
                        action [SetField(player.organs['Labia'], "hair_style", style), SetVariable("create_character_component_active", '')]

# 尿道

screen create_character_urethra_component():
    vbox:
        yalign 0.5
        spacing 10

        textbutton "尿道风格: [player.organs[Urethra].style.value[0]]" action SetVariable("create_character_component_active", 'urethra_style')
        
        if create_character_component_active =='urethra_style':
            vpgrid:
                cols 1
                spacing 20
                draggable True
                for style in PluggableStyle:
                    textbutton style.value[0]:
                        xysize (200,50)
                        action [SetField(player.organs['Urethra'], "style", style), SetVariable("create_character_component_active", '')]

# 阴茎

screen create_character_penis_component():
    vbox:
        yalign 0.5
        spacing 10

        textbutton "阴茎风格: [player.organs[Penis].style.value[0]]" action SetVariable("create_character_component_active", 'penis_style')
        
        if create_character_component_active == 'penis_style':
            vpgrid:
                cols 1
                spacing 20
                draggable True
                for style in SizeStyle:
                    textbutton style.value[0]:
                        xysize (200,50)
                        action [SetField(player.organs['Penis'], "style", style), SetVariable("create_character_component_active", '')]

        textbutton "阴茎毛发: [player.organs[Penis].hair_style.value]" action SetVariable("create_character_component_active", 'penis_hair_style')
        
        if create_character_component_active == 'penis_hair_style':
            vpgrid:
                cols 1
                spacing 20
                draggable True
                for style in PubicHairStyle:
                    textbutton style.value:
                        xysize (200,50)
                        action [SetField(player.organs['Penis'], "hair_style", style), SetVariable("create_character_component_active", '')]

# 睾丸

screen create_character_testicle_component():
    vbox:
        yalign 0.5
        spacing 10

        textbutton "睾丸风格: [player.organs[Testicle][0].style.value[0]]" action SetVariable("create_character_component_active", 'testicle_style')
        
        if create_character_component_active == 'testicle_style':
            vpgrid:
                cols 1
                spacing 20
                draggable True
                for style in SizeStyle:
                    textbutton style.value[0]:
                        xysize (200,50)
                        action [SetField(player.organs['Testicle'][0], "style", style), SetField(player.organs['Testicle'][1], "style", style), SetVariable("create_character_component_active", '')]

# 肛门

screen create_character_anus_component():
    vbox:
        yalign 0.5
        spacing 10

        textbutton "肛门风格: [player.organs[Anus].style.value[0]]" action SetVariable("create_character_component_active", 'anus_style')
        
        if create_character_component_active == 'anus_style':
            vpgrid:
                cols 1
                spacing 20
                draggable True
                for style in PluggableStyle:
                    textbutton style.value[0]:
                        xysize (200,50)
                        action [SetField(player.organs['Anus'], "style", style), SetVariable("create_character_component_active", '')]
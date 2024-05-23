from rpg_battle.battle_actions_ren import *

"""renpy
init -99 python:
"""
MA_LIQUID_ENEMA = ('ma_liquid_enema', [TAG_SADISM], THEME_MACHINE,
                   "药液灌肠",
                   "你被用拘束带固定住,一根粗大冰冷的管子插进了你的肛门里。你看着乳白色的浑浊液体顺着管子流进了你的身体里。",
                   "用水管、灌肠袋或者任何其他管状的东西，将300ml任意液体灌入你的菊穴。并保持5分钟。",
                   ORGAN_ANAL, [EnemaKit])

MA_SIMPLE_CHECK_PUSSY = ('ma_simple_check_pussy', [TAG_HENTAI], THEME_MACHINE,
                         "简易检查",
                         "你坐在实验用的椅子上。你的小穴里被插入了一根酷似体温计的冰冷量具。你需要保持不动，等待一会儿。",
                         "趴着，翘起屁股，把一根体温计(或者圆珠笔)插入你的小穴里，保持3分钟。", ORGAN_PUSSY)

MA_SIMPLE_CHECK_ANAL = ('ma_simple_check_anal', [TAG_HENTAI], THEME_MACHINE,
                        "简易检查",
                        "你坐在实验用的椅子上。你的菊穴里被插入了一根酷似体温计的冰冷量具。你需要保持不动，等待一会儿。",
                        "趴着，翘起屁股，把一根体温计(或者圆珠笔)插入你的菊穴里，保持3分钟。", ORGAN_ANAL)
MA_BIRTH_EXPERIENCE_PUSSY = ('ma_birth_experience_pussy', [TAG_SADISM], THEME_MACHINE,
                             "分娩实验",
                             "你被固定在一个类似产床的设备上。你的小穴被扩张器撑开，你看着机器把几颗巨大的卵塞进了你的身体里。",
                             "把一个3个跳蛋塞进你的小穴里，然后把它排出来。", ORGAN_PUSSY, [Special])
MA_BIRTH_EXPERIENCE_ANAL = ('ma_birth_experience_anal', [TAG_SADISM], THEME_MACHINE,
                            "分娩实验",
                            "你站着，双手被绑在身后。你的菊穴被扩张器撑开，你看着机器把一颗巨大的卵塞进了你的身体里。你要靠自己的力量把它排出来。",
                            "你可以选择把一个鸡蛋或者凝胶做的卵或者3个跳蛋塞进你的菊穴里，然后把它排出来。", ORGAN_ANAL,
                            [Special])
MA_FOREIGN_BODY_INSERTION_PUSSY = ('ma_foreign_body_insertion_pussy', [TAG_HENTAI], THEME_MACHINE,
                                   "异物插入",
                                   "你坐在一个类似检查台的设备上。机器把你的双腿打开，露出了你的私处。你看着机器把一个比一般阴茎大一点的异物插进了你的小穴里。",
                                   "坐在椅子上，用中号的假阳具缓慢抽插你的小穴20次。", ORGAN_PUSSY, [DildoM])
MA_FOREIGN_BODY_INSERTION_ANAL = ('ma_foreign_body_insertion_anal', [TAG_HENTAI], THEME_MACHINE,
                                  "异物插入",
                                  "你坐在一个类似检查台的设备上。机器把你的双腿打开，露出了你的菊穴。你看着机器把一个比一般阴茎大一点的异物插进了你的菊穴里。",
                                  "坐在椅子上，用中号的假阳具缓慢抽插你的菊穴20次。", ORGAN_ANAL, [DildoM])
MA_HUGE_FOREIGN_BODY_INSERTION_PUSSY = ('ma_huge_foreign_body_insertion_pussy', [TAG_HENTAI], THEME_MACHINE,
                                        "巨大异物插入",
                                        "你坐在一个类似检查台的设备上。机器把你的双腿打开，露出了你的私处。你看着机器把硕大的异物插进了你的小穴里。",
                                        "坐在椅子上，用大号的假阳具缓慢抽插你的小穴20次。", ORGAN_PUSSY, [DildoL])
MA_HUGE_FOREIGN_BODY_INSERTION_ANAL = ('ma_huge_foreign_body_insertion_anal', [TAG_HENTAI], THEME_MACHINE,
                                       "巨大异物插入",
                                       "你坐在一个类似检查台的设备上。机器把你的双腿打开，露出了你的菊穴。你看着机器把硕大的异物插进了你的菊穴里。",
                                       "坐在椅子上，用大号的假阳具缓慢抽插你的菊穴20次。", ORGAN_ANAL, [DildoL])
MA_CONTINUOUS_OVULATION_TEST = ('ma_continuous_ovulation_test', [TAG_HENTAI], THEME_MACHINE,
                                "持续排卵实验",
                                "你被绑在试验台上，你的菊穴里被连续放入了好几颗异种生物卵。现在你要靠自己的力量把它们排出来。",
                                "涂上大量润滑液，把一串拉珠中的至少3颗插进你的菊穴里，然后用力排出来。", ORGAN_ANAL,
                                [AnalBeadsL])

MA_INNER_COLLECTION_PUSSY = ('ma_inner_collection_pussy', [TAG_HENTAI], THEME_MACHINE,
                             "内部采集",
                             "你上身被固定住，双脚打开站在地上，某种液体收集工具被插入了你的小穴里。你感觉到了一阵阵的抽吸。",
                             "把真空吸器贴在阴蒂上，紧紧吸住。保持5分钟。", ORGAN_PUSSY, [Pump])
MA_INNER_COLLECTION_ANAL = ('ma_inner_collection_anal', [TAG_HENTAI], THEME_MACHINE,
                            "内部采集",
                            "你上身被固定住，双脚打开站在地上，某种液体收集工具被插入了你的菊穴里。你感觉到了一阵阵的抽吸。",
                            "把真空吸器贴在肛门上，紧紧吸住。保持5分钟。", ORGAN_ANAL, [Pump])
MA_INNER_WALL_EXPLORATION_PUSSY = ('ma_inner_wall_exploration_pussh', [TAG_HENTAI], THEME_MACHINE,
                                   "内壁勘探",
                                   "你被绑在地上，一根细长灵活的探测器被插入了你的小穴里，它在你的身体里搅动，试图寻找你敏感的地方。",
                                   "用手指将一个震动着的跳弹推入小穴的深处，并不停搅动，抚摸内壁。持续3分钟后快速抽出。",
                                   ORGAN_PUSSY, [Vibrator])
MA_INNER_WALL_EXPLORATION_ANAL = ('ma_inner_wall_exploration_anal', [TAG_HENTAI], THEME_MACHINE,
                                  "内壁勘探",
                                  "你被绑在地上，一根细长灵活的探测器被插入了你的菊穴里，它在你的身体里搅动，试图寻找你敏感的地方。",
                                  "用手指将一个震动着的跳弹推入菊穴的深处，并不停搅动，抚摸内壁。持续3分钟后快速抽出。",
                                  ORGAN_ANAL, [Vibrator])
MA_OPEN_CHECK_PUSSY = ('ma_open_check_pussy', [TAG_HENTAI], THEME_MACHINE,
                       "开放检查",
                       "你的小穴需要一个全面的检查。你被固定在一个类似产床的设备上。一个窥阴器被插入了你的小穴里，你看着机器把你的小穴里的每个角落都检查了一遍。",
                       "躺在床上，把窥阴器插入小穴，然后扩张到你能承受的最大值。保持住，并拍一张照片。", ORGAN_PUSSY,
                       [Speculum])
MA_OPEN_CHECK_ANAL = ('ma_open_check_anal', [TAG_HENTAI], THEME_MACHINE,
                      "开放检查",
                      "你的菊穴需要一个全面的检查。你被固定在一个类似产床的设备上。一个窥肛器被插入了你的菊穴里，你看着机器把你的菊穴里的每个角落都检查了一遍。",
                      "躺在床上，把窥肛器插入菊穴，然后扩张到你能承受的最大值。保持住，并拍一张照片。", ORGAN_ANAL,
                      [Speculum])
MA_PETRI_DISH = ('ma_petri_dish', [TAG_HENTAI, TAG_SADISM], THEME_MACHINE,
                 "培养皿",
                 "有人想到了一个天才的方案，他要把你变成一个活体培养皿。第一步是要让你的肚子里充满培养液。",
                 "用混合着润滑液的温水灌肠800ML,然后带上肛塞。保持15分钟。", ORGAN_ANAL, [EnemaKit, ButtPlugL])
MA_BIOLOGICAL_REAGENTS = ('ma_biological_reagents', [TAG_HENTAI, TAG_SADISM], THEME_MACHINE,
                          "生物试剂",
                          "你被强迫灌下了一瓶粘稠的溶液，过了一会儿你感觉小腹热热的。",
                          "喝300ML热水。当你想要尿尿的时候，至少忍耐10分钟。")
MA_SALIVA_COLLECTION = ('ma_saliva_collection', [TAG_HENTAI], THEME_MACHINE,
                        "唾液采集",
                        "你被面朝上的固定在床上，一根粗大的管子被插进了你的嘴里。它在你的嘴里搅动，伸到你的喉咙里，试图让你分泌更多的唾液。",
                        "用一个大号的假阳具插入你的嘴里，并深喉3次。", None, [DildoL])

MA_FEEDING_TUBE = ('ma_feeding_tube', [TAG_HENTAI], THEME_MACHINE,
                   "饲管",
                   "你被固定在床上，一根细长的管子被插进了你的嘴里。你感觉到了阵阵的液体流进你的胃里。",
                   "喝200ML水，然后带上口枷，保持20分钟。", None, [Gag])

MA_ORAL_CHECK = ('ma_oral_check', [TAG_HENTAI], THEME_MACHINE,
                 "口腔检查",
                 "一根体温计被插入到了你的嘴里，你被要求保持不动。直到体温计的指针停止移动。",
                 "把一个小号的假阳具插进嘴里，越深越好。保持1分钟。", None, [DildoS])
MA_MILKING = ('ma_milking', [TAG_HENTAI], THEME_MACHINE,
              "挤奶",
              "你站着，双手被绑在身后。你的乳头被吸奶器紧紧吸着，你看到自己的乳汁被抽了出来。",
              "用乳夹夹住乳头，并向外拉。重复10次。", None, [Clamp])

MACHINE_ACTION_LIBRARY = [MA_LIQUID_ENEMA, MA_SIMPLE_CHECK_PUSSY, MA_SIMPLE_CHECK_ANAL, MA_BIRTH_EXPERIENCE_PUSSY,
                          MA_BIRTH_EXPERIENCE_ANAL, MA_FOREIGN_BODY_INSERTION_PUSSY, MA_FOREIGN_BODY_INSERTION_ANAL,
                          MA_HUGE_FOREIGN_BODY_INSERTION_PUSSY, MA_HUGE_FOREIGN_BODY_INSERTION_ANAL,
                          MA_CONTINUOUS_OVULATION_TEST, MA_INNER_COLLECTION_PUSSY, MA_INNER_COLLECTION_ANAL,
                          MA_INNER_WALL_EXPLORATION_PUSSY, MA_INNER_WALL_EXPLORATION_ANAL, MA_OPEN_CHECK_PUSSY,
                          MA_OPEN_CHECK_ANAL, MA_PETRI_DISH, MA_BIOLOGICAL_REAGENTS, MA_SALIVA_COLLECTION,
                          MA_FEEDING_TUBE,
                          MA_ORAL_CHECK, MA_MILKING]

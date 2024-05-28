"""renpy
init -100 python:
"""


class Toy:
    def __init__(self, code, name, description):
        self.code = code
        self.name = name
        self.description = description


ButtPlugL = Toy('ButtPlugL', '大号肛塞',
                '你必须经过充分的扩张才能使用的肛塞，并且插入过程会让你感觉痛苦。')
ButtPlugM = Toy('ButtPlugM', '中号肛塞',
                '经过一点扩张准备就可以使用的肛塞，插入过程会感到满足并且不会感到疼痛。')
ButtPlugS = Toy('ButtPlugS', '小号肛塞',
                '对你来说可以很容易就插入进去的肛塞')
LockButtPlug = Toy('LockButtPlug', '带锁肛塞',
                   '结构复杂的肛塞，底部有一个小的锁定装置，可以用特殊的钥匙打开。一旦插入，只有拥有钥匙的人才能将其拔出。')
AnalBeadsL = Toy('AnalBeadsL', '大号拉珠', '你必须经过充分的扩张才能使用的拉珠，并且使用过程会让你感觉痛苦')
AnalBeadsM = Toy('AnalBeadsM', '中号拉珠', '经过一点扩张准备就可以使用的拉珠，塞入过程会让你感到满足并且不会感到痛苦')
AnalBeadsS = Toy('AnalBeadsS', '小号拉珠', '对你来说可以很容易就塞进去的拉珠')
EnemaKit = Toy('EnemaKit', '灌肠用具', '可以是注射器、淋浴的水管、灌肠袋或者任何可以让水流进去的东西')
DildoL = Toy('DildoL', '大号假阳具', '你必须经过充分的扩张才能使用的假阳具，并且插入过程会让你感觉痛苦。')
DildoM = Toy('DildoM', '中号假阳具', '经过一点扩张准备就可以使用的假阳具，插入过程会让你感到满足并且不会感到疼痛')
DildoS = Toy('DildoS', '小号假阳具', '对你来说可以很容易就插入进去的假阳具')
Vibrator = Toy('Vibrator', '跳蛋', '震动小玩具，可以被塞到身体里面。')
Clamp = Toy('Clamp', '夹子', '乳夹一类的情趣用品或者普通的夹子')
Gag = Toy('Gag', '口球', '口球、口枷或者其他类似的用品')
Rope = Toy('Rope', '绳子', '几段捆绑用的绳子')
Handcuffs = Toy('Handcuffs', '手铐', '一副手铐。请确保一个人玩的时候能够解开它！')
Chastity = Toy('Chastity', '贞操带', '贞操锁或者贞操带')
Pump = Toy('Pump', '吸力器', '一种有吸力的情趣玩具。')
Speculum = Toy('Speculum', '扩张器', '扩张器、窥阴器或者类似的东西')
ElectroStim = Toy('ElectroStim', '电击器', '可以贴在身上的电极片，比如郊狼')
Special = Toy('Special', '其他物品', '选择这个会允许使用生活中的其他物品，比如水果、蔬菜、餐具、文具等等。')

TOY_LIBRARY = [
    ButtPlugL,
    ButtPlugM,
    ButtPlugS,
    LockButtPlug,
    AnalBeadsL,
    AnalBeadsM,
    AnalBeadsS,
    EnemaKit,
    DildoL,
    DildoM,
    DildoS,
    Vibrator,
    Clamp,
    Gag,
    Rope,
    Handcuffs,
    Pump,
    Speculum,
    ElectroStim,
    Special,
]

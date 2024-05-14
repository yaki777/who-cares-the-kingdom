"""renpy
init -100 python:
"""


class Profession:
    def __init__(self):
        self.slots = 1

    def name(self):
        return ""

    def description(self):
        return ""

    def skills(self):
        return []

    def weapon(self):
        return []

    def dress(self):
        return []

    def gender(self):
        return ['male', 'female', 'femboy']

    def allocate(self):
        if self.slots <= 0:
            raise ValueError(f"Too many allocate of {self.name()}")
        self.slots -= 1


class King(Profession):
    def __init__(self):
        self.slots = 1

    def name(self):
        return "国王"

    def description(self):
        return "国家的统治者，持有最高的权力和责任。"

    def skills(self):
        return ["领导力", "战略规划", "外交"]

    def weapon(self):
        return ["王者之剑"]

    def dress(self):
        return ["皇冠", "长袍", "王者之戒"]

    def gender(self):
        return ['male']

    def max_npc(self):
        return 1


class Queen(Profession):
    def __init__(self):
        self.slots = 1

    def name(self):
        return "女王"

    def description(self):
        return "国家的统治者，持有最高的权力和责任。"

    def skills(self):
        return ["领导力", "战略规划", "外交"]

    def weapon(self):
        return ["王者之杖"]

    def dress(self):
        return ["皇冠", "长裙", "王者之项链"]

    def gender(self):
        return ['female', 'femboy']


class Prince(Profession):
    def __init__(self):
        self.slots = 2

    def name(self):
        return "王子"

    def description(self):
        return "王室的年轻成员，可能涉及到继承、结婚和外交情节。"

    def skills(self):
        return ["骑术", "剑术", "外交"]

    def weapon(self):
        return ["练习用剑"]

    def dress(self):
        return ["王子之帽", "正式服装", "皇家徽章"]

    def gender(self):
        return ['male']


class Princess(Profession):
    def __init__(self):
        self.slots = 1

    def name(self):
        return "公主"

    def description(self):
        return "王室的年轻成员，代表王室的尊严和优雅。"

    def skills(self):
        return ["礼仪", "舞蹈", "外交"]

    def weapon(self):
        return []

    def dress(self):
        return ["公主之冠", "华丽裙装", "皇家项链"]

    def gender(self):
        return ['female', 'femboy']


class Minister(Profession):
    def __init__(self):
        self.slots = 6

    def name(self):
        return "大臣"

    def description(self):
        return "国王的顾问，掌握政府的实际运作。"

    def skills(self):
        return ["政策制定", "管理", "谈判"]

    def weapon(self):
        return []

    def dress(self):
        return ["官服", "徽章", "权杖"]


class Envoy(Profession):
    def __init__(self):
        self.slots = 2

    def name(self):
        return "使者"

    def description(self):
        return "从其他国家或城市来的外交官，代表其国家的利益。"

    def skills(self):
        return ["外交", "谈判", "语言能力"]

    def weapon(self):
        return []

    def dress(self):
        return ["使节服装", "外交徽章", "书信袋"]


class Knight(Profession):
    def __init__(self):
        self.slots = 6

    def name(self):
        return "骑士"

    def description(self):
        return "穿着盔甲的战士，有自己的荣誉准则。"

    def skills(self):
        return ["剑术", "骑术", "防御战术"]

    def weapon(self):
        return ["长剑", "盾牌"]

    def dress(self):
        return ["骑士盔甲", "头盔", "骑士之盾"]


class Guard(Profession):
    def __init__(self):
        self.slots = 12

    def name(self):
        return "护卫"

    def description(self):
        return "皇宫或城市的守卫，保护城市和王室的安全。"

    def skills(self):
        return ["近战战斗", "观察", "巡逻"]

    def weapon(self):
        return ["短剑", "长矛"]

    def dress(self):
        return ["护卫制服", "头盔", "护腕"]


class Soldier(Profession):
    def __init__(self):
        self.slots = 50

    def name(self):
        return "士兵"

    def description(self):
        return "普通的军队成员，执行军队的命令。"

    def skills(self):
        return ["基础战斗技巧", "团队合作", "军事训练"]

    def weapon(self):
        return ["弓箭", "短剑"]

    def dress(self):
        return ["士兵制服", "皮甲", "头巾"]


class Mage(Profession):
    def __init__(self):
        self.slots = 10

    def name(self):
        return "法师"

    def description(self):
        return "研究和施展魔法的人，掌握各种神奇的法术。"

    def skills(self):
        return ["元素魔法", "魔法防护", "法术召唤"]

    def weapon(self):
        return ["魔法杖", "魔法书"]

    def dress(self):
        return ["法师袍", "魔法帽", "魔法戒指"]


class Scholar(Profession):
    def __init__(self):
        self.slots = 10

    def name(self):
        return "学者"

    def description(self):
        return "在学院中教学和研究的人，对各种知识有深入的了解。"

    def skills(self):
        return ["研究", "教学", "历史知识"]

    def weapon(self):
        return []

    def dress(self):
        return ["学者服装", "眼镜", "书本"]


class Alchemist(Profession):
    def __init__(self):
        self.slots = 4

    def name(self):
        return "炼金术师"

    def description(self):
        return "研究魔法药剂和物质转化的人，能制造各种奇妙的药水。"

    def skills(self):
        return ["药剂制造", "材料知识", "实验技巧"]

    def weapon(self):
        return ["炼金瓶", "魔法书"]

    def dress(self):
        return ["炼金术师服装", "防护眼镜", "药草包"]


class Diviner(Profession):
    def __init__(self):
        self.slots = 2

    def name(self):
        return "占卜师"

    def description(self):
        return "预测未来或解读命运的人，通常使用各种神秘的工具。"

    def skills(self):
        return ["占卜术", "解梦", "星相学"]

    def weapon(self):
        return []

    def dress(self):
        return ["占卜师服装", "占卜球", "塔罗牌"]


class Merchant(Profession):
    def __init__(self):
        self.slots = 20

    def name(self):
        return "商人"

    def description(self):
        return "在市场上买卖商品的人，拥有广泛的贸易网络。"

    def skills(self):
        return ["交易技巧", "估价", "谈判"]

    def weapon(self):
        return []

    def dress(self):
        return ["商人服装", "交易记录本", "金币袋"]


class Craftsman(Profession):
    def __init__(self):
        self.slots = 20

    def name(self):
        return "工匠"

    def description(self):
        return "制作武器、工具和其他物品的人，手艺娴熟。"

    def skills(self):
        return ["打铁", "木工", "雕刻"]

    def weapon(self):
        return []

    def dress(self):
        return ["工匠服装", "工具带", "手套"]


class Farmer(Profession):
    def __init__(self):
        self.slots = 50

    def name(self):
        return "农民"

    def description(self):
        return "种植粮食的人"

    def skills(self):
        return []

    def weapon(self):
        return []

    def dress(self):
        return []


class Artist(Profession):
    def __init__(self):
        self.slots = 4

    def name(self):
        return "艺术家"

    def description(self):
        return "画家、雕塑家或音乐家，创作美丽的艺术品。"

    def skills(self):
        return ["绘画", "雕塑", "演奏"]

    def weapon(self):
        return []

    def dress(self):
        return ["艺术家服装", "画笔", "乐器"]


class Bard(Profession):
    def __init__(self):
        self.slots = 4

    def name(self):
        return "吟游诗人"

    def description(self):
        return "讲述故事和传唱歌曲的人，擅长娱乐和讲述历史。"

    def skills(self):
        return ["歌唱", "叙事", "演奏乐器"]

    def weapon(self):
        return ["小刀"]

    def dress(self):
        return ["吟游诗人服装", "吉他或其他乐器", "故事集"]


class Adventurer(Profession):
    def __init__(self):
        self.slots = 8

    def name(self):
        return "冒险家"

    def description(self):
        return "寻找宝藏和未知之地的人，勇敢并喜欢探索。"

    def skills(self):
        return ["探险", "地图阅读", "求生技能"]

    def weapon(self):
        return ["短剑", "弓箭"]

    def dress(self):
        return ["冒险家服装", "背包", "地图"]


class Hunter(Profession):
    def __init__(self):
        self.slots = 10

    def name(self):
        return "猎人"

    def description(self):
        return "追踪和捕猎动物的人，对自然有深入的了解。"

    def skills(self):
        return ["射击", "捕猎", "动物追踪"]

    def weapon(self):
        return ["长弓", "短刀"]

    def dress(self):
        return ["猎人服装", "箭袋", "陷阱"]


class Thief(Profession):
    def __init__(self):
        self.slots = 8

    def name(self):
        return "盗贼"

    def description(self):
        return "偷窃和潜入的专家，擅长避免被发现。"

    def skills(self):
        return ["潜行", "锁匠技能", "快速逃跑"]

    def weapon(self):
        return ["匕首"]

    def dress(self):
        return ["盗贼服装", "面罩", "小偷工具"]


class Priest(Profession):
    def __init__(self):
        self.slots = 4

    def name(self):
        return "牧师"

    def description(self):
        return "在教堂中传播宗教教义的人，为信徒提供精神指导。"

    def skills(self):
        return ["宗教学", "祈祷", "治疗"]

    def weapon(self):
        return []

    def dress(self):
        return ["牧师袍", "宗教徽章", "祈祷书"]


class Monk(Profession):
    def __init__(self):
        self.slots = 4

    def name(self):
        return "修道士"

    def description(self):
        return "在修道院中度过的虔诚信徒，过着简朴的生活。"

    def skills(self):
        return ["冥想", "手工艺", "宗教学"]

    def weapon(self):
        return []

    def dress(self):
        return ["修道士服装", "念珠", "头巾"]

    def gender(self):
        return ['male']


class Nun(Profession):
    def __init__(self):
        self.slots = 4

    def name(self):
        return "修女"

    def description(self):
        return "在修道院中度过的虔诚信徒，为信徒提供关怀。"

    def skills(self):
        return ["冥想", "教育", "宗教学"]

    def weapon(self):
        return []

    def dress(self):
        return ["修女服装", "念珠", "修女帽"]

    def gender(self):
        return ['female', 'femboy']


class Clergy(Profession):
    def __init__(self):
        self.slots = 1

    def name(self):
        return "主教"

    def description(self):
        return "进行宗教仪式的人，通常在重要的宗教场合出现。"

    def skills(self):
        return ["宗教仪式", "祈祷", "领导"]

    def weapon(self):
        return []

    def dress(self):
        return ["神职人员服装", "宗教徽章", "权杖"]


class Slave(Profession):
    def __init__(self):
        self.slots = 20

    def name(self):
        return "奴隶"

    def description(self):
        return "被剥夺自由并为他人工作的人，经常受到不公正的对待。"

    def skills(self):
        return ["劳动", "求生意志", "隐匿"]

    def weapon(self):
        return []

    def dress(self):
        return ["破旧的衣服", "锁链", "脚镣"]


class Prostitute(Profession):
    def __init__(self):
        self.slots = 10

    def name(self):
        return "娼妓"

    def description(self):
        return "为了生计提供身体服务的人，社会地位较低，但可能具有丰富的社交和人际关系技巧。"

    def skills(self):
        return ["社交", "心理学", "自我保护"]

    def weapon(self):
        return ["小刀"]

    def dress(self):
        return ["艳丽的衣服", "首饰", "化妆品"]

    def gender(self):
        return ['female', 'femboy']


king = King()  # 国王
queen = Queen()  # 女王
prince = Prince()  # 王子
princess = Princess()  # 公主
minister = Minister()  # 大臣
envoy = Envoy()  # 使者
knight = Knight()  # 骑士
guard = Guard()  # 护卫
soldier = Soldier()  # 士兵
mage = Mage()  # 法师
scholar = Scholar()  # 学者
alchemist = Alchemist()  # 炼金术师
diviner = Diviner()  # 占卜师
merchant = Merchant()  # 商人
craftsman = Craftsman()  # 工匠
farmer = Farmer()  # 农民
artist = Artist()  # 艺术家
bard = Bard()  # 吟游诗人
adventurer = Adventurer()  # 冒险家
hunter = Hunter()  # 猎人
thief = Thief()  # 盗贼
priest = Priest()  # 牧师
monk = Monk()  # 修道士
nun = Nun()  # 修女
clergy = Clergy()  # 主教
slave = Slave()  # 奴隶
prostitute = Prostitute()  # 娼妓

profession_list = [
    king, queen, prince, princess, minister, envoy,
    knight, guard, soldier, mage, scholar, alchemist,
    diviner, merchant, craftsman, farmer, artist, bard,
    adventurer, hunter, thief, priest, monk, nun,
    clergy, slave, prostitute
]

player_profession_list = [
    queen, princess, soldier, mage, adventurer, slave, prostitute
]

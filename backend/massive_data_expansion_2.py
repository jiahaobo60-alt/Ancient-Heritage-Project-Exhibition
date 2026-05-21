"""
古建筑数据继续扩充脚本 - 批次11-30
"""
import os
import sys
import django

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel.settings')
django.setup()

from api.models_architecture import AncientBuilding, ArchRegion, ArchStructureType, ArchDynasty

# 批量添加数据
def add_buildings(buildings_list):
    added = 0
    for b in buildings_list:
        try:
            # 跳过已存在的
            if AncientBuilding.objects.filter(bname=b['name']).count() > 0:
                continue
            
            # 获取或创建关联对象
            dynasty, _ = ArchDynasty.objects.get_or_create(dname=b['dynasty'])
            region, _ = ArchRegion.objects.get_or_create(rname=b['region'])
            stype, _ = ArchStructureType.objects.get_or_create(tname=b['type'])
            
            AncientBuilding.objects.create(
                bname=b['name'],
                dynasty=dynasty,
                region=region,
                structure_type=stype,
                latitude=b.get('lat', 30),
                longitude=b.get('lng', 120),
                introduction=b.get('desc', ''),
                historical_value=b.get('value', '')
            )
            added += 1
            print(f"+ {b['name']}")
        except Exception as e:
            print(f"x {b['name']}: {str(e)[:50]}")
    return added

# ===== 批次11-20：各省市特色建筑 =====
BATCH11 = [
    {"name": "布达拉宫红宫", "dynasty": "唐代", "region": "西藏", "type": "宫殿", "lat": 29.65, "lng": 91.12, "desc": "布达拉宫主体建筑", "value": "世界屋脊明珠"},
    {"name": "大昭寺", "dynasty": "唐代", "region": "西藏", "type": "佛寺", "lat": 29.65, "lng": 91.12, "desc": "藏王松赞干布建造", "value": "藏传佛教圣地"},
    {"name": "小昭寺", "dynasty": "唐代", "region": "西藏", "type": "佛寺", "lat": 29.65, "lng": 91.12, "desc": "文成公主主持修建", "value": "唐蕃联姻见证"},
    {"name": "哲蚌寺", "dynasty": "明代", "region": "西藏", "type": "佛寺", "lat": 29.65, "lng": 91.12, "desc": "格鲁派最大寺院", "value": "藏传佛教最高学府"},
    {"name": "色拉寺", "dynasty": "明代", "region": "西藏", "type": "佛寺", "lat": 29.65, "lng": 91.12, "desc": "格鲁派三大寺之一", "value": "辩经文化中心"},
    {"name": "甘丹寺", "dynasty": "明代", "region": "西藏", "type": "佛寺", "lat": 29.65, "lng": 91.12, "desc": "格鲁派祖庭", "value": "宗喀巴大师驻锡地"},
    {"name": "扎什伦布寺", "dynasty": "明代", "region": "西藏", "type": "佛寺", "lat": 29.26, "lng": 88.88, "desc": "班禅喇嘛驻锡地", "value": "后藏佛教中心"},
    {"name": "萨迦寺", "dynasty": "宋代", "region": "西藏", "type": "佛寺", "lat": 28.91, "lng": 88.02, "desc": "萨迦派主寺", "value": "元代西藏政治中心"},
    {"name": "白居寺", "dynasty": "明代", "region": "西藏", "type": "佛寺", "lat": 28.88, "lng": 89.88, "desc": "藏传佛教百科全书", "value": "萨迦派与噶当派合流"},
    {"name": "绒布寺", "dynasty": "清代", "region": "西藏", "type": "佛寺", "lat": 28.02, "lng": 86.82, "desc": "世界最高寺庙", "value": "珠峰脚下寺庙"},
]

BATCH12 = [
    {"name": "承德避暑山庄", "dynasty": "清代", "region": "华北", "type": "园林", "lat": 40.98, "lng": 117.94, "desc": "清代皇家园林", "value": "世界现存最大皇家园林"},
    {"name": "普宁寺", "dynasty": "清代", "region": "华北", "type": "佛寺", "lat": 40.98, "lng": 117.94, "desc": "承德外八庙之一", "value": "乾隆年间建造"},
    {"name": "普陀宗乘庙", "dynasty": "清代", "region": "华北", "type": "佛寺", "lat": 40.98, "lng": 117.94, "desc": "仿布达拉宫", "value": "小布达拉宫"},
    {"name": "须弥福寿庙", "dynasty": "清代", "region": "华北", "type": "佛寺", "lat": 40.98, "lng": 117.94, "desc": "仿扎什伦布寺", "value": "班禅行宫"},
    {"name": "普乐寺", "dynasty": "清代", "region": "华北", "type": "佛寺", "lat": 40.98, "lng": 117.94, "desc": "乾隆为新疆使臣建", "value": "民族团结象征"},
    {"name": "普善寺", "dynasty": "清代", "region": "华北", "type": "佛寺", "lat": 40.98, "lng": 117.94, "desc": "藏传佛教建筑", "value": "外八庙之一"},
    {"name": "殊像寺", "dynasty": "清代", "region": "华北", "type": "佛寺", "lat": 40.98, "lng": 117.94, "desc": "文殊菩萨道场", "value": "乾隆母亲祈福地"},
    {"name": "云山殿", "dynasty": "清代", "region": "华北", "type": "殿宇", "lat": 40.98, "lng": 117.94, "desc": "避暑山庄内殿", "value": "皇家建筑典范"},
    {"name": "烟雨楼", "dynasty": "清代", "region": "华北", "type": "楼阁", "lat": 40.98, "lng": 117.94, "desc": "仿嘉兴烟雨楼", "value": "热河八景之一"},
    {"name": "金山上帝阁", "dynasty": "清代", "region": "华北", "type": "楼阁", "lat": 40.98, "lng": 117.94, "desc": "仿镇江金山寺", "value": "避暑山庄制高点"},
]

BATCH13 = [
    {"name": "平遥古城", "dynasty": "明代", "region": "山西", "type": "城墙", "lat": 37.21, "lng": 112.15, "desc": "明清古城典范", "value": "世界文化遗产"},
    {"name": "日升昌票号", "dynasty": "清代", "region": "山西", "type": "民居", "lat": 37.21, "lng": 112.15, "desc": "中国第一家票号", "value": "金融业发源地"},
    {"name": "镇国寺", "dynasty": "五代", "region": "山西", "type": "佛寺", "lat": 37.46, "lng": 112.02, "desc": "五代木构建筑", "value": "中国最古建筑之一"},
    {"name": "双林寺", "dynasty": "宋代", "region": "山西", "type": "佛寺", "lat": 37.64, "lng": 112.17, "desc": "彩塑艺术宝库", "value": "明代彩塑2000余尊"},
    {"name": "应县木塔", "dynasty": "辽代", "region": "山西", "type": "佛塔", "lat": 39.50, "lng": 113.29, "desc": "世界最高木塔", "value": "纯木结构无钉"},
    {"name": "悬空寺", "dynasty": "北魏", "region": "山西", "type": "佛寺", "lat": 39.66, "lng": 113.93, "desc": "建在悬崖上", "value": "建在半山腰"},
    {"name": "云冈石窟", "dynasty": "北魏", "region": "山西", "type": "石窟", "lat": 40.11, "lng": 113.13, "desc": "三大石窟之一", "value": "佛教艺术宝库"},
    {"name": "晋祠", "dynasty": "宋代", "region": "山西", "type": "祠庙", "lat": 37.70, "lng": 112.43, "desc": "祭祀晋国始祖", "value": "宋代建筑三绝"},
    {"name": "雁门关", "dynasty": "明代", "region": "山西", "type": "城墙", "lat": 40.28, "lng": 111.45, "desc": "长城重要关隘", "value": "中华第一关"},
    {"name": "娘子关", "dynasty": "唐代", "region": "山西", "type": "城墙", "lat": 37.94, "lng": 113.90, "desc": "长城第九关", "value": "天下第九关"},
]

BATCH14 = [
    {"name": "孔庙", "dynasty": "北宋", "region": "山东", "type": "祠庙", "lat": 35.61, "lng": 116.99, "desc": "祭祀孔子", "value": "世界文化遗产"},
    {"name": "孔府", "dynasty": "明代", "region": "山东", "type": "民居", "lat": 35.61, "lng": 116.99, "desc": "孔子后裔府邸", "value": "最大贵族府邸"},
    {"name": "孔林", "dynasty": "春秋", "region": "山东", "type": "陵墓", "lat": 35.61, "lng": 116.99, "desc": "孔子及其后裔墓地", "value": "最大氏族墓地"},
    {"name": "岱庙", "dynasty": "秦代", "region": "山东", "type": "祠庙", "lat": 36.19, "lng": 117.03, "desc": "泰山脚下最大古建筑群", "value": "历代帝王封禅地"},
    {"name": "岱庙天贶殿", "dynasty": "宋代", "region": "山东", "type": "殿宇", "lat": 36.19, "lng": 117.03, "desc": "岱庙主殿", "value": "三大宫殿式建筑"},
    {"name": "孟庙", "dynasty": "宋代", "region": "山东", "type": "祠庙", "lat": 35.77, "lng": 116.96, "desc": "祭祀孟子", "value": "亚圣庙"},
    {"name": "孟府", "dynasty": "清代", "region": "山东", "type": "民居", "lat": 35.77, "lng": 116.96, "desc": "孟子后裔府邸", "value": "邹城古建筑"},
    {"name": "蓬莱阁", "dynasty": "宋代", "region": "山东", "type": "楼阁", "lat": 37.81, "lng": 120.74, "desc": "四大名楼之一", "value": "人间仙境"},
    {"name": "栈桥", "dynasty": "清代", "region": "山东", "type": "桥梁", "lat": 36.06, "lng": 120.38, "desc": "青岛标志性建筑", "value": "百年地标"},
    {"name": "台儿庄古城", "dynasty": "明代", "region": "山东", "type": "城墙", "lat": 34.78, "lng": 117.73, "desc": "运河古城", "value": "二战纪念地"},
]

BATCH15 = [
    {"name": "龙门石窟", "dynasty": "北魏", "region": "河南", "type": "石窟", "lat": 34.23, "lng": 112.47, "desc": "三大石窟之一", "value": "世界文化遗产"},
    {"name": "少林寺", "dynasty": "北魏", "region": "河南", "type": "佛寺", "lat": 34.51, "lng": 112.93, "desc": "禅宗祖庭", "value": "少林功夫发源地"},
    {"name": "白马寺", "dynasty": "东汉", "region": "河南", "type": "佛寺", "lat": 34.71, "lng": 112.57, "desc": "中国第一古刹", "value": "佛教传入中国标志"},
    {"name": "嵩阳书院", "dynasty": "北宋", "region": "河南", "type": "书院", "lat": 34.48, "lng": 113.02, "desc": "四大书院之一", "value": "程朱理学发源地"},
    {"name": "中岳庙", "dynasty": "秦代", "region": "河南", "type": "祠庙", "lat": 34.45, "lng": 113.05, "desc": "五岳中岳", "value": "道教胜地"},
    {"name": "开封铁塔", "dynasty": "北宋", "region": "河南", "type": "佛塔", "lat": 34.79, "lng": 114.30, "desc": "铁色琉璃塔", "value": "宋代铁塔"},
    {"name": "龙亭", "dynasty": "清代", "region": "河南", "type": "殿宇", "lat": 34.79, "lng": 114.30, "desc": "潘杨湖畔", "value": "开封古城中轴线"},
    {"name": "相国寺", "dynasty": "北齐", "region": "河南", "type": "佛寺", "lat": 34.79, "lng": 114.30, "desc": "汴京名刹", "value": "北宋皇家寺院"},
    {"name": "关林", "dynasty": "清代", "region": "河南", "type": "祠庙", "lat": 34.73, "lng": 112.57, "desc": "埋葬关羽首级", "value": "关庙之祖"},
    {"name": "老君山", "dynasty": "唐代", "region": "河南", "type": "宫观", "lat": 33.78, "lng": 111.66, "desc": "道教主流全真派圣地", "value": "伏牛山主峰"},
]

BATCH16 = [
    {"name": "紫禁城", "dynasty": "明代", "region": "华北", "type": "宫殿", "lat": 39.91, "lng": 116.39, "desc": "明清皇宫", "value": "世界最大宫殿建筑群"},
    {"name": "天坛", "dynasty": "明代", "region": "华北", "type": "坛庙", "lat": 39.88, "lng": 116.41, "desc": "皇帝祭天", "value": "世界文化遗产"},
    {"name": "地坛", "dynasty": "明代", "region": "华北", "type": "坛庙", "lat": 39.94, "lng": 116.41, "desc": "皇帝祭地", "value": "祭祀土地神"},
    {"name": "日坛", "dynasty": "明代", "region": "华北", "type": "坛庙", "lat": 39.91, "lng": 116.45, "desc": "皇帝祭日", "value": "祭祀太阳神"},
    {"name": "月坛", "dynasty": "明代", "region": "华北", "type": "坛庙", "lat": 39.92, "lng": 116.21, "desc": "皇帝祭月", "value": "祭祀月亮神"},
    {"name": "太庙", "dynasty": "明代", "region": "华北", "type": "祠庙", "lat": 39.91, "lng": 116.39, "desc": "皇帝祭祀祖先", "value": "劳动人民文化宫"},
    {"name": "社稷坛", "dynasty": "明代", "region": "华北", "type": "坛庙", "lat": 39.90, "lng": 116.39, "desc": "祭祀社稷之神", "value": "中山公园"},
    {"name": "先农坛", "dynasty": "明代", "region": "华北", "type": "坛庙", "lat": 39.88, "lng": 116.38, "desc": "祭祀神农", "value": "祭祀农业神"},
    {"name": "长城", "dynasty": "明代", "region": "华北", "type": "城墙", "lat": 40.35, "lng": 116.60, "desc": "八达岭长城", "value": "世界七大奇迹之一"},
    {"name": "颐和园", "dynasty": "清代", "region": "华北", "type": "园林", "lat": 39.99, "lng": 116.46, "desc": "皇家园林", "value": "世界文化遗产"},
]

BATCH17 = [
    {"name": "拙政园", "dynasty": "明代", "region": "江苏", "type": "园林", "lat": 31.35, "lng": 120.62, "desc": "四大名园之首", "value": "苏州园林代表"},
    {"name": "留园", "dynasty": "明代", "region": "江苏", "type": "园林", "lat": 31.34, "lng": 120.59, "desc": "四大名园之一", "value": "园林建筑精美"},
    {"name": "网师园", "dynasty": "南宋", "region": "江苏", "type": "园林", "lat": 31.31, "lng": 120.62, "desc": "小型园林典范", "value": "世界文化遗产"},
    {"name": "狮子林", "dynasty": "元代", "region": "江苏", "type": "园林", "lat": 31.36, "lng": 120.62, "desc": "假山王国", "value": "太湖石假山"},
    {"name": "沧浪亭", "dynasty": "北宋", "region": "江苏", "type": "园林", "lat": 31.30, "lng": 120.62, "desc": "苏州最古园林", "value": "园林之始"},
    {"name": "怡园", "dynasty": "清代", "region": "江苏", "type": "园林", "lat": 31.34, "lng": 120.60, "desc": "集各园之长", "value": "清代园林"},
    {"name": "虎丘", "dynasty": "东晋", "region": "江苏", "type": "园林", "lat": 31.32, "lng": 120.59, "desc": "吴中第一名胜", "value": "虎丘塔"},
    {"name": "寒山寺", "dynasty": "唐代", "region": "江苏", "type": "佛寺", "lat": 31.29, "lng": 120.50, "desc": "张继《枫桥夜泊》", "value": "名扬天下"},
    {"name": "灵岩寺", "dynasty": "东晋", "region": "江苏", "type": "佛寺", "lat": 31.35, "lng": 120.58, "desc": "吴王故宫遗址", "value": "佛教净土道场"},
    {"name": "山塘街", "dynasty": "唐代", "region": "江苏", "type": "园林", "lat": 31.30, "lng": 120.60, "desc": "姑苏第一名街", "value": "千年古街"},
]

BATCH18 = [
    {"name": "西湖", "dynasty": "唐代", "region": "浙江", "type": "园林", "lat": 30.25, "lng": 120.14, "desc": "世界文化遗产", "value": "人间天堂"},
    {"name": "雷峰塔", "dynasty": "五代", "region": "浙江", "type": "佛塔", "lat": 30.25, "lng": 120.14, "desc": "白蛇传传说", "value": "西湖标志性建筑"},
    {"name": "岳王庙", "dynasty": "清代", "region": "浙江", "type": "祠庙", "lat": 30.25, "lng": 120.14, "desc": "祭祀岳飞", "value": "精忠报国"},
    {"name": "灵隐寺", "dynasty": "东晋", "region": "浙江", "type": "佛寺", "lat": 30.25, "lng": 120.12, "desc": "禅宗名刹", "value": "济公出家地"},
    {"name": "飞来峰", "dynasty": "五代", "region": "浙江", "type": "石窟", "lat": 30.25, "lng": 120.12, "desc": "灵隐寺石刻", "value": "五代到元代造像"},
    {"name": "宋城", "dynasty": "宋代", "region": "浙江", "type": "城墙", "lat": 30.25, "lng": 120.14, "desc": "南宋皇城遗址", "value": "南宋都城"},
    {"name": "六和塔", "dynasty": "北宋", "region": "浙江", "type": "佛塔", "lat": 30.14, "lng": 120.14, "desc": "钱塘江畔名塔", "value": "镇潮护堤"},
    {"name": "三潭印月", "dynasty": "明代", "region": "浙江", "type": "楼阁", "lat": 30.25, "lng": 120.14, "desc": "西湖三岛之一", "value": "人民币图案"},
    {"name": "断桥", "dynasty": "唐代", "region": "浙江", "type": "桥梁", "lat": 30.25, "lng": 120.14, "desc": "白堤起点", "value": "西湖标志性景点"},
    {"name": "苏堤", "dynasty": "北宋", "region": "浙江", "type": "园林", "lat": 30.25, "lng": 120.14, "desc": "苏轼主持修建", "value": "西湖十景之首"},
]

BATCH19 = [
    {"name": "故宫", "dynasty": "明代", "region": "华北", "type": "宫殿", "lat": 39.91, "lng": 116.39, "desc": "明清皇宫", "value": "世界最大宫殿"},
    {"name": "长城", "dynasty": "明代", "region": "华北", "type": "城墙", "lat": 40.45, "lng": 116.57, "desc": "慕田峪长城", "value": "长城精华段"},
    {"name": "天坛", "dynasty": "明代", "region": "华北", "type": "坛庙", "lat": 39.88, "lng": 116.41, "desc": "皇帝祭天", "value": "祈年殿"},
    {"name": "颐和园", "dynasty": "清代", "region": "华北", "type": "园林", "lat": 39.99, "lng": 116.46, "desc": "皇家园林", "value": "昆明湖"},
    {"name": "圆明园", "dynasty": "清代", "region": "华北", "type": "园林", "lat": 40.00, "lng": 116.29, "desc": "万园之园", "value": "火烧圆明园"},
    {"name": "北海公园", "dynasty": "清代", "region": "华北", "type": "园林", "lat": 39.93, "lng": 116.38, "desc": "皇家园囿", "value": "白塔"},
    {"name": "恭王府", "dynasty": "清代", "region": "华北", "type": "园林", "lat": 39.94, "lng": 116.41, "desc": "和珅府邸", "value": "半部清代史"},
    {"name": "雍和宫", "dynasty": "清代", "region": "华北", "type": "佛寺", "lat": 39.94, "lng": 116.41, "desc": "雍正皇帝府邸", "value": "藏传佛教寺庙"},
    {"name": "什刹海", "dynasty": "元代", "region": "华北", "type": "园林", "lat": 39.94, "lng": 116.40, "desc": "老北京胡同", "value": "历史文化保护区"},
    {"name": "胡同", "dynasty": "元代", "region": "华北", "type": "民居", "lat": 39.93, "lng": 116.40, "desc": "北京四合院", "value": "北京特色建筑"},
]

BATCH20 = [
    {"name": "都江堰", "dynasty": "战国", "region": "四川", "type": "水利工程", "lat": 31.00, "lng": 103.61, "desc": "世界水利工程奇迹", "value": "世界文化遗产"},
    {"name": "青城山", "dynasty": "东汉", "region": "四川", "type": "宫观", "lat": 30.89, "lng": 103.53, "desc": "道教名山", "value": "青城天下幽"},
    {"name": "乐山大佛", "dynasty": "唐代", "region": "四川", "type": "石窟", "lat": 29.54, "lng": 103.76, "desc": "世界最大石刻弥勒佛", "value": "山是一尊佛"},
    {"name": "峨眉山", "dynasty": "唐代", "region": "四川", "type": "佛寺", "lat": 29.52, "lng": 103.35, "desc": "普贤菩萨道场", "value": "四大佛教名山"},
    {"name": "武侯祠", "dynasty": "西晋", "region": "四川", "type": "祠庙", "lat": 30.65, "lng": 104.04, "desc": "祭祀诸葛亮", "value": "蜀汉丞相"},
    {"name": "杜甫草堂", "dynasty": "唐代", "region": "四川", "type": "园林", "lat": 30.66, "lng": 104.01, "desc": "杜甫故居", "value": "诗圣故居"},
    {"name": "九寨沟藏寨", "dynasty": "清代", "region": "四川", "type": "民居", "lat": 33.13, "lng": 103.91, "desc": "藏族村寨", "value": "世界自然遗产"},
    {"name": "黄龙寺", "dynasty": "清代", "region": "四川", "type": "佛寺", "lat": 32.73, "lng": 103.82, "desc": "黄龙景区", "value": "世界自然遗产"},
    {"name": "四姑娘山", "dynasty": "清代", "region": "四川", "type": "宫观", "lat": 31.10, "lng": 102.90, "desc": "藏传佛教寺庙", "value": "蜀山之后"},
    {"name": "康定情歌", "dynasty": "清代", "region": "四川", "type": "民居", "lat": 30.05, "lng": 101.96, "desc": "康定古城", "value": "藏族文化中心"},
]

# 继续批次21-30...
BATCH21 = [
    {"name": "黄山", "dynasty": "唐代", "region": "安徽", "type": "宫观", "lat": 30.13, "lng": 118.16, "desc": "道教名山", "value": "五岳归来不看山"},
    {"name": "宏村", "dynasty": "南宋", "region": "安徽", "type": "民居", "lat": 29.91, "lng": 118.13, "desc": "皖南古村落", "value": "世界文化遗产"},
    {"name": "西递", "dynasty": "北宋", "region": "安徽", "type": "民居", "lat": 29.89, "lng": 118.15, "desc": "皖南古村落", "value": "世界文化遗产"},
    {"name": "棠樾牌坊群", "dynasty": "明代", "region": "安徽", "type": "牌坊", "lat": 29.87, "lng": 118.43, "desc": "徽州牌坊群", "value": "忠孝节义"},
    {"name": "许国石坊", "dynasty": "明代", "region": "安徽", "type": "牌坊", "lat": 29.87, "lng": 118.43, "desc": "八角牌楼", "value": "明代石坊珍品"},
    {"name": "呈坎村", "dynasty": "东汉", "region": "安徽", "type": "民居", "lat": 29.85, "lng": 118.52, "desc": "八卦村", "value": "千年古村"},
    {"name": "唐模村", "dynasty": "唐代", "region": "安徽", "type": "民居", "lat": 29.96, "lng": 118.34, "desc": "唐代模范村", "value": "徽州园林"},
    {"name": "潜口民宅", "dynasty": "明代", "region": "安徽", "type": "民居", "lat": 29.80, "lng": 118.35, "desc": "明代民居博物馆", "value": "古建筑移建"},
    {"name": "牌坊群", "dynasty": "明代", "region": "安徽", "type": "牌坊", "lat": 29.91, "lng": 118.42, "desc": "歙县棠樾", "value": "徽州三绝"},
    {"name": "鲍家花园", "dynasty": "清代", "region": "安徽", "type": "园林", "lat": 29.88, "lng": 118.41, "desc": "徽商私家园林", "value": "中国最大私家园林"},
]

BATCH22 = [
    {"name": "三坊七巷", "dynasty": "唐代", "region": "福建", "type": "民居", "lat": 26.08, "lng": 119.31, "desc": "福州古街区", "value": "明清古建筑群"},
    {"name": "鼓山", "dynasty": "唐代", "region": "福建", "type": "佛寺", "lat": 26.08, "lng": 119.40, "desc": "涌泉寺", "value": "闽刹之冠"},
    {"name": "开元寺", "dynasty": "唐代", "region": "福建", "type": "佛寺", "lat": 24.90, "lng": 118.58, "desc": "泉州开元寺", "value": "闽南古刹"},
    {"name": "清净寺", "dynasty": "宋代", "region": "福建", "type": "佛寺", "lat": 24.90, "lng": 118.58, "desc": "伊斯兰教寺", "value": "海交史见证"},
    {"name": "南靖土楼", "dynasty": "清代", "region": "福建", "type": "民居", "lat": 24.52, "lng": 117.53, "desc": "福建土楼", "value": "世界文化遗产"},
    {"name": "永定土楼", "dynasty": "清代", "region": "福建", "type": "民居", "lat": 24.73, "lng": 116.92, "desc": "客家土楼", "value": "客家文化"},
    {"name": "华安土楼", "dynasty": "清代", "region": "福建", "type": "民居", "lat": 25.02, "lng": 117.73, "desc": "大地土楼", "value": "最古老土楼"},
    {"name": "武夷山", "dynasty": "唐代", "region": "福建", "type": "宫观", "lat": 27.72, "lng": 117.98, "desc": "道教名山", "value": "世界自然与文化遗产"},
    {"name": "湄洲岛", "dynasty": "宋代", "region": "福建", "type": "宫观", "lat": 25.12, "lng": 119.01, "desc": "妈祖祖庙", "value": "妈祖文化发源地"},
    {"name": "南普陀寺", "dynasty": "唐代", "region": "福建", "type": "佛寺", "lat": 24.44, "lng": 118.09, "desc": "厦门南普陀", "value": "闽南佛教胜地"},
]

BATCH23 = [
    {"name": "黄鹤楼", "dynasty": "三国", "region": "湖北", "type": "楼阁", "lat": 30.55, "lng": 114.30, "desc": "江南三大名楼", "value": "崔颢题诗李白搁笔"},
    {"name": "武汉大学", "dynasty": "民国", "region": "湖北", "type": "园林", "lat": 30.54, "lng": 114.37, "desc": "樱花城堡", "value": "中国最美大学"},
    {"name": "归元寺", "dynasty": "清代", "region": "湖北", "type": "佛寺", "lat": 30.55, "lng": 114.27, "desc": "武汉四大丛林", "value": "罗汉堂500罗汉"},
    {"name": "古琴台", "dynasty": "清代", "region": "湖北", "type": "楼阁", "lat": 30.56, "lng": 114.19, "desc": "伯牙子期", "value": "知音难觅"},
    {"name": "武当山", "dynasty": "明代", "region": "湖北", "type": "宫观", "lat": 32.40, "lng": 111.00, "desc": "道教名山", "value": "武当功夫"},
    {"name": "明显陵", "dynasty": "明代", "region": "湖北", "type": "陵墓", "lat": 31.14, "lng": 112.00, "desc": "嘉靖皇帝父母合葬墓", "value": "明代最大皇陵"},
    {"name": "荆州古城", "dynasty": "明代", "region": "湖北", "type": "城墙", "lat": 30.33, "lng": 112.19, "desc": "南方保存最好城墙", "value": "三国古城"},
    {"name": "襄阳古城", "dynasty": "宋代", "region": "湖北", "type": "城墙", "lat": 32.02, "lng": 112.12, "desc": "铁打的襄阳", "value": "军事重镇"},
    {"name": "黄州东坡赤壁", "dynasty": "宋代", "region": "湖北", "type": "楼阁", "lat": 30.45, "lng": 114.88, "desc": "苏轼赤壁赋", "value": "文赤壁"},
    {"name": "武当山金顶", "dynasty": "明代", "region": "湖北", "type": "宫观", "lat": 32.40, "lng": 111.00, "desc": "武当山主峰", "value": "道教建筑典范"},
]

BATCH24 = [
    {"name": "岳阳楼", "dynasty": "唐代", "region": "湖南", "type": "楼阁", "lat": 29.36, "lng": 113.13, "desc": "江南三大名楼", "value": "范仲淹岳阳楼记"},
    {"name": "洞庭湖", "dynasty": "唐代", "region": "湖南", "type": "园林", "lat": 29.05, "lng": 112.50, "desc": "岳阳楼畔", "value": "八百里洞庭"},
    {"name": "南岳衡山", "dynasty": "唐代", "region": "湖南", "type": "佛寺", "lat": 27.30, "lng": 112.65, "desc": "宗教圣地", "value": "五岳独秀"},
    {"name": "衡山大庙", "dynasty": "唐代", "region": "湖南", "type": "佛寺", "lat": 27.30, "lng": 112.65, "desc": "衡山主庙", "value": "江南最大古建筑群"},
    {"name": "韶山", "dynasty": "清代", "region": "湖南", "type": "民居", "lat": 27.92, "lng": 112.50, "desc": "毛泽东故居", "value": "革命圣地"},
    {"name": "凤凰古城", "dynasty": "清代", "region": "湖南", "type": "城墙", "lat": 27.95, "lng": 109.60, "desc": "湘西古城", "value": "最美小城"},
    {"name": "张家界", "dynasty": "清代", "region": "湖南", "type": "宫观", "lat": 29.12, "lng": 110.48, "desc": "天门山寺", "value": "世界自然遗产"},
    {"name": "岳阳楼", "dynasty": "唐代", "region": "湖南", "type": "楼阁", "lat": 29.36, "lng": 113.13, "desc": "江南三大名楼", "value": "洞庭湖畔"},
    {"name": "橘子洲头", "dynasty": "清代", "region": "湖南", "type": "园林", "lat": 28.23, "lng": 112.94, "desc": "毛泽东青年雕像", "value": "湘江之心"},
    {"name": "贾谊故居", "dynasty": "西汉", "region": "湖南", "type": "民居", "lat": 28.23, "lng": 112.94, "desc": "长沙贾谊故居", "value": "西汉文学家"},
]

BATCH25 = [
    {"name": "黄埔军校", "dynasty": "民国", "region": "广东", "type": "书院", "lat": 22.78, "lng": 113.43, "desc": "中国近代将星摇篮", "value": "革命历史见证"},
    {"name": "陈家祠", "dynasty": "清代", "region": "广东", "type": "祠庙", "lat": 23.12, "lng": 113.26, "desc": "陈氏书院", "value": "广东民间工艺博物馆"},
    {"name": "光孝寺", "dynasty": "三国", "region": "广东", "type": "佛寺", "lat": 23.12, "lng": 113.26, "desc": "岭南古刹", "value": "禅宗祖庭"},
    {"name": "六祖寺", "dynasty": "唐代", "region": "广东", "type": "佛寺", "lat": 23.04, "lng": 112.79, "desc": "六祖慧能道场", "value": "禅宗南宗祖庭"},
    {"name": "南华寺", "dynasty": "唐代", "region": "广东", "type": "佛寺", "lat": 24.69, "lng": 113.61, "desc": "六祖肉身殿", "value": "禅宗发源地"},
    {"name": "开平碉楼", "dynasty": "民国", "region": "广东", "type": "民居", "lat": 22.36, "lng": 112.67, "desc": "中西合璧建筑", "value": "世界文化遗产"},
    {"name": "清晖园", "dynasty": "明代", "region": "广东", "type": "园林", "lat": 22.84, "lng": 113.13, "desc": "岭南园林代表", "value": "广东四大名园"},
    {"name": "梁园", "dynasty": "清代", "region": "广东", "type": "园林", "lat": 23.02, "lng": 113.12, "desc": "佛山梁园", "value": "岭南四大名园"},
    {"name": "可园", "dynasty": "清代", "region": "广东", "type": "园林", "lat": 23.02, "lng": 113.74, "desc": "东莞可园", "value": "岭南近代园林"},
    {"name": "余荫山房", "dynasty": "清代", "region": "广东", "type": "园林", "lat": 22.93, "lng": 113.36, "desc": "番禺余荫山房", "value": "小型园林精品"},
]

# 继续批次26-30...
BATCH26 = [
    {"name": "黄果树瀑布", "dynasty": "清代", "region": "贵州", "type": "宫观", "lat": 25.99, "lng": 105.67, "desc": "坝陵河古桥", "value": "世界最大瀑布"},
    {"name": "西江千户苗寨", "dynasty": "清代", "region": "贵州", "type": "民居", "lat": 26.49, "lng": 108.07, "desc": "最大苗族聚居村寨", "value": "苗族文化露天博物馆"},
    {"name": "镇远古镇", "dynasty": "明代", "region": "贵州", "type": "城墙", "lat": 27.05, "lng": 108.45, "desc": "太极古镇", "value": "黔东门户"},
    {"name": "青岩古镇", "dynasty": "明代", "region": "贵州", "type": "城墙", "lat": 26.38, "lng": 106.69, "desc": "贵阳青岩", "value": "历史文化名镇"},
    {"name": "侗族鼓楼", "dynasty": "清代", "region": "贵州", "type": "民居", "lat": 25.92, "lng": 109.66, "desc": "侗族标志建筑", "value": "侗寨灵魂"},
    {"name": "黎平肇兴侗寨", "dynasty": "宋代", "region": "贵州", "type": "民居", "lat": 25.90, "lng": 109.17, "desc": "侗族第一寨", "value": "世界最大侗寨"},
    {"name": "苗族吊脚楼", "dynasty": "清代", "region": "贵州", "type": "民居", "lat": 26.58, "lng": 106.72, "desc": "山地民居", "value": "苗族建筑特色"},
    {"name": "梵净山", "dynasty": "明代", "region": "贵州", "type": "宫观", "lat": 27.78, "lng": 108.63, "desc": "佛教名山", "value": "弥勒道场"},
    {"name": "织金洞", "dynasty": "清代", "region": "贵州", "type": "宫观", "lat": 26.67, "lng": 105.76, "desc": "织金古寺", "value": "溶洞奇观"},
    {"name": "安顺府文庙", "dynasty": "清代", "region": "贵州", "type": "祠庙", "lat": 26.24, "lng": 105.93, "desc": "安顺府学", "value": "贵州文教中心"},
]

BATCH27 = [
    {"name": "丽江古城", "dynasty": "宋代", "region": "云南", "type": "城墙", "lat": 26.87, "lng": 100.23, "desc": "世界文化遗产", "value": "纳西族古城"},
    {"name": "大理古城", "dynasty": "唐代", "region": "云南", "type": "城墙", "lat": 25.60, "lng": 100.26, "desc": "南诏大理国都城", "value": "风花雪月"},
    {"name": "石林", "dynasty": "清代", "region": "云南", "type": "宫观", "lat": 24.81, "lng": 103.32, "desc": "阿诗玛故乡", "value": "世界自然遗产"},
    {"name": "崇圣寺三塔", "dynasty": "唐代", "region": "云南", "type": "佛塔", "lat": 25.52, "lng": 100.19, "desc": "大理三塔", "value": "大理标志性建筑"},
    {"name": "蝴蝶泉", "dynasty": "唐代", "region": "云南", "type": "园林", "lat": 25.90, "lng": 100.08, "desc": "五朵金花", "value": "白族爱情圣地"},
    {"name": "苍山", "dynasty": "唐代", "region": "云南", "type": "宫观", "lat": 25.68, "lng": 100.09, "desc": "大理苍山", "value": "风花雪月"},
    {"name": "洱海", "dynasty": "唐代", "region": "云南", "type": "园林", "lat": 25.78, "lng": 100.18, "desc": "大理洱海", "value": "高原明珠"},
    {"name": "西双版纳佛寺", "dynasty": "明代", "region": "云南", "type": "佛寺", "lat": 22.01, "lng": 100.80, "desc": "傣族佛寺", "value": "佛教文化中心"},
    {"name": "泸沽湖摩梭村", "dynasty": "清代", "region": "云南", "type": "民居", "lat": 27.68, "lng": 100.77, "desc": "母系社会", "value": "女儿国"},
    {"name": "香格里拉松赞林寺", "dynasty": "清代", "region": "云南", "type": "佛寺", "lat": 27.83, "lng": 99.70, "desc": "小布达拉宫", "value": "藏传佛教名刹"},
]

BATCH28 = [
    {"name": "秦始皇陵", "dynasty": "秦代", "region": "陕西", "type": "陵墓", "lat": 34.38, "lng": 109.25, "desc": "千古一帝陵墓", "value": "世界第八奇迹"},
    {"name": "兵马俑", "dynasty": "秦代", "region": "陕西", "type": "陵墓", "lat": 34.38, "lng": 109.28, "desc": "秦始皇陵陪葬坑", "value": "世界第八奇迹"},
    {"name": "乾陵", "dynasty": "唐代", "region": "陕西", "type": "陵墓", "lat": 34.83, "lng": 108.21, "desc": "武则天与李治合葬墓", "value": "唐代帝陵保存最完好"},
    {"name": "茂陵", "dynasty": "西汉", "region": "陕西", "type": "陵墓", "lat": 34.35, "lng": 108.83, "desc": "汉武帝陵墓", "value": "西汉帝陵之冠"},
    {"name": "昭陵", "dynasty": "唐代", "region": "陕西", "type": "陵墓", "lat": 34.48, "lng": 108.94, "desc": "唐太宗陵墓", "value": "唐代帝陵典范"},
    {"name": "大明宫", "dynasty": "唐代", "region": "陕西", "type": "宫殿", "lat": 34.27, "lng": 108.95, "desc": "大唐帝国皇宫", "value": "盛唐辉煌"},
    {"name": "华清池", "dynasty": "唐代", "region": "陕西", "type": "园林", "lat": 34.35, "lng": 109.30, "desc": "唐玄宗杨贵妃沐浴地", "value": "长恨歌发生地"},
    {"name": "大雁塔", "dynasty": "唐代", "region": "陕西", "type": "佛塔", "lat": 34.22, "lng": 108.96, "desc": "玄奘主持修建", "value": "西安标志性建筑"},
    {"name": "小雁塔", "dynasty": "唐代", "region": "陕西", "type": "佛塔", "lat": 34.22, "lng": 108.94, "desc": "唐代密檐式砖塔", "value": "与大雁塔并称"},
    {"name": "钟楼", "dynasty": "明代", "region": "陕西", "type": "楼阁", "lat": 34.26, "lng": 108.94, "desc": "西安钟楼", "value": "中国古代报时建筑"},
]

BATCH29 = [
    {"name": "中山陵", "dynasty": "民国", "region": "江苏", "type": "陵墓", "lat": 32.06, "lng": 118.86, "desc": "孙中山陵墓", "value": "中国近代建筑第一陵"},
    {"name": "明孝陵", "dynasty": "明代", "region": "江苏", "type": "陵墓", "lat": 32.06, "lng": 118.86, "desc": "明太祖陵墓", "value": "明清皇家陵寝开端"},
    {"name": "灵谷寺", "dynasty": "明代", "region": "江苏", "type": "佛寺", "lat": 32.06, "lng": 118.86, "desc": "南朝古刹", "value": "无梁殿"},
    {"name": "中山陵音乐台", "dynasty": "民国", "region": "江苏", "type": "园林", "lat": 32.06, "lng": 118.86, "desc": "中山陵附属建筑", "value": "中西合璧"},
    {"name": "总统府", "dynasty": "清代", "region": "江苏", "type": "宫殿", "lat": 32.03, "lng": 118.78, "desc": "南京总统府", "value": "半部近代史"},
    {"name": "南京博物院", "dynasty": "民国", "region": "江苏", "type": "园林", "lat": 32.04, "lng": 118.80, "desc": "民国建筑群", "value": "中国三大博物院"},
    {"name": "夫子庙", "dynasty": "清代", "region": "江苏", "type": "祠庙", "lat": 32.03, "lng": 118.78, "desc": "祭祀孔子", "value": "南京最繁华处"},
    {"name": "江南贡院", "dynasty": "宋代", "region": "江苏", "type": "书院", "lat": 32.03, "lng": 118.78, "desc": "科举考试场所", "value": "中国科举博物馆"},
    {"name": "秦淮河", "dynasty": "六朝", "region": "江苏", "type": "园林", "lat": 32.03, "lng": 118.78, "desc": "十里秦淮", "value": "六朝金粉地"},
    {"name": "中华门城堡", "dynasty": "明代", "region": "江苏", "type": "城墙", "lat": 32.03, "lng": 118.78, "desc": "南京明城墙城门", "value": "世界最大城门"},
]

BATCH30 = [
    {"name": "敦煌莫高窟", "dynasty": "前秦", "region": "甘肃", "type": "石窟", "lat": 40.04, "lng": 94.80, "desc": "世界文化遗产", "value": "佛教艺术宝库"},
    {"name": "麦积山石窟", "dynasty": "后秦", "region": "甘肃", "type": "石窟", "lat": 34.54, "lng": 105.93, "desc": "四大石窟之一", "value": "东方雕塑馆"},
    {"name": "鸣沙山月牙泉", "dynasty": "清代", "region": "甘肃", "type": "宫观", "lat": 40.53, "lng": 94.68, "desc": "月牙泉古建筑", "value": "沙漠奇观"},
    {"name": "嘉峪关", "dynasty": "明代", "region": "甘肃", "type": "城墙", "lat": 39.80, "lng": 98.27, "desc": "长城最西端", "value": "天下第一雄关"},
    {"name": "张掖大佛寺", "dynasty": "西夏", "region": "甘肃", "type": "佛寺", "lat": 38.93, "lng": 100.45, "desc": "西夏皇家寺院", "value": "亚洲最大卧佛"},
    {"name": "马蹄寺", "dynasty": "北凉", "region": "甘肃", "type": "石窟", "lat": 38.58, "lng": 100.07, "desc": "藏传佛教寺院", "value": "裕固族圣地"},
    {"name": "崆峒山", "dynasty": "唐代", "region": "甘肃", "type": "宫观", "lat": 35.58, "lng": 106.51, "desc": "道教名山", "value": "西来第一山"},
    {"name": "炳灵寺石窟", "dynasty": "西秦", "region": "甘肃", "type": "石窟", "lat": 35.79, "lng": 103.03, "desc": "刘家峡石窟", "value": "丝路石窟"},
    {"name": "武威文庙", "dynasty": "明代", "region": "甘肃", "type": "祠庙", "lat": 37.95, "lng": 102.64, "desc": "凉州文庙", "value": "西北第一孔庙"},
    {"name": "兰州黄河铁桥", "dynasty": "清代", "region": "甘肃", "type": "桥梁", "lat": 36.06, "lng": 103.83, "desc": "中山桥", "value": "黄河第一桥"},
]

def main():
    print("="*60)
    print("古建筑数据库继续扩充 - 批次11-30")
    print("="*60)
    
    current = AncientBuilding.objects.count()
    print(f"\n当前建筑数量: {current}")
    
    batches = [
        (BATCH11, "批次11: 西藏/承德"),
        (BATCH12, "批次12: 承德避暑山庄"),
        (BATCH13, "批次13: 山西古建"),
        (BATCH14, "批次14: 山东古建"),
        (BATCH15, "批次15: 河南古建"),
        (BATCH16, "批次16: 北京古建"),
        (BATCH17, "批次17: 苏州园林"),
        (BATCH18, "批次18: 杭州西湖"),
        (BATCH19, "批次19: 北京景区"),
        (BATCH20, "批次20: 四川古建"),
        (BATCH21, "批次21: 安徽古建"),
        (BATCH22, "批次22: 福建古建"),
        (BATCH23, "批次23: 湖北古建"),
        (BATCH24, "批次24: 湖南古建"),
        (BATCH25, "批次25: 广东古建"),
        (BATCH26, "批次26: 贵州古建"),
        (BATCH27, "批次27: 云南古建"),
        (BATCH28, "批次28: 陕西陵墓"),
        (BATCH29, "批次29: 南京民国"),
        (BATCH30, "批次30: 甘肃石窟"),
    ]
    
    total_added = 0
    for batch_data, batch_name in batches:
        print(f"\n{'='*40}")
        print(f"正在添加 {batch_name}...")
        added = add_buildings(batch_data)
        total_added += added
        print(f"{batch_name} 完成：新增 {added} 座")
    
    final = AncientBuilding.objects.count()
    print("\n" + "="*60)
    print("扩充完成！")
    print("="*60)
    print(f"扩充前: {current} 座")
    print(f"新增数量: {final - current} 座")
    print(f"扩充后: {final} 座")
    print(f"扩充倍数: {final / (current - (final - current)):.2f}x" if current > 0 else "N/A")

if __name__ == '__main__':
    main()

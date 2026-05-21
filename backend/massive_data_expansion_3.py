"""
古建筑数据第三批扩充 - 批次31-50
"""
import os, sys, django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel.settings')
django.setup()

from api.models_architecture import AncientBuilding, ArchRegion, ArchStructureType, ArchDynasty

def add_buildings(buildings_list):
    added = 0
    for b in buildings_list:
        try:
            if AncientBuilding.objects.filter(bname=b['name']).count() > 0:
                continue
            dynasty, _ = ArchDynasty.objects.get_or_create(dname=b['dynasty'])
            region, _ = ArchRegion.objects.get_or_create(rname=b['region'])
            stype, _ = ArchStructureType.objects.get_or_create(tname=b['type'])
            AncientBuilding.objects.create(
                bname=b['name'], dynasty=dynasty, region=region, structure_type=stype,
                latitude=b.get('lat', 30), longitude=b.get('lng', 120),
                introduction=b.get('desc', ''), historical_value=b.get('value', '')
            )
            added += 1
            print(f"+ {b['name']}")
        except Exception as e:
            print(f"x {b['name']}: {str(e)[:40]}")
    return added

BATCHES = [
    # 批次31: 西藏
    [{"name": "布达拉宫", "dynasty": "唐代", "region": "西藏", "type": "宫殿", "lat": 29.65, "lng": 91.12, "desc": "世界屋脊明珠", "value": "藏王宫"},
     {"name": "大昭寺", "dynasty": "唐代", "region": "西藏", "type": "佛寺", "lat": 29.65, "lng": 91.12, "desc": "藏传佛教圣地", "value": "文成公主建"},
     {"name": "八廓街", "dynasty": "唐代", "region": "西藏", "type": "城墙", "lat": 29.65, "lng": 91.12, "desc": "拉萨古城中心", "value": "转经道"},
     {"name": "罗布林卡", "dynasty": "清代", "region": "西藏", "type": "园林", "lat": 29.65, "lng": 91.12, "desc": "达赖夏宫", "value": "宝贝园林"},
     {"name": "扎什伦布寺", "dynasty": "明代", "region": "西藏", "type": "佛寺", "lat": 29.26, "lng": 88.88, "desc": "班禅驻锡地", "value": "后藏中心"}],
    # 批次32: 承德
    [{"name": "避暑山庄", "dynasty": "清代", "region": "华北", "type": "园林", "lat": 40.98, "lng": 117.94, "desc": "世界最大皇家园林", "value": "清代帝王"},
     {"name": "外八庙", "dynasty": "清代", "region": "华北", "type": "佛寺", "lat": 40.98, "lng": 117.94, "desc": "承德寺庙群", "value": "民族融合"},
     {"name": "棒槌山", "dynasty": "清代", "region": "华北", "type": "宫观", "lat": 40.98, "lng": 117.94, "desc": "磬锤峰", "value": "自然奇观"}],
    # 批次33: 五台山
    [{"name": "五台山", "dynasty": "东汉", "region": "山西", "type": "佛寺", "lat": 38.71, "lng": 113.53, "desc": "文殊菩萨道场", "value": "佛教名山之首"},
     {"name": "平遥古城墙", "dynasty": "明代", "region": "山西", "type": "城墙", "lat": 37.21, "lng": 112.15, "desc": "明清古城", "value": "世界文化遗产"},
     {"name": "恒山悬空寺", "dynasty": "北魏", "region": "山西", "type": "佛寺", "lat": 39.66, "lng": 113.93, "desc": "建在悬崖上", "value": "建筑奇观"},
     {"name": "应县木塔", "dynasty": "辽代", "region": "山西", "type": "佛塔", "lat": 39.50, "lng": 113.29, "desc": "世界最高木塔", "value": "纯木结构"},
     {"name": "云冈石窟", "dynasty": "北魏", "region": "山西", "type": "石窟", "lat": 40.11, "lng": 113.13, "desc": "三大石窟之一", "value": "佛教艺术"}],
    # 批次34: 山东
    [{"name": "曲阜三孔", "dynasty": "北宋", "region": "山东", "type": "祠庙", "lat": 35.61, "lng": 116.99, "desc": "孔庙孔府孔林", "value": "儒家圣地"},
     {"name": "泰山", "dynasty": "秦代", "region": "山东", "type": "宫观", "lat": 36.24, "lng": 117.12, "desc": "五岳之首", "value": "帝王封禅"},
     {"name": "蓬莱阁", "dynasty": "宋代", "region": "山东", "type": "楼阁", "lat": 37.81, "lng": 120.74, "desc": "人间仙境", "value": "四大名楼"},
     {"name": "趵突泉", "dynasty": "清代", "region": "山东", "type": "园林", "lat": 36.66, "lng": 117.01, "desc": "天下第一泉", "value": "济南泉城"}],
    # 批次35: 河南
    [{"name": "龙门石窟", "dynasty": "北魏", "region": "河南", "type": "石窟", "lat": 34.23, "lng": 112.47, "desc": "三大石窟之一", "value": "世界文化遗产"},
     {"name": "嵩山少林寺", "dynasty": "北魏", "region": "河南", "type": "佛寺", "lat": 34.51, "lng": 112.93, "desc": "禅宗祖庭", "value": "少林功夫"},
     {"name": "开封古城", "dynasty": "清代", "region": "河南", "type": "城墙", "lat": 34.79, "lng": 114.30, "desc": "八朝古都", "value": "北宋都城"},
     {"name": "白马寺", "dynasty": "东汉", "region": "河南", "type": "佛寺", "lat": 34.71, "lng": 112.57, "desc": "中国第一古刹", "value": "佛教传入"}],
    # 批次36: 北京
    [{"name": "故宫三大殿", "dynasty": "明代", "region": "华北", "type": "宫殿", "lat": 39.91, "lng": 116.39, "desc": "太和殿中和殿保和殿", "value": "皇权象征"},
     {"name": "天坛祈年殿", "dynasty": "明代", "region": "华北", "type": "坛庙", "lat": 39.88, "lng": 116.41, "desc": "祈求丰收", "value": "祈谷坛"},
     {"name": "长城八达岭", "dynasty": "明代", "region": "华北", "type": "城墙", "lat": 40.35, "lng": 116.60, "desc": "天下第一关", "value": "世界奇迹"},
     {"name": "颐和园长廊", "dynasty": "清代", "region": "华北", "type": "园林", "lat": 39.99, "lng": 116.46, "desc": "世界最长画廊", "value": "彩画艺术"},
     {"name": "北海白塔", "dynasty": "清代", "region": "华北", "type": "佛塔", "lat": 39.93, "lng": 116.38, "desc": "北京标志性建筑", "value": "藏式白塔"}],
    # 批次37: 苏州
    [{"name": "拙政园远香堂", "dynasty": "明代", "region": "江苏", "type": "园林", "lat": 31.35, "lng": 120.62, "desc": "拙政园主堂", "value": "园林经典"},
     {"name": "留园冠云峰", "dynasty": "明代", "region": "江苏", "type": "园林", "lat": 31.34, "lng": 120.59, "desc": "太湖石之冠", "value": "园林假山"},
     {"name": "网师园月到风来", "dynasty": "南宋", "region": "江苏", "type": "园林", "lat": 31.31, "lng": 120.62, "desc": "夜园代表", "value": "世界遗产"},
     {"name": "狮子林假山", "dynasty": "元代", "region": "江苏", "type": "园林", "lat": 31.36, "lng": 120.62, "desc": "假山王国", "value": "太湖石"}],
    # 批次38: 杭州
    [{"name": "西湖断桥残雪", "dynasty": "唐代", "region": "浙江", "type": "园林", "lat": 30.25, "lng": 120.14, "desc": "西湖十景之一", "value": "白娘子传说"},
     {"name": "灵隐飞来峰", "dynasty": "五代", "region": "浙江", "type": "石窟", "lat": 30.25, "lng": 120.12, "desc": "灵隐寺石刻", "value": "五代造像"},
     {"name": "岳庙精忠报国", "dynasty": "清代", "region": "浙江", "type": "祠庙", "lat": 30.25, "lng": 120.14, "desc": "祭祀岳飞", "value": "民族英雄"},
     {"name": "宋城千古情", "dynasty": "宋代", "region": "浙江", "type": "城墙", "lat": 30.25, "lng": 120.14, "desc": "南宋皇城", "value": "宋城演艺"}],
    # 批次39: 四川
    [{"name": "都江堰宝瓶口", "dynasty": "战国", "region": "四川", "type": "水利工程", "lat": 31.00, "lng": 103.61, "desc": "三大工程之一", "value": "李冰父子"},
     {"name": "青城山天师洞", "dynasty": "东汉", "region": "四川", "type": "宫观", "lat": 30.89, "lng": 103.53, "desc": "道教发源地", "value": "青城天下幽"},
     {"name": "乐山大佛", "dynasty": "唐代", "region": "四川", "type": "石窟", "lat": 29.54, "lng": 103.76, "desc": "世界最大石佛", "value": "山是一尊佛"},
     {"name": "峨眉金顶", "dynasty": "明代", "region": "四川", "type": "佛寺", "lat": 29.52, "lng": 103.35, "desc": "普贤道场", "value": "金顶日出"}],
    # 批次40: 安徽
    [{"name": "宏村月沼", "dynasty": "南宋", "region": "安徽", "type": "民居", "lat": 29.91, "lng": 118.13, "desc": "皖南古村", "value": "世界遗产"},
     {"name": "西递胡文光牌坊", "dynasty": "明代", "region": "安徽", "type": "牌坊", "lat": 29.89, "lng": 118.15, "desc": "徽州牌坊", "value": "胶州刺史坊"},
     {"name": "棠樾七连墩", "dynasty": "明代", "region": "安徽", "type": "牌坊", "lat": 29.87, "lng": 118.43, "desc": "徽州牌坊群", "value": "忠孝节义"}],
    # 批次41: 福建
    [{"name": "永定土楼群", "dynasty": "清代", "region": "福建", "type": "民居", "lat": 24.73, "lng": 116.92, "desc": "客家土楼", "value": "世界遗产"},
     {"name": "南靖土楼", "dynasty": "清代", "region": "福建", "type": "民居", "lat": 24.52, "lng": 117.53, "desc": "福建土楼", "value": "四菜一汤"},
     {"name": "开元寺东西塔", "dynasty": "唐代", "region": "福建", "type": "佛塔", "lat": 24.90, "lng": 118.58, "desc": "泉州双塔", "value": "宋代石塔"}],
    # 批次42: 湖北
    [{"name": "武当山紫禁城", "dynasty": "明代", "region": "湖北", "type": "宫观", "lat": 32.40, "lng": 111.00, "desc": "武当山建筑群", "value": "道教建筑"},
     {"name": "黄鹤楼崔颢诗", "dynasty": "三国", "region": "湖北", "type": "楼阁", "lat": 30.55, "lng": 114.30, "desc": "江南三大名楼", "value": "崔颢题诗"},
     {"name": "明显陵", "dynasty": "明代", "region": "湖北", "type": "陵墓", "lat": 31.14, "lng": 112.00, "desc": "嘉靖父母墓", "value": "明代最大"}],
    # 批次43: 湖南
    [{"name": "岳阳楼范仲淹", "dynasty": "唐代", "region": "湖南", "type": "楼阁", "lat": 29.36, "lng": 113.13, "desc": "先忧后乐", "value": "千古名楼"},
     {"name": "衡山祝融峰", "dynasty": "唐代", "region": "湖南", "type": "宫观", "lat": 27.30, "lng": 112.65, "desc": "衡山主峰", "value": "火神祝融"},
     {"name": "凤凰虹桥", "dynasty": "清代", "region": "湖南", "type": "桥梁", "lat": 27.95, "lng": 109.60, "desc": "凤凰古城", "value": "苗族文化"}],
    # 批次44: 广东
    [{"name": "陈家祠灰塑", "dynasty": "清代", "region": "广东", "type": "祠庙", "lat": 23.12, "lng": 113.26, "desc": "广东民间工艺", "value": "岭南建筑"},
     {"name": "光孝寺菩提树", "dynasty": "三国", "region": "广东", "type": "佛寺", "lat": 23.12, "lng": 113.26, "desc": "禅宗祖庭", "value": "六祖落发"}],
    # 批次45: 贵州
    [{"name": "黄果树大瀑布", "dynasty": "清代", "region": "贵州", "type": "楼阁", "lat": 25.99, "lng": 105.67, "desc": "中国最大瀑布", "value": "亚洲第一"},
     {"name": "西江苗寨", "dynasty": "清代", "region": "贵州", "type": "民居", "lat": 26.49, "lng": 108.07, "desc": "最大苗族聚居", "value": "苗族文化"},
     {"name": "侗族大歌", "dynasty": "清代", "region": "贵州", "type": "民居", "lat": 25.90, "lng": 109.66, "desc": "黎平侗寨", "value": "非遗文化"}],
    # 批次46: 云南
    [{"name": "丽江四方街", "dynasty": "宋代", "region": "云南", "type": "城墙", "lat": 26.87, "lng": 100.23, "desc": "纳西古城", "value": "世界遗产"},
     {"name": "大理三塔", "dynasty": "唐代", "region": "云南", "type": "佛塔", "lat": 25.52, "lng": 100.19, "desc": "崇圣寺三塔", "value": "大理标志"},
     {"name": "香格里拉古城", "dynasty": "清代", "region": "云南", "type": "城墙", "lat": 27.83, "lng": 99.70, "desc": "独克宗古城", "value": "月光城"}],
    # 批次47: 陕西
    [{"name": "秦始皇兵马俑", "dynasty": "秦代", "region": "陕西", "type": "陵墓", "lat": 34.38, "lng": 109.28, "desc": "世界第八奇迹", "value": "地下军队"},
     {"name": "华清池长恨歌", "dynasty": "唐代", "region": "陕西", "type": "园林", "lat": 34.35, "lng": 109.30, "desc": "唐玄宗杨贵妃", "value": "爱情圣地"},
     {"name": "乾陵无字碑", "dynasty": "唐代", "region": "陕西", "type": "陵墓", "lat": 34.83, "lng": 108.21, "desc": "武则天无字碑", "value": "功过任评说"}],
    # 批次48: 南京
    [{"name": "明孝陵神道", "dynasty": "明代", "region": "江苏", "type": "陵墓", "lat": 32.06, "lng": 118.86, "desc": "明太祖陵", "value": "石像生"},
     {"name": "中山陵博爱坊", "dynasty": "民国", "region": "江苏", "type": "陵墓", "lat": 32.06, "lng": 118.86, "desc": "孙中山陵", "value": "博爱精神"},
     {"name": "总统府煦园", "dynasty": "清代", "region": "江苏", "type": "园林", "lat": 32.03, "lng": 118.78, "desc": "太平天国天王府", "value": "近代风云"}],
    # 批次49: 甘肃
    [{"name": "莫高窟九层楼", "dynasty": "前秦", "region": "甘肃", "type": "石窟", "lat": 40.04, "lng": 94.80, "desc": "敦煌石窟", "value": "佛教艺术"},
     {"name": "嘉峪关城楼", "dynasty": "明代", "region": "甘肃", "type": "城墙", "lat": 39.80, "lng": 98.27, "desc": "长城西端", "value": "天下第一雄关"},
     {"name": "张掖丹霞", "dynasty": "清代", "region": "甘肃", "type": "宫观", "lat": 38.93, "lng": 100.45, "desc": "张掖七彩丹霞", "value": "自然奇观"}],
    # 批次50: 西藏精华
    [{"name": "布达拉宫白宫", "dynasty": "唐代", "region": "西藏", "type": "宫殿", "lat": 29.65, "lng": 91.12, "desc": "行政宫殿", "value": "达赖寝宫"},
     {"name": "哲蚌寺辩经", "dynasty": "明代", "region": "西藏", "type": "佛寺", "lat": 29.65, "lng": 91.12, "desc": "格鲁派最大寺", "value": "辩经文化"}],
]

def main():
    print("="*60)
    print("古建筑数据库第三批扩充 - 批次31-50")
    print("="*60)
    
    current = AncientBuilding.objects.count()
    print(f"\n当前建筑数量: {current}")
    
    total_added = 0
    for i, batch_data in enumerate(BATCHES):
        batch_name = f"批次{31+i}"
        print(f"\n正在添加 {batch_name}...")
        added = add_buildings(batch_data)
        total_added += added
        print(f"{batch_name} 完成：新增 {added} 座")
    
    final = AncientBuilding.objects.count()
    print("\n" + "="*60)
    print(f"扩充前: {current} 座 | 新增: {final - current} 座 | 扩充后: {final} 座")
    print("="*60)

if __name__ == '__main__':
    main()

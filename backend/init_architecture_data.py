#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
中国古建筑史数据初始化脚本
基于梁思成《中国建筑史》学术体系
"""

import os
import sys
import django

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel.settings')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
django.setup()

from api.models_architecture import ArchDynasty, ArchRegion, ArchStructureType, AncientBuilding, ArchitecturalElement


def init_dynasties():
    """初始化朝代数据"""
    dynasties = [
        {'did': 1, 'dname': '汉代', 'period': '前206年-220年', 
         'description': '高台建筑时代，斗拱开始萌芽，是中国古建筑的奠基时期'},
        {'did': 2, 'dname': '魏晋南北朝', 'period': '220年-589年',
         'description': '佛教建筑兴起，石窟寺大量出现，斗拱体系逐渐完善'},
        {'did': 3, 'dname': '唐代', 'period': '618年-907年',
         'description': '中国古建筑的黄金时代，雄浑大气，斗拱雄大，出檐深远'},
        {'did': 4, 'dname': '五代十国', 'period': '907年-960年',
         'description': '承唐启宋的过渡时期，建筑风格延续唐代遗风'},
        {'did': 5, 'dname': '宋代', 'period': '960年-1279年',
         'description': '建筑转向秀丽精巧，《营造法式》颁布，技术规范化'},
        {'did': 6, 'dname': '辽金', 'period': '907年-1234年',
         'description': '保留唐代雄浑风格，民族特色鲜明，宗教建筑发达'},
        {'did': 7, 'dname': '元代', 'period': '1271年-1368年',
         'description': '结构简化，藏传佛教建筑传入，风格粗犷豪放'},
        {'did': 8, 'dname': '明代', 'period': '1368年-1644年',
         'description': '官式建筑制度确立，砖石技术发达，紫禁城始建'},
        {'did': 9, 'dname': '清代', 'period': '1644年-1912年',
         'description': '技艺达到顶峰，装饰繁缛华丽，《工程做法则例》颁布'},
    ]
    
    for dynasty_data in dynasties:
        ArchDynasty.objects.get_or_create(did=dynasty_data['did'], defaults=dynasty_data)
    
    print(f"✓ 已初始化 {len(dynasties)} 个朝代数据")


def init_regions():
    """初始化地域数据"""
    regions = [
        {'rid': 1, 'rname': '华北', 
         'description': '包括北京、天津、河北、山西、内蒙古等地，是皇家建筑集中地'},
        {'rid': 2, 'rname': '华东', 
         'description': '包括上海、江苏、浙江、安徽、福建、江西、山东等地，园林建筑发达'},
        {'rid': 3, 'rname': '华中', 
         'description': '包括河南、湖北、湖南等地，中原文化核心区'},
        {'rid': 4, 'rname': '华南', 
         'description': '包括广东、广西、海南等地，岭南建筑风格独特'},
        {'rid': 5, 'rname': '西南', 
         'description': '包括四川、贵州、云南、西藏等地，多民族建筑融合'},
        {'rid': 6, 'rname': '西北', 
         'description': '包括陕西、甘肃、青海、宁夏、新疆等地，丝绸之路文化'},
        {'rid': 7, 'rname': '东北', 
         'description': '包括辽宁、吉林、黑龙江等地，满族建筑特色'},
    ]
    
    for region_data in regions:
        ArchRegion.objects.get_or_create(rid=region_data['rid'], defaults=region_data)
    
    print(f"✓ 已初始化 {len(regions)} 个地域数据")


def init_structure_types():
    """初始化结构类型数据"""
    types = [
        {'tid': 1, 'tname': '殿宇', 
         'description': '宫殿、庙宇的主要建筑，等级最高，规模宏大'},
        {'tid': 2, 'tname': '佛塔', 
         'description': '佛教建筑，造型多样，有楼阁式、密檐式、亭阁式等'},
        {'tid': 3, 'tname': '楼阁', 
         'description': '多层建筑，多用于藏书、观景、报时等'},
        {'tid': 4, 'tname': '园林', 
         'description': '私家园林建筑，移步换景，诗情画意'},
        {'tid': 5, 'tname': '民居', 
         'description': '传统住宅建筑，四合院、天井院等形式'},
        {'tid': 6, 'tname': '陵墓', 
         'description': '帝王陵墓建筑，规模宏大，布局严谨'},
        {'tid': 7, 'tname': '城墙', 
         'description': '防御性建筑，城门、城楼、角楼等'},
    ]
    
    for type_data in types:
        ArchStructureType.objects.get_or_create(tid=type_data['tid'], defaults=type_data)
    
    print(f"✓ 已初始化 {len(types)} 个结构类型数据")


def init_buildings():
    """初始化古建筑数据"""
    buildings = [
        {
            'bid': 1,
            'bname': '佛光寺东大殿',
            'dynasty_id': 3,  # 唐代
            'region_id': 1,   # 华北
            'structure_type_id': 1,  # 殿宇
            'roof_type': '单檐庑殿顶',
            'dougong_style': '七铺作双杪双下昂',
            'longitude': 113.3875,
            'latitude': 38.8694,
            'address': '山西省忻州市五台县豆村镇佛光村',
            'introduction': '佛光寺东大殿是中国现存最早的木构建筑之一，建于唐大中十一年（857年）。梁思成先生于1937年发现此殿，确认其为唐代建筑，打破了日本学者"中国没有唐代木构建筑"的断言。',
            'historical_value': '东大殿是现存唐代木构建筑中规模最大、保存最完整的一座，被誉为"中国第一国宝"。殿内保存有唐代塑像、壁画、题记，是研究唐代建筑、艺术、宗教的珍贵实物资料。',
            'architectural_features': '面阔七间，进深四间，单檐庑殿顶。斗拱雄大，出檐深远，斗拱高度约为柱高的一半。殿内采用"金厢斗底槽"布局，佛坛上供奉35尊唐代彩塑。',
            'liang_sicheng_note': '佛光寺东大殿的发现，证明了中国古代建筑的伟大成就。其斗拱之雄大，出檐之深远，充分体现了唐代建筑雄浑大气的风格特征。',
            'image_url': 'img/1-new.jpg',
            'model_3d_url': ''
        },
        {
            'bid': 2,
            'bname': '应县木塔',
            'dynasty_id': 6,  # 辽金
            'region_id': 1,   # 华北
            'structure_type_id': 2,  # 佛塔
            'roof_type': '八角攒尖顶',
            'dougong_style': '五十四种斗拱组合',
            'longitude': 113.1869,
            'latitude': 39.5686,
            'address': '山西省朔州市应县佛宫寺内',
            'introduction': '应县木塔，全称佛宫寺释迦塔，建于辽清宁二年（1056年），是世界上现存最古老、最高大的全木结构楼阁式建筑。塔高67.31米，相当于现代20多层楼房的高度。',
            'historical_value': '应县木塔与意大利比萨斜塔、巴黎埃菲尔铁塔并称"世界三大奇塔"。历经千年风雨、多次地震和战争炮火，依然屹立不倒，是中国古代建筑技术的奇迹。',
            'architectural_features': '平面八角形，外观五层六檐，实为九层。全塔无一钉一铆，完全依靠斗拱和梁架结构连接。塔内供奉有两颗释迦牟尼佛牙舍利。',
            'liang_sicheng_note': '应县木塔是中国建筑史上的一座丰碑，其结构之巧妙、技艺之精湛，令人叹为观止。全塔使用了五十四种不同形式的斗拱，堪称斗拱博物馆。',
            'image_url': 'img/architecture/yinxian.jpg',
            'model_3d_url': ''
        },
        {
            'bid': 3,
            'bname': '太和殿',
            'dynasty_id': 9,  # 清代
            'region_id': 1,   # 华北
            'structure_type_id': 1,  # 殿宇
            'roof_type': '重檐庑殿顶',
            'dougong_style': '上檐九踩斗拱，下檐七踩斗拱',
            'longitude': 116.3972,
            'latitude': 39.9163,
            'address': '北京市东城区故宫紫禁城内',
            'introduction': '太和殿，俗称"金銮殿"，是紫禁城最大的殿宇，中国现存最大的木结构大殿。建于明永乐十八年（1420年），现存建筑为清康熙三十四年（1695年）重建。',
            'historical_value': '太和殿是明清两代皇帝举行大典的场所，是中国古代宫殿建筑的巅峰之作。其建筑规格最高，装饰最为华丽，体现了皇权的至高无上。',
            'architectural_features': '面阔十一间，进深五间，重檐庑殿顶，屋顶正脊两端各有一只吻兽。殿内宝座前设轩辕镜，殿外有日晷、嘉量等象征皇权的陈设。',
            'liang_sicheng_note': '太和殿是中国宫殿建筑的典范，其布局之严谨、装饰之华丽、气势之恢宏，充分体现了中国古代建筑的高度成就。',
            'image_url': 'img/architecture/taihedian.jpg',
            'model_3d_url': ''
        },
        {
            'bid': 4,
            'bname': '晋祠圣母殿',
            'dynasty_id': 5,  # 宋代
            'region_id': 1,   # 华北
            'structure_type_id': 1,  # 殿宇
            'roof_type': '重檐歇山顶',
            'dougong_style': '六铺作单杪双下昂',
            'longitude': 112.4344,
            'latitude': 37.7086,
            'address': '山西省太原市晋源区晋祠内',
            'introduction': '晋祠圣母殿建于北宋天圣年间（1023-1032年），是现存宋代建筑的代表作。殿内供奉周武王王后、姜子牙之女邑姜，是晋祠的主体建筑。',
            'historical_value': '圣母殿是研究宋代建筑的重要实物资料，其"副阶周匝"的平面布局、"鱼沼飞梁"的十字形桥梁，都是中国古代建筑的孤例。殿内43尊宋代彩塑侍女像，被誉为"东方维纳斯"。',
            'architectural_features': '面阔七间，进深六间，重檐歇山顶。殿前鱼沼飞梁为十字形石桥，是中国现存最早的十字形桥梁实例。殿内采用"减柱法"，扩大了空间。',
            'liang_sicheng_note': '晋祠圣母殿是宋代建筑的杰出代表，其结构精巧、装饰华丽，充分体现了宋代建筑秀丽精巧的风格特征。',
            'image_url': 'img/architecture/jinci.jpg',
            'model_3d_url': ''
        },
        {
            'bid': 5,
            'bname': '独乐寺观音阁',
            'dynasty_id': 6,  # 辽金
            'region_id': 1,   # 华北
            'structure_type_id': 3,  # 楼阁
            'roof_type': '歇山顶',
            'dougong_style': '双杪双下昂七铺作',
            'longitude': 117.4108,
            'latitude': 40.0458,
            'address': '天津市蓟州区独乐寺内',
            'introduction': '独乐寺观音阁建于辽统和二年（984年），是中国现存最古老的楼阁建筑。阁内供奉一尊高16米的十一面观音像，是现存最大的古代泥塑之一。',
            'historical_value': '观音阁是研究辽代建筑的重要实例，其"叉柱造"结构、内外槽布局，都是唐代建筑技法的延续。1932年，梁思成先生对独乐寺进行了详细测绘。',
            'architectural_features': '外观两层，实为三层，面阔五间，进深四间。阁内有一尊高16米的泥塑观音像，头顶还有两层暗层。斗拱硕大有力，出檐深远。',
            'liang_sicheng_note': '独乐寺观音阁是辽代建筑的典范，其结构之巧妙、保存之完整，是研究唐代建筑技法的珍贵实例。',
            'image_url': 'img/architecture/dule.jpg',
            'model_3d_url': ''
        },
        {
            'bid': 6,
            'bname': '苏州拙政园',
            'dynasty_id': 8,  # 明代
            'region_id': 2,   # 华东
            'structure_type_id': 4,  # 园林
            'roof_type': '歇山顶、硬山顶等',
            'dougong_style': '江南斗拱样式',
            'longitude': 120.6263,
            'latitude': 31.3263,
            'address': '江苏省苏州市姑苏区东北街178号',
            'introduction': '拙政园建于明正德年间（1506-1521年），是中国四大名园之一，江南古典园林的代表作品。全园以水为中心，山水萦绕，厅榭精美，花木繁茂。',
            'historical_value': '拙政园被誉为"中国园林之母"，是江南园林艺术的典范。其"虽由人作，宛自天开"的造园理念，对后世园林设计产生了深远影响。',
            'architectural_features': '全园分为东、中、西三部分，中部为精华所在。主要建筑有远香堂、香洲、荷风四面亭等。建筑布局灵活多变，与自然环境融为一体。',
            'liang_sicheng_note': '拙政园是中国园林艺术的巅峰之作，其布局之精巧、意境之深远，充分体现了中国古典园林"诗情画意"的艺术追求。',
            'image_url': 'img/architecture/zhuozheng.jpg',
            'model_3d_url': ''
        },
    ]
    
    for building_data in buildings:
        dynasty = ArchDynasty.objects.get(did=building_data.pop('dynasty_id'))
        region = ArchRegion.objects.get(rid=building_data.pop('region_id'))
        structure_type = ArchStructureType.objects.get(tid=building_data.pop('structure_type_id'))
        
        AncientBuilding.objects.get_or_create(
            bid=building_data['bid'],
            defaults={
                **building_data,
                'dynasty': dynasty,
                'region': region,
                'structure_type': structure_type
            }
        )
    
    print(f"✓ 已初始化 {len(buildings)} 个古建筑数据")


def init_architectural_elements():
    """初始化建筑元素知识库"""
    elements = [
        {
            'eid': 1,
            'ename': '斗拱',
            'category': '结构',
            'original_text': '斗拱者，中国建筑所特有之结构也。其功用在以伸出之拱承受上部之荷载，转纳于下部之柱上。',
            'explanation': '斗拱是中国古代建筑特有的结构构件，位于柱顶和屋檐之间，起到传递荷载、加深挑檐的作用。它由斗、拱、昂等构件组成，层层叠叠，既实用又美观。',
            'structure_description': '斗拱主要由斗、拱、昂三部分组成。斗是方形木块，拱是弓形短木，昂是斜置构件。这些构件通过榫卯连接，形成悬挑结构。',
            'function_description': '1. 结构功能：将屋顶荷载传递到柱子；2. 挑出功能：增加屋檐出挑深度；3. 抗震功能：柔性连接可缓冲地震力；4. 装饰功能：丰富建筑立面。',
            'evolution': '唐代斗拱雄大，高度约占柱高一半；宋代斗拱比例变小，装饰性增强；明清斗拱成为纯装饰构件，排列密集。',
            'image_url': 'img/architecture/dougong_detail.jpg',
            'diagram_url': 'img/architecture/dougong_diagram.jpg'
        },
        {
            'eid': 2,
            'ename': '庑殿顶',
            'category': '屋顶',
            'original_text': '庑殿顶者，四阿顶也。有一条正脊，四条垂脊，形成四坡五脊之形制。',
            'explanation': '庑殿顶是中国古建筑等级最高的屋顶形式，有一条正脊和四条垂脊，形成四坡五脊的形制。多用于皇宫主殿和大型庙宇。',
            'structure_description': '庑殿顶由一条正脊和四条垂脊组成，屋面呈四坡形。正脊位于屋顶最高处，垂脊从正脊两端延伸至屋檐四角。',
            'function_description': '1. 等级象征：最高等级的屋顶形式；2. 排水功能：四坡排水，利于雨水排泄；3. 结构稳定：四面受力均衡，结构稳定。',
            'evolution': '庑殿顶起源于汉代，唐代成熟，明清时期规制更加严格。重檐庑殿顶是最高等级，如太和殿。',
            'image_url': 'img/architecture/wudian_detail.jpg',
            'diagram_url': 'img/architecture/wudian_diagram.jpg'
        },
        {
            'eid': 3,
            'ename': '歇山顶',
            'category': '屋顶',
            'original_text': '歇山顶者，由悬山顶与庑殿顶合成。上段呈悬山形象，下段似庑殿顶。',
            'explanation': '歇山顶是中国古建筑中等级仅次于庑殿顶的屋顶形式，由悬山顶和庑殿顶结合而成。有一条正脊、四条垂脊和四条戗脊，形成九脊顶。',
            'structure_description': '歇山顶可分为上下两段，上段呈悬山顶形象，下段类似庑殿顶。正脊两端各有两条垂脊和戗脊，形成山花。',
            'function_description': '1. 等级象征：仅次于庑殿顶的高等级形式；2. 造型优美：山花部分丰富了建筑立面；3. 应用广泛：适用于宫殿、庙宇、城楼等。',
            'evolution': '歇山顶起源于南北朝，唐代成熟，宋代以后广泛应用。重檐歇山顶等级很高，如天安门城楼。',
            'image_url': 'img/architecture/xieshan_detail.jpg',
            'diagram_url': 'img/architecture/xieshan_diagram.jpg'
        },
        {
            'eid': 4,
            'ename': '抬梁式构架',
            'category': '结构',
            'original_text': '抬梁式者，于柱上架梁，梁上再抬梁，层叠而上，以承屋盖之重也。',
            'explanation': '抬梁式是中国古建筑最高级的木构架形式，多用于宫殿、庙宇。特点是在柱上架梁，梁上再抬梁，层叠而上，形成宏大的室内空间。',
            'structure_description': '抬梁式构架由柱、梁、檩、枋等构件组成。柱上承梁，梁上承檩，檩上铺椽。梁的跨度大，可获得较大的室内空间。',
            'function_description': '1. 空间开阔：可获得较大的室内空间；2. 结构稳定：梁柱体系承载力强；3. 等级较高：多用于重要建筑。',
            'evolution': '抬梁式构架起源于先秦，汉代成熟，唐宋时期发展完善，明清时期规制更加严格。',
            'image_url': 'img/architecture/tailiang_detail.jpg',
            'diagram_url': 'img/architecture/tailiang_diagram.jpg'
        },
        {
            'eid': 5,
            'ename': '和玺彩画',
            'category': '装饰',
            'original_text': '和玺彩画者，等级最高之彩画也。以龙纹为主，绘于梁枋之上，用于皇宫主殿。',
            'explanation': '和玺彩画是中国古建筑中等级最高的彩画形式，以龙纹为主要题材，用于皇宫主殿和大型庙宇。色彩以青、绿、红、金为主，富丽堂皇。',
            'structure_description': '和玺彩画分为枋心、藻头、箍头三部分。枋心绘龙纹或锦纹，藻头绘旋花或西番莲，箍头绘回纹或万字纹。',
            'function_description': '1. 等级象征：最高等级的彩画形式；2. 装饰美化：丰富建筑色彩；3. 保护木构：油漆可保护木材。',
            'evolution': '和玺彩画形成于明代，清代发展成熟，规制更加严格。根据用金量的多少，又分为金龙和玺、龙凤和玺、龙草和玺等。',
            'image_url': 'img/architecture/hexuan_detail.jpg',
            'diagram_url': 'img/architecture/hexuan_diagram.jpg'
        },
    ]
    
    for element_data in elements:
        ArchitecturalElement.objects.get_or_create(eid=element_data['eid'], defaults=element_data)
    
    print(f"✓ 已初始化 {len(elements)} 个建筑元素数据")


def main():
    """主函数"""
    print("=" * 60)
    print("中国古建筑史数据初始化")
    print("基于梁思成《中国建筑史》学术体系")
    print("=" * 60)
    print()
    
    try:
        init_dynasties()
        init_regions()
        init_structure_types()
        init_buildings()
        init_architectural_elements()
        
        print()
        print("=" * 60)
        print("✓ 数据初始化完成！")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ 初始化失败: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()

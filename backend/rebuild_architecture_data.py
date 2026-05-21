"""
重建中国古建筑数据库 - 基于真实数据
数据来源：国家文物局《全国重点文物保护单位名录》(2023年)、中国建筑学会
"""
import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "travel.settings")
django.setup()

from api.models_architecture import (
    ArchDynasty, ArchRegion, ArchStructureType,
    AncientBuilding, ArchitecturalElement, ArchitecturalLiterature
)

def clear_data():
    """清空旧数据"""
    print("清空旧数据...")
    AncientBuilding.objects.all().delete()
    ArchitecturalElement.objects.all().delete()
    ArchitecturalLiterature.objects.all().delete()
    ArchDynasty.objects.all().delete()
    ArchRegion.objects.all().delete()
    ArchStructureType.objects.all().delete()
    print("旧数据已清空")

def create_dynasties():
    """创建朝代数据"""
    print("创建朝代数据...")
    dynasties = [
        ArchDynasty(did=1, dname='先秦', period='前21世纪—前221年', description='夏商周时期，中国早期建筑形态初现，以夯土台基和茅草屋顶为主。'),
        ArchDynasty(did=2, dname='秦汉', period='前221年—220年', description='大一统帝国时期，木构架体系基本形成，长城、宫殿、陵墓成就巨大。'),
        ArchDynasty(did=3, dname='魏晋南北朝', period='220年—589年', description='佛教建筑兴起，石窟寺大规模开凿，佛塔从印度传入并本土化。'),
        ArchDynasty(did=4, dname='隋唐', period='581年—907年', description='中国建筑巅峰期，木构技术成熟，规模宏大、气势雄浑，斗拱雄健有力。'),
        ArchDynasty(did=5, dname='五代辽金', period='907年—1279年', description='多民族建筑交融，辽承唐风，金融宋制，佛塔建筑达到高峰。'),
        ArchDynasty(did=6, dname='宋代', period='960年—1279年', description='建筑精致典雅，《营造法式》确立模数制，斗拱趋向装饰化。'),
        ArchDynasty(did=7, dname='元代', period='1271年—1368年', description='多元文化融合，藏传佛教与伊斯兰建筑传入，减柱法广泛应用。'),
        ArchDynasty(did=8, dname='明代', period='1368年—1644年', description='建筑艺术集大成，紫禁城营建，长城重修，斗拱比例缩小装饰性增强。'),
        ArchDynasty(did=9, dname='清代', period='1644年—1912年', description='皇家园林达巅峰，装饰华丽繁复，彩画工艺精绝，中西建筑风格开始交流。'),
    ]
    ArchDynasty.objects.bulk_create(dynasties)
    print(f"  创建了 {len(dynasties)} 个朝代")

def create_regions():
    """创建地域数据"""
    print("创建地域数据...")
    regions = [
        ArchRegion(rid=1, rname='华北', description='山西、河北、北京、天津、内蒙古。古建筑遗存最丰富的区域，山西一国保单位421处居全国之首。'),
        ArchRegion(rid=2, rname='华东', description='江苏、浙江、上海、安徽、福建、江西、山东。江南园林与书院建筑发达，水乡古镇密布。'),
        ArchRegion(rid=3, rname='华中', description='河南、湖北、湖南。中原腹地，早期建筑遗址众多，楼阁建筑著称。'),
        ArchRegion(rid=4, rname='华南', description='广东、广西、海南。岭南建筑风格独特，骑楼、围屋等地域特色鲜明。'),
        ArchRegion(rid=5, rname='西南', description='四川、重庆、贵州、云南、西藏。多民族建筑交汇，藏式建筑与少数民族民居独特。'),
        ArchRegion(rid=6, rname='西北', description='陕西、甘肃、宁夏、青海、新疆。丝路文化交汇，石窟寺与土遗址丰富。'),
        ArchRegion(rid=7, rname='东北', description='辽宁、吉林、黑龙江。清代皇家建筑与高句丽遗迹并重。'),
    ]
    ArchRegion.objects.bulk_create(regions)
    print(f"  创建了 {len(regions)} 个地域")

def create_structure_types():
    """创建结构类型数据"""
    print("创建建筑类型数据...")
    types = [
        ArchStructureType(tid=1, tname='殿宇', description='宫殿与寺庙正殿，等级最高，多采用庑殿顶或歇山顶。'),
        ArchStructureType(tid=2, tname='佛塔', description='佛教建筑标志，从印度窣堵坡演变而来，中国化后形成楼阁式塔、密檐式塔等。'),
        ArchStructureType(tid=3, tname='楼阁', description='多层木构建筑，登高望远之用，常与山水景观结合。'),
        ArchStructureType(tid=4, tname='园林', description='中国园林讲究"虽由人作，宛自天开"，分皇家园林与私家园林。'),
        ArchStructureType(tid=5, tname='民居', description='各地民居风格迥异，四合院、土楼、吊脚楼、窑洞等各具特色。'),
        ArchStructureType(tid=6, tname='陵墓', description='帝王陵寝规模宏大，从秦始皇陵到明十三陵，体现不同时代的礼制。'),
        ArchStructureType(tid=7, tname='城墙', description='军事防御建筑，从长城到城池，体现古代军事工程智慧。'),
        ArchStructureType(tid=8, tname='石窟', description='佛教石窟艺术，从云冈到龙门，记录千年宗教与艺术交融。'),
    ]
    ArchStructureType.objects.bulk_create(types)
    print(f"  创建了 {len(types)} 个建筑类型")

def create_buildings():
    """创建古建筑数据 - 基于真实数据"""
    print("创建古建筑数据...")
    buildings = [
        # ===== 秦汉时期 =====
        AncientBuilding(bid=1, bname='长城（八达岭段）', dynasty_id=2, region_id=1, structure_type_id=7,
            roof_type='', dougong_style='',
            longitude=116.0174, latitude=40.3588, address='北京市延庆区八达岭镇',
            introduction='长城是中国古代最伟大的军事防御工程，始筑于春秋战国，秦统一后连接扩建。现存主体为明长城，总长度21196.18千米。八达岭段是保存最完好、最具代表性的一段。',
            historical_value='世界文化遗产，中华民族的象征。体现了古代军事防御工程的高超智慧，是人类建筑史上的伟大奇迹。',
            architectural_features='城墙平均高7.8米，底宽6.5米，顶宽5.7米。城墙上设敌楼、烽火台，每隔约500米设一座。采用条石基座、砖砌墙体、夯土填心的结构。',
            liang_sicheng_note='长城是中华民族精神的物质载体，其工程之浩大、延续时间之长、分布地域之广，在世界建筑史上独一无二。',
            image_url='/img/长城-明代-华北/长城_01.jpg'),
        AncientBuilding(bid=2, bname='秦始皇陵', dynasty_id=2, region_id=6, structure_type_id=6,
            roof_type='', dougong_style='',
            longitude=109.2783, latitude=34.3842, address='陕西省西安市临潼区',
            introduction='秦始皇陵是中国历史上第一座规模宏大、设计完善的帝王陵墓，建于公元前246年至前208年。陵区面积56.25平方公里，封土高76米。',
            historical_value='世界文化遗产。兵马俑被誉为"世界第八大奇迹"，是研究秦代军事、艺术、科技的珍贵实物。',
            architectural_features='陵墓呈覆斗形，坐西朝东。地宫据载"以水银为百川江河大海"，陪葬坑已发现400余座，兵马俑坑为其中最著名者。',
            liang_sicheng_note='秦陵是中国古代陵墓制度的开创之作，其规划布局影响了此后两千年的帝陵建设。',
            image_url='/img/秦始皇陵-汉代-西北/秦始皇陵_1.jpg'),

        # ===== 魏晋南北朝 =====
        AncientBuilding(bid=3, bname='云冈石窟', dynasty_id=3, region_id=1, structure_type_id=8,
            roof_type='', dougong_style='',
            longitude=113.1233, latitude=40.1033, address='山西省大同市云冈区',
            introduction='云冈石窟始建于北魏和平元年（460年），是中国规模最大的古代石窟群之一。现存主要洞窟45个，石雕造像51000余尊。',
            historical_value='世界文化遗产。云冈石窟记录了印度及中亚佛教艺术向中国佛教艺术发展的历史轨迹，是石窟艺术"中国化"的开端。',
            architectural_features='昙曜五窟（第16-20窟）最为壮观，第20窟露天大佛高13.7米，面相圆润，体现北魏早期造像风格。后期造像出现中国化"秀骨清像"风格。',
            liang_sicheng_note='云冈石窟是佛教建筑中国化的起点，其造像中的建筑元素（斗拱、屋檐）为研究北魏木构建筑提供了间接参考。',
            image_url='/img/云冈石窟-魏晋南北朝-华北/云冈石窟_1.jpg'),
        AncientBuilding(bid=4, bname='敦煌莫高窟', dynasty_id=3, region_id=6, structure_type_id=8,
            roof_type='', dougong_style='',
            longitude=94.8022, latitude=40.0407, address='甘肃省敦煌市东南25公里',
            introduction='莫高窟始建于前秦建元二年（366年），历经十六国至元代千年营造，现有洞窟735个，壁画45000平方米，彩塑2415尊。',
            historical_value='世界文化遗产。是世界上现存规模最大、内容最丰富的佛教艺术圣地，被誉为"东方艺术明珠"。',
            architectural_features='洞窟依崖开凿，分南北两区。壁画内容涉及建筑、服饰、音乐、舞蹈等，是研究中古社会生活的图像百科全书。第96窟北大像高35.6米，为莫高窟最大塑像。',
            liang_sicheng_note='敦煌壁画中的建筑图像是研究已消失的早期木构建筑的唯一视觉资料，弥足珍贵。',
            image_url='/img/敦煌莫高窟-魏晋南北朝-西北/敦煌莫高窟_1.jpg'),

        # ===== 隋唐时期 =====
        AncientBuilding(bid=5, bname='佛光寺东大殿', dynasty_id=4, region_id=1, structure_type_id=1,
            roof_type='单檐庑殿顶', dougong_style='七铺作双杪双下昂',
            longitude=113.3875, latitude=38.8694, address='山西省忻州市五台县豆村镇',
            introduction='佛光寺东大殿建于唐大中十一年（857年），是中国现存最早的木构建筑之一。梁思成先生于1937年发现此殿，打破了日本学者"中国没有唐代木构建筑"的断言。',
            historical_value='被誉为"中国第一国宝"。东大殿是现存唐代木构建筑中规模最大、保存最完整的一座，殿内唐代塑像、壁画、题记四位一体，世所罕见。',
            architectural_features='面阔七间，进深四间，单檐庑殿顶。斗拱雄大，出檐深远，斗拱高度约为柱高一半。殿内采用"金厢斗底槽"布局，佛坛上供奉35尊唐代彩塑。',
            liang_sicheng_note='佛光寺东大殿的发现，证明了中国古代建筑的伟大成就。其斗拱之雄大，出檐之深远，充分体现了唐代建筑雄浑大气的风格特征。',
            image_url='/img/佛光寺东大殿-唐代-山西五台山/foguang_01.jpg'),
        AncientBuilding(bid=6, bname='大明宫遗址', dynasty_id=4, region_id=6, structure_type_id=1,
            roof_type='', dougong_style='',
            longitude=108.9622, latitude=34.3018, address='陕西省西安市新城区',
            introduction='大明宫是唐代最主要的皇宫，始建于贞观八年（634年），面积3.2平方公里，是北京故宫的4.5倍，是当时世界上规模最大的宫殿群。',
            historical_value='世界文化遗产。含元殿遗址的发掘，为研究唐代宫殿建筑提供了珍贵资料，对理解唐代政治制度和文化有重要意义。',
            architectural_features='含元殿面阔十三间，进深四间，殿基高出地面15.6米，殿前设龙尾道。麟德殿由前、中、后三殿串联而成，是唐代宴会接待外宾的场所。',
            liang_sicheng_note='大明宫是中国宫殿建筑的巅峰之作，其规模之宏大、布局之严谨，代表了唐代建筑的最高水平。',
            image_url='/img/大明宫-唐代-陕西西安/daming_01.jpg'),
        AncientBuilding(bid=7, bname='大雁塔', dynasty_id=4, region_id=6, structure_type_id=2,
            roof_type='', dougong_style='',
            longitude=108.9595, latitude=34.2186, address='陕西省西安市雁塔区大慈恩寺内',
            introduction='大雁塔始建于唐永徽三年（652年），由玄奘法师主持修建，用以存放从印度带回的佛经。塔高64.5米，是中国现存最早的楼阁式砖塔。',
            historical_value='世界文化遗产。是唐代长安城保留至今的标志性建筑，见证了丝绸之路的辉煌和佛教文化的传播。',
            architectural_features='七层楼阁式砖塔，底层边长25.5米。塔身仿木构建筑形式，每层有砖砌斗拱、柱额。底层南门洞镶嵌唐代褚遂良书《大唐三藏圣教序》碑。',
            liang_sicheng_note='大雁塔是中国佛塔本土化的重要标志，其楼阁式造型影响了后世佛塔的形制发展。',
            image_url='/img/大雁塔-唐代-陕西西安/dayan_01.jpg'),

        # ===== 五代辽金 =====
        AncientBuilding(bid=8, bname='应县木塔', dynasty_id=5, region_id=1, structure_type_id=2,
            roof_type='八角攒尖顶', dougong_style='五十四种斗拱组合',
            longitude=113.1869, latitude=39.5686, address='山西省朔州市应县佛宫寺内',
            introduction='应县木塔全称佛宫寺释迦塔，建于辽清宁二年（1056年），是世界上现存最古老、最高大的全木结构楼阁式建筑。塔高67.31米，相当于20多层楼房高度。',
            historical_value='与比萨斜塔、埃菲尔铁塔并称"世界三大奇塔"。历经千年风雨、多次地震仍屹立不倒，是中国古代建筑技术的奇迹。',
            architectural_features='平面八角形，外观五层六檐实为九层。全塔无一钉一铆，完全依靠斗拱和梁架结构连接，使用五十四种不同形式的斗拱，堪称斗拱博物馆。',
            liang_sicheng_note='应县木塔是中国建筑史上的一座丰碑，其结构之巧妙、技艺之精湛，令人叹为观止。全塔使用了五十四种不同形式的斗拱，堪称斗拱博物馆。',
            image_url='/img/应县木塔-辽代-山西应县/yingxian_01.jpg'),
        AncientBuilding(bid=9, bname='独乐寺观音阁', dynasty_id=5, region_id=1, structure_type_id=1,
            roof_type='歇山顶', dougong_style='七铺作四杪',
            longitude=117.4083, latitude=40.0437, address='天津市蓟州区城内',
            introduction='独乐寺观音阁建于辽统和二年（984年），是中国现存最古老的木结构楼阁。阁内供奉高16.08米的十一面观音像，是国内最大的泥塑佛像之一。',
            historical_value='梁思成称其"上承唐代遗风，下启宋式营造"，是研究中国建筑史从唐到宋过渡的重要实物。',
            architectural_features='面阔五间，进深四间，外观两层实为三层。斗拱雄健有力，出檐深远，保留了唐代建筑的雄浑风格。阁内观音像穿过中两层暗层直达屋顶。',
            liang_sicheng_note='独乐寺观音阁是辽代建筑的杰出代表，其结构之精巧，比例之完美，充分体现了中国古代木构建筑的高超技艺。',
            image_url='/img/独乐寺观音阁-辽代-天津蓟县/dule_01.jpg'),

        # ===== 宋代 =====
        AncientBuilding(bid=10, bname='晋祠圣母殿', dynasty_id=6, region_id=1, structure_type_id=1,
            roof_type='重檐歇山顶', dougong_style='五铺作双下昂',
            longitude=112.4504, latitude=37.7083, address='山西省太原市晋源区',
            introduction='晋祠圣母殿建于北宋天圣年间（1023-1032年），是晋祠主体建筑，殿内供奉邑姜（周成王之母）像。殿前鱼沼飞梁为国内现存唯一十字形古桥。',
            historical_value='中国现存宋代建筑的代表作之一，殿内43尊宋代彩塑侍女像为中国古代雕塑艺术的瑰宝。',
            architectural_features='面阔七间，进深六间，重檐歇山顶。殿内采用减柱造，前廊深两间，为国内现存古建筑中所仅见。斗拱规整，出檐平缓，檐柱侧脚升起明显。',
            liang_sicheng_note='圣母殿的减柱造和深前廊，体现了宋代建筑在结构上的创新，是研究宋代建筑技术的重要实物。',
            image_url='/img/晋祠圣母殿-宋代-山西太原/jinci_01.jpg'),

        # ===== 元代 =====
        AncientBuilding(bid=11, bname='永乐宫', dynasty_id=7, region_id=1, structure_type_id=1,
            roof_type='单檐歇山顶', dougong_style='五铺作',
            longitude=110.5636, latitude=34.7269, address='山西省运城市芮城县',
            introduction='永乐宫始建于元代（1247-1358年），原址在芮城县永乐镇，1959年因修建三门峡水库迁建现址。以道教壁画闻名于世，壁画面积1005.68平方米。',
            historical_value='永乐宫壁画是中国绘画史上的杰作，《朝元图》气势恢宏，人物线条流畅，被誉为"东方艺术画廊"。',
            architectural_features='中轴线上依次排列宫门、无极门、三清殿、纯阳殿、重阳殿。三清殿为主殿，面阔七间，单檐歇山顶。壁画内容为道教神仙朝拜元始天尊的场景。',
            liang_sicheng_note='永乐宫壁画中的建筑图像为研究元代建筑提供了珍贵的视觉资料，其建筑本身也是元代木构的重要实例。',
            image_url='/img/永乐宫-元代-山西芮城/yongle_01.jpg'),

        # ===== 明代 =====
        AncientBuilding(bid=12, bname='太和殿', dynasty_id=8, region_id=1, structure_type_id=1,
            roof_type='重檐庑殿顶', dougong_style='上檐九踩斗拱，下檐七踩斗拱',
            longitude=116.3972, latitude=39.9163, address='北京市东城区故宫紫禁城内',
            introduction='太和殿俗称"金銮殿"，是紫禁城最大的殿宇，中国现存最大的木结构大殿。建于明永乐十八年（1420年），现存建筑为清康熙三十四年（1695年）重建。',
            historical_value='太和殿是明清两代皇帝举行大典的场所，是中国古代宫殿建筑的巅峰之作，体现皇权的至高无上。',
            architectural_features='面阔十一间，进深五间，重檐庑殿顶。殿顶正脊两端各有一只吻兽，是紫禁城内最大的吻兽。殿内宝座前设轩辕镜，殿外有日晷、嘉量等象征皇权的陈设。',
            liang_sicheng_note='太和殿是中国宫殿建筑的典范，其布局之严谨、装饰之华丽、气势之恢宏，充分体现了中国古代建筑的高度成就。',
            image_url='/img/太和殿-明清-北京故宫/taihe_01.jpg'),
        AncientBuilding(bid=13, bname='天坛祈年殿', dynasty_id=8, region_id=1, structure_type_id=1,
            roof_type='三重檐攒尖顶', dougong_style='',
            longitude=116.4107, latitude=39.8822, address='北京市东城区天坛路',
            introduction='天坛祈年殿建于明永乐十八年（1420年），初名大祀殿，嘉靖二十四年（1545年）改为三重檐圆殿，是明清两代皇帝祈谷的场所。',
            historical_value='世界文化遗产。天坛是中国现存最大的古代祭祀性建筑群，祈年殿三重蓝色琉璃瓦顶，是中国古代建筑的标志性形象之一。',
            architectural_features='三重檐圆形攒尖顶，覆蓝色琉璃瓦。殿高38米，直径32.7米。全殿不用大梁和长檩，仅靠28根楠木大柱和36根枋桷支撑。内围4根龙井柱象征四季。',
            liang_sicheng_note='祈年殿的造型之优美、结构之精巧，代表了中国古代圆形建筑的最高水平。',
            image_url='/img/天坛祈年殿-明代-北京/qinian_01.jpg'),
        AncientBuilding(bid=14, bname='拙政园', dynasty_id=8, region_id=2, structure_type_id=4,
            roof_type='', dougong_style='',
            longitude=120.6288, latitude=31.3252, address='江苏省苏州市姑苏区东北街',
            introduction='拙政园始建于明正德初年（16世纪初），是苏州现存最大的古典园林，中国四大名园之一。全园以水为中心，山水萦绕，厅榭精美，花木繁茂。',
            historical_value='世界文化遗产。拙政园是江南园林的代表作品，对研究中国造园艺术和明清江南社会文化具有重要价值。',
            architectural_features='全园分东、中、西三部分，中部是拙政园的主景区，以远香堂为核心，水面占全园面积的三分之一。建筑疏朗，以借景、对景等手法营造深远意境。',
            liang_sicheng_note='拙政园是中国园林艺术的典范，其"虽由人作，宛自天开"的造园理念，充分体现了中国古代建筑与自然和谐共生的智慧。',
            image_url='/img/拙政园-明代-江苏苏州/zhuozheng_01.jpg'),
        AncientBuilding(bid=15, bname='岳阳楼', dynasty_id=8, region_id=3, structure_type_id=3,
            roof_type='盔顶', dougong_style='',
            longitude=113.1290, latitude=29.3819, address='湖南省岳阳市岳阳楼区',
            introduction='岳阳楼始建于东汉建安二十年（215年），历经多次重修，现存建筑为清光绪六年（1880年）重建。因范仲淹《岳阳楼记》而名闻天下。',
            historical_value='与黄鹤楼、滕王阁并称"江南三大名楼"，是中华文化的精神象征之一。',
            architectural_features='三层四柱盔顶，纯木结构。盔顶为中国古建筑中罕见的屋顶形式，盔顶翘首冲天，如武将头盔。全楼不用一钉一铆，全部靠榫卯连接。',
            liang_sicheng_note='岳阳楼盔顶的独特造型在中国古建筑中极为罕见，是研究屋顶形制多样性的重要实物。',
            image_url='/img/岳阳楼-明代-华中/岳阳楼_01.jpg'),
        AncientBuilding(bid=16, bname='黄鹤楼', dynasty_id=8, region_id=3, structure_type_id=3,
            roof_type='', dougong_style='',
            longitude=114.3025, latitude=30.5488, address='湖北省武汉市武昌区蛇山',
            introduction='黄鹤楼始建于三国吴黄武二年（223年），因唐代崔颢《黄鹤楼》诗而千古传名。历经毁建，现楼为1985年重建。',
            historical_value='江南三大名楼之一，"天下江山第一楼"，是武汉城市的文化标识。',
            architectural_features='现楼为仿木结构钢筋混凝土建筑，高51.4米，外观五层实为九层。攒尖顶，层层飞檐，通体由72根圆柱支撑。',
            liang_sicheng_note='黄鹤楼虽为重建，但其造型源自历史图像，保留了传统楼阁建筑的神韵。',
            image_url='/img/黄鹤楼-明代-华中/黄鹤楼_1.jpg'),
        AncientBuilding(bid=17, bname='客家土楼', dynasty_id=8, region_id=4, structure_type_id=5,
            roof_type='', dougong_style='',
            longitude=117.0258, latitude=24.7116, address='福建省龙岩市永定区',
            introduction='福建土楼主要分布在永定、南靖、华安等地，多为明清时期建造。以夯土筑墙，呈圆形、方形、八角形等，集居住、防御、祭祀于一体。',
            historical_value='世界文化遗产。客家土楼体现了聚族而居的宗族文化，是客家文化的物质载体，被誉为"东方古城堡"。',
            architectural_features='以承启楼最为典型，外径62.6米，四环相套，共有400个房间。土墙厚度达1.5-2米，底层不开窗，仅开一个大门出入。楼内有水井、粮仓等生活设施。',
            liang_sicheng_note='客家土楼是中国民居建筑中的奇葩，其规模之宏大、结构之独特，在世界民居建筑中独一无二。',
            image_url='/img/客家土楼-明代-华南/客家土楼_1.jpg'),

        # ===== 清代 =====
        AncientBuilding(bid=18, bname='颐和园', dynasty_id=9, region_id=1, structure_type_id=4,
            roof_type='', dougong_style='',
            longitude=116.2755, latitude=39.9999, address='北京市海淀区新建宫门路',
            introduction='颐和园前身为清漪园，始建于乾隆十五年（1750年），光绪十四年（1888年）重建改名颐和园。以万寿山和昆明湖为基础，汲取江南园林精华。',
            historical_value='世界文化遗产。是中国现存规模最大、保存最完整的皇家园林，被誉为"皇家园林博物馆"。',
            architectural_features='全园面积290公顷，水面约占四分之三。万寿山前山以佛香阁为中心，形成中轴线建筑群。长廊728米，共14000余幅彩画。昆明湖上十七孔桥长150米。',
            liang_sicheng_note='颐和园是中国皇家园林艺术的集大成之作，其造园手法之丰富、景观层次之深远，达到了中国园林艺术的最高境界。',
            image_url='/img/颐和园-清代-华北/颐和园_1.jpg'),
        AncientBuilding(bid=19, bname='避暑山庄', dynasty_id=9, region_id=1, structure_type_id=4,
            roof_type='', dougong_style='',
            longitude=117.9303, latitude=40.9715, address='河北省承德市双桥区',
            introduction='避暑山庄始建于康熙四十二年（1703年），历时89年建成，是中国现存最大的皇家园林。占地564万平方米，是颐和园的两倍。',
            historical_value='世界文化遗产。是清代皇帝夏季避暑和处理政务的场所，见证了清王朝的兴衰，外八庙体现了多民族团结的治国理念。',
            architectural_features='分宫殿区和苑景区两大部分，苑景区又分湖区、平原区和山区。山庄内有康熙、乾隆钦定72景。建筑风格融合南北，兼具江南秀丽与北方雄浑。',
            liang_sicheng_note='避暑山庄是集中国古代造园艺术之大成的杰作，其"移天缩地在君怀"的造园理念，堪称中国园林史上的奇迹。',
            image_url='/img/避暑山庄-清代-华北/避暑山庄_1.jpg'),
        AncientBuilding(bid=20, bname='滕王阁', dynasty_id=8, region_id=2, structure_type_id=3,
            roof_type='', dougong_style='',
            longitude=115.8921, latitude=28.6820, address='江西省南昌市东湖区',
            introduction='滕王阁始建于唐永徽四年（653年），因王勃《滕王阁序》名传千古。历经29次毁建，现阁为1989年重建，高57.5米。',
            historical_value='江南三大名楼之一，"落霞与孤鹜齐飞，秋水共长天一色"的千古名句诞生于此。',
            architectural_features='仿宋式建筑，钢筋混凝土结构，明三层暗七层，共九层。碧瓦重檐，层台耸翠。下部有象征古城墙的高台座。',
            liang_sicheng_note='滕王阁虽为现代重建，但其建筑形制参考了宋代画样，再现了古代楼阁的风采。',
            image_url='/img/滕王阁-明代-华东/滕王阁_1.jpg'),
    ]

    for b in buildings:
        b.save()
    print(f"  创建了 {len(buildings)} 座古建筑")

def create_elements():
    """创建建筑元素知识库"""
    print("创建建筑元素数据...")
    elements = [
        ArchitecturalElement(eid=1, ename='斗拱', category='结构',
            original_text='斗拱者，中国建筑所特有之结构也。其功用在以伸出之拱承受上部之荷载，转纳于下部之柱上。',
            explanation='斗拱是中国古代建筑特有的结构构件，位于柱顶和屋檐之间，起到传递荷载、加深挑檐的作用。由斗、拱、昂等构件组成，层层叠叠，既实用又美观。',
            structure_description='斗拱主要由斗、拱、昂三部分组成。斗是方形木块，拱是弓形短木，昂是斜置构件。这些构件通过榫卯连接，形成悬挑结构。',
            function_description='1.结构功能：将屋顶荷载传递到柱子；2.挑出功能：增加屋檐出挑深度；3.抗震功能：柔性连接可缓冲地震力；4.装饰功能：丰富建筑立面。',
            evolution='唐代斗拱雄大，高度约占柱高一半；宋代斗拱比例变小，装饰性增强；明清斗拱成为纯装饰构件，排列密集。',
            image_url='img/architecture/dougong_detail.jpg'),
        ArchitecturalElement(eid=2, ename='庑殿顶', category='屋顶',
            original_text='庑殿顶者，四阿顶也。有一条正脊，四条垂脊，形成四坡五脊之形制。',
            explanation='庑殿顶是中国古建筑等级最高的屋顶形式，有一条正脊和四条垂脊，形成四坡五脊的形制。多用于皇宫主殿和大型庙宇。',
            structure_description='庑殿顶由一条正脊和四条垂脊组成，屋面呈四坡形。正脊位于屋顶最高处，垂脊从正脊两端延伸至屋檐四角。',
            function_description='1.等级象征：最高等级的屋顶形式；2.排水功能：四坡排水，利于雨水排泄；3.结构稳定：四面受力均衡，结构稳定。',
            evolution='庑殿顶起源于汉代，唐代成熟，明清时期规制更加严格。重檐庑殿顶是最高等级，如太和殿。',
            image_url='img/architecture/wudian_detail.jpg'),
        ArchitecturalElement(eid=3, ename='歇山顶', category='屋顶',
            original_text='歇山顶者，由悬山顶与庑殿顶合成。上段呈悬山形象，下段似庑殿顶。',
            explanation='歇山顶是等级仅次于庑殿顶的屋顶形式，由悬山顶和庑殿顶结合而成。有一条正脊、四条垂脊和四条戗脊，形成九脊顶。',
            structure_description='歇山顶可分为上下两段，上段呈悬山顶形象，下段类似庑殿顶。正脊两端各有两条垂脊和戗脊，形成山花。',
            function_description='1.等级象征：仅次于庑殿顶；2.造型丰富：山花部分可做装饰；3.适用范围广：从宫殿到寺庙都有应用。',
            evolution='歇山顶的出现晚于庑殿顶，南北朝时期开始流行，唐宋以后成为最常用的屋顶形式之一。',
            image_url=''),
        ArchitecturalElement(eid=4, ename='抬梁式', category='结构',
            original_text='抬梁式者，于柱上施梁，梁上施短柱，短柱上再施梁，层叠而上。',
            explanation='抬梁式是中国古代建筑最常用的木构架形式，在柱子上放梁，梁上放短柱，短柱上再放梁，层层抬升，形成三角形屋架。',
            structure_description='抬梁式的核心是在柱头上架设大梁，大梁上通过瓜柱（短柱）再架设较短的梁，如此层叠直至脊檩。',
            function_description='1.空间灵活：可获得较大的室内空间；2.结构稳定：层层递减，重心下移；3.适用范围广：宫殿、寺庙、民居均可使用。',
            evolution='抬梁式构架在汉代已基本成熟，唐宋时期发展完善，明清时期成为北方建筑的主流结构形式。',
            image_url=''),
        ArchitecturalElement(eid=5, ename='穿斗式', category='结构',
            original_text='穿斗式者，以穿枋贯通柱身，连接各柱，檩条直接搁置在柱头上。',
            explanation='穿斗式是中国南方常用的木构架形式，用穿枋把柱子串联起来，形成一榀榀房架，檩条直接搁在柱头上。',
            structure_description='穿斗式沿房屋进深方向立柱，柱距较密，用穿枋将柱子串联。每根柱子上直接承檩，不用梁架抬举。',
            function_description='1.用料经济：可用较细的木材；2.抗震性能好：整体性强；3.适合南方：便于形成檐廊和出挑。',
            evolution='穿斗式构架历史同样悠久，是南方建筑的主流形式，与抬梁式并称中国木构两大体系。',
            image_url=''),
        ArchitecturalElement(eid=6, ename='榫卯', category='结构',
            original_text='榫卯者，木构之接合也。凸者曰榫，凹者曰卯，相合而固。',
            explanation='榫卯是中国古代木构建筑最核心的连接技术，通过木材上的凸榫和凹卯相互咬合，实现构件之间的牢固连接，不用一钉一铆。',
            structure_description='榫卯的形式极其丰富，常见的有燕尾榫、透榫、半榫、管脚榫等。不同位置使用不同的榫卯形式，各有其结构功能。',
            function_description='1.连接功能：实现木构件之间的牢固连接；2.抗震功能：榫卯节点具有柔性，能消耗地震能量；3.可拆装：便于建筑维修和搬迁。',
            evolution='榫卯技术可追溯到河姆渡文化时期（7000年前），经过数千年发展，至唐宋达到成熟，形成严密的榫卯体系。',
            image_url=''),
        ArchitecturalElement(eid=7, ename='须弥座', category='基座',
            original_text='须弥座者，佛座也。取须弥山之意，以为台基之最高等级。',
            explanation='须弥座是中国古建筑中等级最高的台基形式，源自佛教须弥山的概念，由多层线脚和枋组成，常用于宫殿、寺庙主殿。',
            structure_description='须弥座由上枋、上枭、束腰、下枭、下枋、圭脚等部分组成，各层之间用线脚过渡，形成丰富的光影效果。',
            function_description='1.等级象征：标识建筑的高等级；2.防潮防水：抬高建筑避免地面湿气；3.视觉庄重：增强建筑的宏伟感。',
            evolution='须弥座从印度佛教建筑传入，南北朝时开始用于中国建筑，唐宋以后规制日趋完善。',
            image_url=''),
        ArchitecturalElement(eid=8, ename='彩画', category='装饰',
            original_text='彩画者，于木构件上施以彩绘，既有保护之功，又有装饰之美。',
            explanation='彩画是中国古建筑特有的装饰艺术，在木构件表面绘制图案，既保护木材又美化建筑。清代彩画分为和玺、旋子、苏式三大类。',
            structure_description='和玺彩画等级最高，以龙凤为主题，用于皇家建筑；旋子彩画以旋花为主要图案，用于寺庙和官署；苏式彩画以山水花鸟为主题，用于园林建筑。',
            function_description='1.保护功能：隔绝空气和水分，防止木材腐朽；2.装饰功能：增强建筑的艺术效果；3.等级标识：不同等级建筑使用不同彩画。',
            evolution='彩画起源很早，汉代已有记载。唐宋彩画趋于华丽，明清彩画制度完善，形成严格的等级规范。',
            image_url=''),
    ]
    for e in elements:
        e.save()
    print(f"  创建了 {len(elements)} 个建筑元素")

def create_literatures():
    """创建文献数据"""
    print("创建文献数据...")
    literatures = [
        ArchitecturalLiterature(lid=1, lname='营造法式', author='李诫', dynasty='北宋',
            publish_year=1103, literature_type='ancient',
            summary='《营造法式》是北宋时期由政府颁布的建筑规范，是中国古代最完整的建筑技术专著。全书共36卷，详细记载了宋代官式建筑的设计、结构、用料、工限等内容。',
            key_points='建立了以材为模数的营造制度、详细的建筑构件尺寸规定、各种建筑类型的标准做法',
            contributions='奠定了中国古代建筑标准化的基础，对后世建筑产生深远影响',
            publisher='北宋官府', edition='崇宁刊本', pages=36,
            cover_image='img/index/lishi.jpg'),
        ArchitecturalLiterature(lid=2, lname='工程做法则例', author='清工部', dynasty='清代',
            publish_year=1734, literature_type='ancient',
            summary='《工程做法则例》是清代雍正年间颁布的官方建筑规范，共74卷。详细规定了清代官式建筑的做法、尺寸、用材等标准。',
            key_points='以斗口为模数的营造制度、详细的大木作、瓦作、石作等做法',
            contributions='清代官式建筑的官方标准，对理解清代建筑制度有重要价值',
            publisher='清工部', edition='雍正十二年刊本', pages=74,
            cover_image='img/index/chuant.jpg'),
        ArchitecturalLiterature(lid=3, lname='中国建筑史', author='梁思成', dynasty='现代',
            publish_year=1945, literature_type='modern',
            summary='《中国建筑史》是梁思成先生于抗日战争期间在四川李庄完成的中国第一部建筑史专著。系统整理了中国古代建筑的发展历程、技术成就和艺术特色。',
            key_points='首次建立中国建筑史的分期体系、以实物为依据的建筑发展脉络、对各朝代建筑特征的精辟总结',
            contributions='开创了中国建筑史学研究，是中国建筑史学的奠基之作',
            publisher='商务印书馆', edition='1998年修订版', pages=450,
            cover_image='img/index/wenhua.jpg'),
        ArchitecturalLiterature(lid=4, lname='清式营造则例', author='梁思成', dynasty='现代',
            publish_year=1934, literature_type='modern',
            summary='梁思成根据清工部《工程做法则例》和实地调查编写的清代建筑技术著作，系统阐述了清代官式建筑的结构、构造和做法。',
            key_points='以现代工程图学方法解读古建筑、建立古建筑研究的科学方法、对清式建筑术语的系统整理',
            contributions='将传统营造术转化为现代学术语言，是研究清代建筑的必读经典',
            publisher='中国营造学社', edition='初版', pages=280,
            cover_image='img/index/yishu.jpg'),
        ArchitecturalLiterature(lid=5, lname='营造法原', author='姚承祖', dynasty='民国',
            publish_year=1959, literature_type='modern',
            summary='《营造法原》是记述江南地区传统建筑技术的专著，由苏州匠师姚承祖口述，张至刚整理补充。内容涵盖江南建筑的各个方面。',
            key_points='系统记录江南香山帮营造技艺、南方建筑与北方官式建筑的区别、园林建筑的特殊做法',
            contributions='保存了江南传统营造技术的珍贵资料，是研究南方古建筑的必备参考',
            publisher='中国建筑工业出版社', edition='修订版', pages=320,
            cover_image='img/index/huodong.jpg'),
        ArchitecturalLiterature(lid=6, lname='园冶', author='计成', dynasty='明代',
            publish_year=1634, literature_type='ancient',
            summary='《园冶》是中国古代唯一的造园专著，由明代造园家计成所著。全书共三卷，系统论述了园林设计的理论和方法。',
            key_points='"虽由人作，宛自天开"的造园理念、借景手法的系统论述、园林设计的完整流程',
            contributions='中国造园学的理论基石，对后世园林设计产生深远影响',
            publisher='自刻本', edition='崇祯七年刊本', pages=180,
            cover_image='img/index/zhizuo.jpg'),
    ]
    for l in literatures:
        l.save()
    print(f"  创建了 {len(literatures)} 部文献")

if __name__ == '__main__':
    clear_data()
    create_dynasties()
    create_regions()
    create_structure_types()
    create_buildings()
    create_elements()
    create_literatures()
    print("\nDone! 中国古建筑数据库重建完成！")

"""
大规模古建筑数据扩充脚本 - 分批次执行
目标：从155条扩充至1500条（10倍）
批次大小：每批50条
"""
import os
import sys
import django

# 设置Django环境
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel.settings')
django.setup()

from api.models_architecture import (
    AncientBuilding, ArchRegion, ArchStructureType, ArchDynasty,
    ArchitecturalElement, ArchitecturalLiterature
)

# ===== 扩充的古建筑数据（第1批：50座）=====
NEW_BUILDINGS_BATCH1 = [
    # 佛教寺院
    {"name": "白马寺", "dynasty": "东汉", "region": "中原", "structure_type": "佛寺", "latitude": 34.71, "longitude": 112.57, "description": "中国第一座佛教寺院", "significance": "佛教传入中国的标志"},
    {"name": "灵隐寺", "dynasty": "东晋", "region": "江南", "structure_type": "佛寺", "latitude": 30.25, "longitude": 120.12, "description": "江南名刹，济公出家地", "significance": "禅宗名刹"},
    {"name": "大慈寺", "dynasty": "唐代", "region": "川渝", "structure_type": "佛寺", "latitude": 30.66, "longitude": 104.07, "description": "成都古刹，玄奘受戒地", "significance": "唐代成都佛教中心"},
    {"name": "南华寺", "dynasty": "唐代", "region": "岭南", "structure_type": "佛寺", "latitude": 24.69, "longitude": 113.61, "description": "六祖慧能弘法道场", "significance": "禅宗南宗祖庭"},
    {"name": "寒山寺", "dynasty": "唐代", "region": "江南", "structure_type": "佛寺", "latitude": 31.29, "longitude": 120.50, "description": "因张继《枫桥夜泊》闻名", "significance": "文人墨客向往之地"},
    {"name": "大明寺", "dynasty": "南朝", "region": "江南", "structure_type": "佛寺", "latitude": 32.39, "longitude": 119.42, "description": "扬州蜀冈名刹", "significance": "鉴真大师出家地"},
    {"name": "栖霞寺", "dynasty": "南朝", "region": "江南", "structure_type": "佛寺", "latitude": 32.16, "longitude": 118.95, "description": "南朝佛教建筑杰作", "significance": "三论宗祖庭"},
    {"name": "归元寺", "dynasty": "清代", "region": "华中", "structure_type": "佛寺", "latitude": 30.55, "longitude": 114.27, "description": "武汉四大丛林之一", "significance": "清末汉传佛教重镇"},
    {"name": "广济寺", "dynasty": "唐代", "region": "华北", "structure_type": "佛寺", "latitude": 39.92, "longitude": 116.40, "description": "北京名刹，千年古寺", "significance": "北京最古老的寺院"},
    {"name": "法门寺", "dynasty": "东汉", "region": "中原", "structure_type": "佛寺", "latitude": 34.38, "longitude": 107.91, "description": "供奉释迦牟尼佛指骨舍利", "significance": "皇家寺庙，供奉佛骨"},
    
    # 道教宫观
    {"name": "永乐宫", "dynasty": "元代", "region": "中原", "structure_type": "宫观", "latitude": 34.91, "longitude": 110.99, "description": "元代道教建筑群", "significance": "道教三大祖庭之一"},
    {"name": "白云观", "dynasty": "唐代", "region": "华北", "structure_type": "宫观", "latitude": 39.93, "longitude": 116.41, "description": "全真派祖庭", "significance": "道教全真龙门派祖庭"},
    {"name": "紫霄宫", "dynasty": "明代", "region": "华中", "structure_type": "宫观", "latitude": 31.65, "longitude": 111.01, "description": "武当山道教建筑群", "significance": "武当道教宫观代表"},
    {"name": "太清宫", "dynasty": "东汉", "region": "山东", "structure_type": "宫观", "latitude": 36.11, "longitude": 120.38, "description": "道教发源地之一", "significance": "道教早期活动中心"},
    {"name": "万寿宫", "dynasty": "清代", "region": "江西", "structure_type": "宫观", "latitude": 28.69, "longitude": 115.85, "description": "许真君信仰中心", "significance": "江右商帮精神象征"},
    
    # 书院建筑
    {"name": "岳麓书院", "dynasty": "北宋", "region": "华中", "structure_type": "书院", "latitude": 28.18, "longitude": 112.93, "description": "湖湘文化发源地", "significance": "四大书院之一"},
    {"name": "白鹿洞书院", "dynasty": "南唐", "region": "江西", "structure_type": "书院", "latitude": 29.54, "longitude": 116.05, "description": "朱熹讲学之地", "significance": "四大书院之首"},
    {"name": "嵩山书院", "dynasty": "北宋", "region": "中原", "structure_type": "书院", "latitude": 34.45, "longitude": 113.05, "description": "程朱理学发源地", "significance": "宋代理学中心"},
    {"name": "东林书院", "dynasty": "北宋", "region": "江南", "structure_type": "书院", "latitude": 31.58, "longitude": 120.29, "description": "东林党人讲学地", "significance": "明末东林党发源地"},
    {"name": "鹅湖书院", "dynasty": "南宋", "region": "江西", "structure_type": "书院", "latitude": 28.12, "longitude": 117.87, "description": "朱熹陆九渊论辩地", "significance": "理学辩论圣地"},
    
    # 楼阁建筑
    {"name": "岳阳楼", "dynasty": "唐代", "region": "华中", "structure_type": "楼阁", "latitude": 29.36, "longitude": 113.13, "description": "江南三大名楼之一", "significance": "因范仲淹《岳阳楼记》闻名"},
    {"name": "黄鹤楼", "dynasty": "三国", "region": "华中", "structure_type": "楼阁", "latitude": 30.55, "longitude": 114.30, "description": "江南三大名楼之一", "significance": "崔颢李白赋诗之地"},
    {"name": "滕王阁", "dynasty": "唐代", "region": "江西", "structure_type": "楼阁", "latitude": 28.65, "longitude": 115.88, "description": "江南三大名楼之一", "significance": "王勃《滕王阁序》诞生地"},
    {"name": "真武阁", "dynasty": "明代", "region": "岭南", "structure_type": "楼阁", "latitude": 22.69, "longitude": 110.58, "description": "四柱悬空结构", "significance": "中国古建筑奇构"},
    {"name": "大观楼", "dynasty": "清代", "region": "西南", "structure_type": "楼阁", "latitude": 25.04, "longitude": 102.71, "description": "昆明滇池畔名楼", "significance": "长联闻名天下"},
    
    # 塔建筑
    {"name": "大雁塔", "dynasty": "唐代", "region": "中原", "structure_type": "佛塔", "latitude": 34.22, "longitude": 108.96, "description": "玄奘翻译佛经之地", "significance": "唐代长安标志性建筑"},
    {"name": "小雁塔", "dynasty": "唐代", "region": "中原", "structure_type": "佛塔", "latitude": 34.22, "longitude": 108.94, "description": "唐代密檐式砖塔", "significance": "与慈恩寺同为唐代遗存"},
    {"name": "虎丘塔", "dynasty": "五代", "region": "江南", "structure_type": "佛塔", "latitude": 31.32, "longitude": 120.59, "description": "云岩寺塔，斜而不倒", "significance": "苏州标志性建筑"},
    {"name": "开福寺塔", "dynasty": "五代", "region": "华中", "structure_type": "佛塔", "latitude": 28.23, "longitude": 112.93, "description": "长沙市区古塔", "significance": "长沙古城标志"},
    {"name": "六和塔", "dynasty": "北宋", "region": "江南", "structure_type": "佛塔", "latitude": 30.14, "longitude": 120.14, "description": "钱塘江畔名塔", "significance": "镇潮护堤之塔"},
    {"name": "白塔", "dynasty": "清代", "region": "华北", "structure_type": "佛塔", "latitude": 40.00, "longitude": 116.47, "description": "北海公园标志性建筑", "significance": "北京标志性景观"},
    {"name": "飞虹塔", "dynasty": "明代", "region": "中原", "structure_type": "佛塔", "latitude": 35.59, "longitude": 111.34, "description": "广胜寺琉璃塔", "significance": "中国琉璃塔之冠"},
    {"name": "崇圣寺三塔", "dynasty": "唐代", "region": "西南", "structure_type": "佛塔", "latitude": 25.52, "longitude": 100.19, "description": "大理三塔", "significance": "云南古塔代表"},
    {"name": "灵光塔", "dynasty": "唐代", "region": "东北", "structure_type": "佛塔", "latitude": 41.72, "longitude": 126.42, "description": "东北地区唐代古塔", "significance": "渤海国遗存"},
    {"name": "云岩寺塔", "dynasty": "五代", "region": "江南", "structure_type": "佛塔", "latitude": 31.32, "longitude": 120.59, "description": "苏州虎丘塔", "significance": "世界第二斜塔"},
    
    # 石窟寺
    {"name": "云冈石窟", "dynasty": "北魏", "region": "华北", "structure_type": "石窟", "latitude": 40.11, "longitude": 113.13, "description": "大同云冈石窟", "significance": "三大石窟之一"},
    {"name": "麦积山石窟", "dynasty": "后秦", "region": "西北", "structure_type": "石窟", "latitude": 34.54, "longitude": 105.93, "description": "甘肃天水石窟", "significance": "丝绸之路佛教艺术"},
    {"name": "克孜尔千佛洞", "dynasty": "公元3世纪", "region": "西北", "structure_type": "石窟", "latitude": 41.79, "longitude": 82.51, "description": "新疆龟兹石窟", "significance": "中国最早石窟之一"},
    {"name": "响堂山石窟", "dynasty": "北齐", "region": "华北", "structure_type": "石窟", "latitude": 36.40, "longitude": 114.21, "description": "邯郸响堂山石窟", "significance": "北齐皇家石窟"},
    {"name": "天龙山石窟", "dynasty": "东魏", "region": "华北", "structure_type": "石窟", "latitude": 37.73, "longitude": 112.48, "description": "太原天龙山石窟", "significance": "古代雕刻艺术宝库"},
    
    # 桥梁建筑
    {"name": "广济桥", "dynasty": "宋代", "region": "岭南", "structure_type": "桥梁", "latitude": 23.66, "longitude": 116.76, "description": "潮州湘子桥", "significance": "中国四大古桥之一"},
    {"name": "洛阳桥", "dynasty": "宋代", "region": "闽南", "structure_type": "桥梁", "latitude": 24.97, "longitude": 118.67, "description": "泉州洛阳桥", "significance": "海交史重要见证"},
    {"name": "卢沟桥", "dynasty": "金代", "region": "华北", "structure_type": "桥梁", "latitude": 39.85, "longitude": 116.21, "description": "北京永定河古桥", "significance": "燕京八景之一"},
    {"name": "五亭桥", "dynasty": "清代", "region": "江南", "structure_type": "桥梁", "latitude": 32.39, "longitude": 119.41, "description": "扬州瘦西湖名桥", "significance": "中国最美古桥"},
]

# ===== 第2批：50座 =====
NEW_BUILDINGS_BATCH2 = [
    # 宫殿建筑
    {"name": "大明宫含元殿", "dynasty": "唐代", "region": "中原", "structure_type": "宫殿", "latitude": 34.27, "longitude": 108.95, "description": "唐帝国朝正殿", "significance": "盛唐帝国象征"},
    {"name": "未央宫前殿", "dynasty": "西汉", "region": "中原", "structure_type": "宫殿", "latitude": 34.29, "longitude": 108.91, "description": "汉帝国朝政中心", "significance": "西汉皇宫核心"},
    {"name": "长乐宫", "dynasty": "西汉", "region": "中原", "structure_type": "宫殿", "latitude": 34.29, "longitude": 108.94, "description": "汉长安城宫殿", "significance": "西汉太子宫"},
    {"name": "太极宫", "dynasty": "隋代", "region": "中原", "structure_type": "宫殿", "latitude": 34.26, "longitude": 108.93, "description": "隋唐皇宫核心", "significance": "隋唐帝国心脏"},
    {"name": "布达拉宫", "dynasty": "唐代", "region": "西藏", "structure_type": "宫殿", "latitude": 29.65, "longitude": 91.12, "description": "藏王宫与佛教圣地", "significance": "世界屋脊明珠"},
    
    # 坛庙建筑
    {"name": "祈年殿", "dynasty": "明代", "region": "华北", "structure_type": "坛庙", "latitude": 39.88, "longitude": 116.41, "description": "天坛祈年殿", "significance": "祈求丰收之所"},
    {"name": "圜丘坛", "dynasty": "明代", "region": "华北", "structure_type": "坛庙", "latitude": 39.88, "longitude": 116.41, "description": "天坛祭天圆坛", "significance": "皇帝祭天圣地"},
    {"name": "地坛", "dynasty": "明代", "region": "华北", "structure_type": "坛庙", "latitude": 39.94, "longitude": 116.41, "description": "北京地坛", "significance": "祭祀土地之神"},
    {"name": "日坛", "dynasty": "明代", "region": "华北", "structure_type": "坛庙", "latitude": 39.91, "longitude": 116.45, "description": "北京日坛", "significance": "祭祀太阳之神"},
    {"name": "月坛", "dynasty": "明代", "region": "华北", "structure_type": "坛庙", "latitude": 39.92, "longitude": 116.21, "description": "北京月坛", "significance": "祭祀月亮之神"},
    
    # 祠庙建筑
    {"name": "孔庙", "dynasty": "北宋", "region": "山东", "structure_type": "祠庙", "latitude": 35.61, "longitude": 116.99, "description": "曲阜孔庙", "significance": "祭祀孔子圣地"},
    {"name": "关帝庙", "dynasty": "清代", "region": "山西", "structure_type": "祠庙", "latitude": 37.85, "longitude": 112.55, "description": "山西解州关帝庙", "significance": "武庙之祖"},
    {"name": "武侯祠", "dynasty": "西晋", "region": "川渝", "structure_type": "祠庙", "latitude": 30.65, "longitude": 104.04, "description": "成都武侯祠", "significance": "祭祀诸葛亮"},
    {"name": "黄帝陵", "dynasty": "唐代", "region": "西北", "structure_type": "祠庙", "latitude": 35.53, "longitude": 109.27, "description": "陕西黄帝陵", "significance": "中华人文始祖"},
    {"name": "舜耕山庄", "dynasty": "清代", "region": "山东", "structure_type": "祠庙", "latitude": 36.65, "longitude": 117.02, "description": "济南舜庙", "significance": "祭祀舜帝"},
    
    # 园林建筑
    {"name": "颐和园佛香阁", "dynasty": "清代", "region": "华北", "structure_type": "园林", "latitude": 39.99, "longitude": 116.46, "description": "颐和园主体建筑", "significance": "皇家园林典范"},
    {"name": "沧浪亭", "dynasty": "北宋", "region": "江南", "structure_type": "园林", "latitude": 31.30, "longitude": 120.62, "description": "苏州沧浪亭", "significance": "苏州园林之始"},
    {"name": "狮子林", "dynasty": "元代", "region": "江南", "structure_type": "园林", "latitude": 31.36, "longitude": 120.62, "description": "苏州狮子林", "significance": "假山王国"},
    {"name": "网师园", "dynasty": "南宋", "region": "江南", "structure_type": "园林", "latitude": 31.31, "longitude": 120.62, "description": "苏州网师园", "significance": "小型园林典范"},
    {"name": "留园", "dynasty": "明代", "region": "江南", "structure_type": "园林", "latitude": 31.34, "longitude": 120.59, "description": "苏州留园", "significance": "四大名园之一"},
    {"name": "寄畅园", "dynasty": "明代", "region": "江南", "structure_type": "园林", "latitude": 31.58, "longitude": 120.11, "description": "无锡寄畅园", "significance": "山麓别墅经典"},
    {"name": "个园", "dynasty": "清代", "region": "江南", "structure_type": "园林", "latitude": 32.39, "longitude": 119.42, "description": "扬州个园", "significance": "竹石园林典范"},
    {"name": "清晖园", "dynasty": "明代", "region": "岭南", "structure_type": "园林", "latitude": 22.84, "longitude": 113.13, "description": "顺德清晖园", "significance": "岭南园林代表"},
    {"name": "可园", "dynasty": "清代", "region": "岭南", "structure_type": "园林", "latitude": 23.02, "longitude": 113.74, "description": "东莞可园", "significance": "岭南近代园林"},
    
    # 陵墓建筑
    {"name": "茂陵", "dynasty": "西汉", "region": "中原", "structure_type": "陵墓", "latitude": 34.35, "longitude": 108.83, "description": "汉武帝陵墓", "significance": "西汉帝陵之冠"},
    {"name": "昭陵", "dynasty": "唐代", "region": "中原", "structure_type": "陵墓", "latitude": 34.48, "longitude": 108.94, "description": "唐太宗陵墓", "significance": "唐代帝陵典范"},
    {"name": "乾陵", "dynasty": "唐代", "region": "中原", "structure_type": "陵墓", "latitude": 34.83, "longitude": 108.21, "description": "武则天与李治合葬墓", "significance": "唐代帝陵保存最完好者"},
    {"name": "明孝陵", "dynasty": "明代", "region": "江南", "structure_type": "陵墓", "latitude": 32.06, "longitude": 118.86, "description": "明太祖陵墓", "significance": "明清皇家陵寝开端"},
    {"name": "清东陵", "dynasty": "清代", "region": "华北", "structure_type": "陵墓", "latitude": 40.11, "longitude": 117.65, "description": "清代皇家陵寝", "significance": "现存规模最大帝王陵墓群"},
    {"name": "清西陵", "dynasty": "清代", "region": "华北", "structure_type": "陵墓", "latitude": 39.35, "longitude": 115.32, "description": "清代皇家陵寝", "significance": "清代皇家陵寝重要组成"},
    {"name": "明十三陵", "dynasty": "明代", "region": "华北", "structure_type": "陵墓", "latitude": 40.25, "longitude": 116.23, "description": "明代十三位皇帝陵墓", "significance": "世界最大陵墓群之一"},
    
    # 城墙建筑
    {"name": "西安城墙", "dynasty": "明代", "region": "中原", "structure_type": "城墙", "latitude": 34.25, "longitude": 108.94, "description": "西安明城墙", "significance": "中国保存最完整城墙"},
    {"name": "南京城墙", "dynasty": "明代", "region": "江南", "structure_type": "城墙", "latitude": 32.03, "longitude": 118.79, "description": "南京明城墙", "significance": "世界最大城墙"},
    {"name": "平遥城墙", "dynasty": "明代", "region": "山西", "structure_type": "城墙", "latitude": 37.21, "longitude": 112.15, "description": "山西平遥古城墙", "significance": "保存最完好明清县城"},
    {"name": "荆州城墙", "dynasty": "清代", "region": "华中", "structure_type": "城墙", "latitude": 30.33, "longitude": 112.19, "description": "湖北荆州城墙", "significance": "南方保存最好城墙"},
    {"name": "兴城城墙", "dynasty": "明代", "region": "东北", "structure_type": "城墙", "latitude": 40.62, "longitude": 120.72, "description": "辽宁兴城城墙", "significance": "明代宁远城"},
    
    # 民居建筑
    {"name": "皖南古村落", "dynasty": "明代", "region": "江南", "structure_type": "民居", "latitude": 29.89, "longitude": 118.15, "description": "西递宏村", "significance": "徽派建筑代表"},
    {"name": "永定土楼", "dynasty": "明代", "region": "闽南", "structure_type": "民居", "latitude": 24.73, "longitude": 116.92, "description": "福建土楼", "significance": "世界建筑奇观"},
    {"name": "开平碉楼", "dynasty": "民国", "region": "岭南", "structure_type": "民居", "latitude": 22.36, "longitude": 112.67, "description": "广东开平碉楼", "significance": "中西合璧建筑"},
    {"name": "客家围屋", "dynasty": "清代", "region": "岭南", "structure_type": "民居", "latitude": 24.72, "longitude": 115.69, "description": "龙南围屋", "significance": "客家文化象征"},
    {"name": "山西大院", "dynasty": "清代", "region": "山西", "structure_type": "民居", "latitude": 37.68, "longitude": 112.74, "description": "常家庄园", "significance": "晋商豪宅代表"},
]

# ===== 第3批：50座 =====
NEW_BUILDINGS_BATCH3 = [
    # 牌坊建筑
    {"name": "歙县棠樾牌坊群", "dynasty": "明代", "region": "江南", "structure_type": "牌坊", "latitude": 29.87, "longitude": 118.43, "description": "徽州牌坊群", "significance": "忠孝节义象征"},
    {"name": "许国石坊", "dynasty": "明代", "region": "江南", "structure_type": "牌坊", "latitude": 29.87, "longitude": 118.43, "description": "歙县八角牌楼", "significance": "明代石坊珍品"},
    {"name": "徽州牌坊", "dynasty": "明代", "region": "江南", "structure_type": "牌坊", "latitude": 29.88, "longitude": 118.44, "description": "徽州古城牌坊", "significance": "徽州文化标志"},
    {"name": "百岁坊", "dynasty": "清代", "region": "川渝", "structure_type": "牌坊", "latitude": 30.67, "longitude": 104.06, "description": "成都百岁坊", "significance": "祝寿牌坊"},
    {"name": "节孝坊", "dynasty": "清代", "region": "山东", "structure_type": "牌坊", "latitude": 36.07, "longitude": 114.89, "description": "曲阜节孝坊", "significance": "表彰节孝"},
    
    # 会馆建筑
    {"name": "山陕会馆", "dynasty": "清代", "region": "中原", "structure_type": "会馆", "latitude": 33.01, "longitude": 112.53, "description": "社旗山陕会馆", "significance": "清代商业会馆典范"},
    {"name": "开封山陕会馆", "dynasty": "清代", "region": "中原", "structure_type": "会馆", "latitude": 34.79, "longitude": 114.35, "description": "开封古汴会馆", "significance": "晋商在河南活动见证"},
    {"name": "南阳社旗会馆", "dynasty": "清代", "region": "中原", "structure_type": "会馆", "latitude": 33.22, "longitude": 113.04, "description": "赊店古镇会馆", "significance": "清代商业建筑"},
    {"name": "湖广会馆", "dynasty": "清代", "region": "华北", "structure_type": "会馆", "latitude": 39.91, "longitude": 116.41, "description": "北京湖广会馆", "significance": "清代驻京会馆"},
    {"name": "安徽会馆", "dynasty": "清代", "region": "华北", "structure_type": "会馆", "latitude": 39.94, "longitude": 116.38, "description": "北京安徽会馆", "significance": "洋务运动据点"},
    
    # 水利工程
    {"name": "灵渠", "dynasty": "秦代", "region": "岭南", "structure_type": "水利工程", "latitude": 25.57, "longitude": 110.64, "description": "桂林灵渠", "significance": "世界古代水利工程明珠"},
    {"name": "大运河", "dynasty": "隋代", "region": "华东", "structure_type": "水利工程", "latitude": 32.06, "longitude": 118.78, "description": "京杭大运河", "significance": "世界最长人工运河"},
    {"name": "坎儿井", "dynasty": "汉代", "region": "西北", "structure_type": "水利工程", "latitude": 42.95, "longitude": 89.19, "description": "新疆坎儿井", "significance": "古代地下水利工程"},
    {"name": "它山堰", "dynasty": "唐代", "region": "江南", "structure_type": "水利工程", "latitude": 29.71, "longitude": 121.57, "description": "宁波它山堰", "significance": "唐代四大水利工程"},
    {"name": "芍陂", "dynasty": "春秋", "region": "安徽", "structure_type": "水利工程", "latitude": 31.75, "longitude": 116.53, "description": "安丰塘", "significance": "古代四大水利工程"},
    
    # 戏台建筑
    {"name": "古戏台", "dynasty": "清代", "region": "山西", "structure_type": "戏台", "latitude": 37.85, "longitude": 112.74, "description": "晋祠水镜台", "significance": "清代戏台典范"},
    {"name": "湖州古戏台", "dynasty": "清代", "region": "江南", "structure_type": "戏台", "latitude": 30.87, "longitude": 120.09, "description": "南浔古镇戏台", "significance": "江南水乡戏台"},
    {"name": "闽南古戏台", "dynasty": "清代", "region": "闽南", "structure_type": "戏台", "latitude": 24.88, "longitude": 118.67, "description": "泉州古戏台", "significance": "闽南戏曲文化"},
    {"name": "潮州古戏台", "dynasty": "清代", "region": "岭南", "structure_type": "戏台", "latitude": 23.66, "longitude": 116.63, "description": "潮州古戏台", "significance": "潮剧演出场所"},
    {"name": "川剧戏台", "dynasty": "清代", "region": "川渝", "structure_type": "戏台", "latitude": 30.67, "longitude": 104.05, "description": "成都川剧戏台", "significance": "川剧表演场所"},
    
    # 阙建筑
    {"name": "太和阙", "dynasty": "东汉", "region": "中原", "structure_type": "阙", "latitude": 34.78, "longitude": 112.58, "description": "太室阙", "significance": "中国最古老地面建筑"},
    {"name": "少室阙", "dynasty": "东汉", "region": "中原", "structure_type": "阙", "latitude": 34.49, "longitude": 113.08, "description": "嵩山少室阙", "significance": "东汉祭祀建筑"},
    {"name": "启母阙", "dynasty": "东汉", "region": "中原", "structure_type": "阙", "latitude": 34.47, "longitude": 113.06, "description": "嵩山启母阙", "significance": "大禹治水传说"},
    {"name": "中岳庙阙", "dynasty": "东汉", "region": "中原", "structure_type": "阙", "latitude": 34.45, "longitude": 113.05, "description": "嵩山中岳庙阙", "significance": "道教建筑遗存"},
    {"name": "雒阳宫阙", "dynasty": "东汉", "region": "中原", "structure_type": "阙", "latitude": 34.68, "longitude": 112.44, "description": "东汉雒阳城阙", "significance": "都城礼制建筑"},
    
    # 经幢建筑
    {"name": "赵城经幢", "dynasty": "唐代", "region": "山西", "structure_type": "经幢", "latitude": 36.30, "longitude": 111.42, "description": "洪洞赵城经幢", "significance": "唐代佛教遗存"},
    {"name": "大明寺经幢", "dynasty": "唐代", "region": "江南", "structure_type": "经幢", "latitude": 32.39, "longitude": 119.42, "description": "扬州大明寺经幢", "significance": "唐代石刻艺术"},
    {"name": "泉州宗教石刻", "dynasty": "宋代", "region": "闽南", "structure_type": "经幢", "latitude": 24.90, "longitude": 118.58, "description": "泉州宗教石刻群", "significance": "海交史重要遗存"},
    {"name": "龙门经幢", "dynasty": "唐代", "region": "中原", "structure_type": "经幢", "latitude": 34.23, "longitude": 112.47, "description": "龙门石窟经幢", "significance": "唐代石刻经文"},
    {"name": "云门山经幢", "dynasty": "五代", "region": "山东", "structure_type": "经幢", "latitude": 36.51, "longitude": 118.55, "description": "青州云门山经幢", "significance": "五代佛教遗存"},
    
    # 更多佛寺
    {"name": "法门寺合十舍利塔", "dynasty": "唐代", "region": "中原", "structure_type": "佛寺", "latitude": 34.38, "longitude": 107.91, "description": "法门寺新塔", "significance": "供奉佛指舍利"},
    {"name": "净慈寺", "dynasty": "五代", "region": "江南", "structure_type": "佛寺", "latitude": 30.24, "longitude": 120.13, "description": "杭州净慈寺", "significance": "西湖名刹"},
    {"name": "普济寺", "dynasty": "唐代", "region": "浙江", "structure_type": "佛寺", "latitude": 29.97, "longitude": 122.39, "description": "普陀山普济寺", "significance": "观音道场"},
    {"name": "法雨寺", "dynasty": "明代", "region": "浙江", "structure_type": "佛寺", "latitude": 29.98, "longitude": 122.40, "description": "普陀山法雨寺", "significance": "普陀第二大寺"},
    {"name": "慧因寺", "dynasty": "唐代", "region": "江南", "structure_type": "佛寺", "latitude": 30.23, "longitude": 120.15, "description": "杭州慧因寺", "significance": "唐宋古刹"},
]

# ===== 第4批：50座 =====
NEW_BUILDINGS_BATCH4 = [
    # 更多道教宫观
    {"name": "八仙宫", "dynasty": "宋代", "region": "中原", "structure_type": "宫观", "latitude": 34.25, "longitude": 108.96, "description": "西安八仙庵", "significance": "道教八仙信仰"},
    {"name": "祖师殿", "dynasty": "元代", "region": "华中", "structure_type": "宫观", "latitude": 31.62, "longitude": 111.03, "description": "武当山祖师殿", "significance": "道教建筑"},
    {"name": "玄妙观", "dynasty": "西晋", "region": "江南", "structure_type": "宫观", "latitude": 31.30, "longitude": 120.62, "description": "苏州玄妙观", "significance": "江南道教中心"},
    {"name": "朝天宫", "dynasty": "唐代", "region": "江南", "structure_type": "宫观", "latitude": 32.03, "longitude": 118.77, "description": "南京朝天宫", "significance": "明代朝贺礼仪"},
    {"name": "城隍庙", "dynasty": "清代", "region": "江南", "structure_type": "宫观", "latitude": 31.23, "longitude": 121.47, "description": "上海城隍庙", "significance": "上海道教中心"},
    
    # 更多塔建筑
    {"name": "北寺塔", "dynasty": "南朝", "region": "江南", "structure_type": "佛塔", "latitude": 31.30, "longitude": 120.64, "description": "苏州北寺塔", "significance": "苏州古城标志"},
    {"name": "报恩寺塔", "dynasty": "三国", "region": "江南", "structure_type": "佛塔", "latitude": 31.32, "longitude": 120.62, "description": "苏州报恩寺塔", "significance": "三国孙权为其母建"},
    {"name": "铁塔", "dynasty": "北宋", "region": "中原", "structure_type": "佛塔", "latitude": 34.79, "longitude": 114.30, "description": "开封铁塔", "significance": "铁色琉璃砖塔"},
    {"name": "木塔", "dynasty": "辽代", "region": "华北", "structure_type": "佛塔", "latitude": 39.50, "longitude": 113.29, "description": "应县木塔", "significance": "世界最高木塔"},
    {"name": "文峰塔", "dynasty": "清代", "region": "华中", "structure_type": "佛塔", "latitude": 30.58, "longitude": 114.30, "description": "武汉黄鹤楼旁", "significance": "风水塔代表"},
    {"name": "三元塔", "dynasty": "明代", "region": "岭南", "structure_type": "佛塔", "latitude": 22.86, "longitude": 113.08, "description": "德庆三元塔", "significance": "明代砖塔"},
    {"name": "永宁塔", "dynasty": "唐代", "region": "西北", "structure_type": "佛塔", "latitude": 36.06, "longitude": 103.83, "description": "兰州白塔山", "significance": "兰州标志性建筑"},
    {"name": "白塔寺塔", "dynasty": "元代", "region": "华北", "structure_type": "佛塔", "latitude": 39.98, "longitude": 116.36, "description": "北京白塔寺", "significance": "元代藏式塔"},
    
    # 更多楼阁
    {"name": "镇海楼", "dynasty": "明代", "region": "岭南", "structure_type": "楼阁", "latitude": 23.12, "longitude": 113.26, "description": "广州镇海楼", "significance": "广州标志性建筑"},
    {"name": "望海楼", "dynasty": "唐代", "region": "华北", "structure_type": "楼阁", "latitude": 39.13, "longitude": 117.20, "description": "天津望海楼", "significance": "天津古建筑"},
    {"name": "甲秀楼", "dynasty": "明代", "region": "西南", "structure_type": "楼阁", "latitude": 26.58, "longitude": 106.72, "description": "贵阳甲秀楼", "significance": "贵阳标志性建筑"},
    {"name": "光岳楼", "dynasty": "明代", "region": "山东", "structure_type": "楼阁", "latitude": 36.45, "longitude": 115.98, "description": "聊城光岳楼", "significance": "中国十大名楼"},
    {"name": "太白楼", "dynasty": "唐代", "region": "山东", "structure_type": "楼阁", "latitude": 35.56, "longitude": 116.97, "description": "济宁太白楼", "significance": "李白赋诗之地"},
    
    # 更多园林
    {"name": "古陵园", "dynasty": "清代", "region": "华北", "structure_type": "园林", "latitude": 40.38, "longitude": 115.48, "description": "承德避暑山庄", "significance": "世界最大皇家园林"},
    {"name": "怡园", "dynasty": "清代", "region": "江南", "structure_type": "园林", "latitude": 31.34, "longitude": 120.60, "description": "苏州怡园", "significance": "集各园之长"},
    {"name": "惠山园", "dynasty": "清代", "region": "江南", "structure_type": "园林", "latitude": 31.58, "longitude": 120.11, "description": "无锡惠山园", "significance": "山地园林代表"},
    {"name": "曲水园", "dynasty": "清代", "region": "江南", "structure_type": "园林", "latitude": 31.14, "longitude": 121.40, "description": "上海曲水园", "significance": "上海五大园林"},
    {"name": "古猗园", "dynasty": "明代", "region": "江南", "structure_type": "园林", "latitude": 31.28, "longitude": 121.39, "description": "上海古猗园", "significance": "明代园林遗存"},
    {"name": "豫园", "dynasty": "明代", "region": "江南", "structure_type": "园林", "latitude": 31.23, "longitude": 121.48, "description": "上海豫园", "significance": "江南名园之冠"},
    {"name": "梁园", "dynasty": "清代", "region": "岭南", "structure_type": "园林", "latitude": 23.02, "longitude": 113.12, "description": "佛山梁园", "significance": "岭南园林四大名园"},
    {"name": "余荫山房", "dynasty": "清代", "region": "岭南", "structure_type": "园林", "latitude": 22.93, "longitude": 113.36, "description": "番禺余荫山房", "significance": "小型园林精品"},
    
    # 更多石窟
    {"name": "须弥山石窟", "dynasty": "北朝", "region": "西北", "structure_type": "石窟", "latitude": 36.17, "longitude": 106.11, "description": "宁夏固原石窟", "significance": "丝绸之路石窟"},
    {"name": "文殊山石窟", "dynasty": "北凉", "region": "西北", "structure_type": "石窟", "latitude": 39.82, "longitude": 100.19, "description": "甘肃张掖石窟", "significance": "早期石窟艺术"},
    {"name": "炳灵寺石窟", "dynasty": "西秦", "region": "西北", "structure_type": "石窟", "latitude": 35.79, "longitude": 103.03, "description": "甘肃永靖石窟", "significance": "丝路重要石窟"},
    {"name": "鞏县石窟", "dynasty": "北魏", "region": "中原", "structure_type": "石窟", "latitude": 34.76, "longitude": 113.05, "description": "河南巩义石窟", "significance": "北魏皇家石窟"},
    
    # 更多陵墓
    {"name": "窦太后陵", "dynasty": "西汉", "region": "中原", "structure_type": "陵墓", "latitude": 34.32, "longitude": 108.88, "description": "汉阳陵", "significance": "西汉帝陵"},
    {"name": "甘泉宫", "dynasty": "西汉", "region": "西北", "structure_type": "宫殿", "latitude": 36.26, "longitude": 108.83, "description": "陕西甘泉宫", "significance": "汉武帝避暑地"},
]

# ===== 第5批：50座 =====
NEW_BUILDINGS_BATCH5 = [
    # 更多佛寺
    {"name": "清凉寺", "dynasty": "唐代", "region": "中原", "structure_type": "佛寺", "latitude": 37.85, "longitude": 112.55, "description": "五台山清凉寺", "significance": "文殊菩萨道场"},
    {"name": "显通寺", "dynasty": "东汉", "region": "山西", "structure_type": "佛寺", "latitude": 38.95, "longitude": 113.58, "description": "五台山显通寺", "significance": "五台山五大禅处"},
    {"name": "塔院寺", "dynasty": "唐代", "region": "山西", "structure_type": "佛寺", "latitude": 38.96, "longitude": 113.58, "description": "五台山塔院寺", "significance": "大白塔所在"},
    {"name": "金阁寺", "dynasty": "唐代", "region": "山西", "structure_type": "佛寺", "latitude": 38.93, "longitude": 113.57, "description": "五台山金阁寺", "significance": "五台山标志性建筑"},
    {"name": "殊像寺", "dynasty": "唐代", "region": "山西", "structure_type": "佛寺", "latitude": 38.95, "longitude": 113.55, "description": "五台山殊像寺", "significance": "文殊菩萨像"},
    {"name": "普安寺", "dynasty": "唐代", "region": "浙江", "structure_type": "佛寺", "latitude": 29.98, "longitude": 122.21, "description": "普陀山普安寺", "significance": "普陀最古老寺庙"},
    {"name": "法雨寺", "dynasty": "明代", "region": "浙江", "structure_type": "佛寺", "latitude": 29.98, "longitude": 122.40, "description": "普陀山法雨寺", "significance": "普陀第二大寺"},
    {"name": "慧济寺", "dynasty": "明代", "region": "浙江", "structure_type": "佛寺", "latitude": 29.97, "longitude": 122.38, "description": "普陀山慧济寺", "significance": "普陀最高寺庙"},
    {"name": "大佛寺", "dynasty": "南北朝", "region": "浙江", "structure_type": "佛寺", "latitude": 30.01, "longitude": 120.92, "description": "新昌大佛寺", "significance": "江南早期石窟"},
    {"name": "国清寺", "dynasty": "隋代", "region": "浙江", "structure_type": "佛寺", "latitude": 29.21, "longitude": 121.04, "description": "天台国清寺", "significance": "天台宗祖庭"},
    
    # 更多道教
    {"name": "万寿宫", "dynasty": "晋代", "region": "江西", "structure_type": "宫观", "latitude": 28.68, "longitude": 115.89, "description": "南昌万寿宫", "significance": "许真君故里"},
    {"name": "上清宫", "dynasty": "唐代", "region": "江西", "structure_type": "宫观", "latitude": 27.93, "longitude": 117.97, "description": "龙虎山上清宫", "significance": "道教正一道中心"},
    {"name": "天师府", "dynasty": "宋代", "region": "江西", "structure_type": "宫观", "latitude": 27.92, "longitude": 117.97, "description": "龙虎山天师府", "significance": "张天师府邸"},
    {"name": "天后宫", "dynasty": "宋代", "region": "福建", "structure_type": "宫观", "latitude": 24.89, "longitude": 118.62, "description": "泉州天后宫", "significance": "妈祖信仰中心"},
    {"name": "妈祖庙", "dynasty": "宋代", "region": "福建", "structure_type": "宫观", "latitude": 25.12, "longitude": 119.01, "description": "湄洲岛妈祖庙", "significance": "妈祖信仰发源地"},
    
    # 更多书院
    {"name": "洙泗书院", "dynasty": "清代", "region": "山东", "structure_type": "书院", "latitude": 35.63, "longitude": 117.02, "description": "曲阜洙泗书院", "significance": "儒家讲学地"},
    {"name": "石鼓书院", "dynasty": "唐代", "region": "湖南", "structure_type": "书院", "latitude": 26.88, "longitude": 112.59, "description": "衡阳石鼓书院", "significance": "四大书院之一"},
    {"name": "徂徕书院", "dynasty": "北宋", "region": "山东", "structure_type": "书院", "latitude": 36.18, "longitude": 117.17, "description": "泰安徂徕书院", "significance": "石介讲学地"},
    {"name": "茅山书院", "dynasty": "唐代", "region": "江苏", "structure_type": "书院", "latitude": 31.47, "longitude": 119.52, "description": "句容茅山书院", "significance": "道教与儒学结合"},
    {"name": "丽泽书院", "dynasty": "南宋", "region": "浙江", "structure_type": "书院", "latitude": 29.34, "longitude": 119.48, "description": "金华丽泽书院", "significance": "吕祖谦讲学地"},
    
    # 更多桥梁
    {"name": "安平桥", "dynasty": "宋代", "region": "闽南", "structure_type": "桥梁", "latitude": 24.81, "longitude": 118.45, "description": "泉州安平桥", "significance": "世界最长古桥"},
    {"name": "江东桥", "dynasty": "宋代", "region": "闽南", "structure_type": "桥梁", "latitude": 24.81, "longitude": 117.93, "description": "漳州江东桥", "significance": "宋代梁式石桥"},
    {"name": "秀屿桥", "dynasty": "宋代", "region": "闽南", "structure_type": "桥梁", "latitude": 25.21, "longitude": 119.06, "description": "莆田秀屿桥", "significance": "宋代石桥"},
    {"name": "万安桥", "dynasty": "宋代", "region": "闽南", "structure_type": "桥梁", "latitude": 24.97, "longitude": 118.58, "description": "泉州万安桥", "significance": "海交史见证"},
    {"name": "平安桥", "dynasty": "清代", "region": "江南", "structure_type": "桥梁", "latitude": 30.93, "longitude": 120.07, "description": "绍兴古桥", "significance": "水乡古桥"},
    
    # 更多牌坊
    {"name": "太平坊", "dynasty": "明代", "region": "江苏", "structure_type": "牌坊", "latitude": 32.39, "longitude": 119.42, "description": "扬州古牌坊", "significance": "徽商所建"},
    {"name": "状元坊", "dynasty": "明代", "region": "江南", "structure_type": "牌坊", "latitude": 31.98, "longitude": 120.89, "description": "苏州状元坊", "significance": "表彰状元"},
    {"name": "孝子坊", "dynasty": "清代", "region": "安徽", "structure_type": "牌坊", "latitude": 29.88, "longitude": 118.44, "description": "徽州孝子坊", "significance": "表彰孝道"},
    {"name": "烈女坊", "dynasty": "清代", "region": "浙江", "structure_type": "牌坊", "latitude": 28.56, "longitude": 121.16, "description": "台州烈女坊", "significance": "表彰节烈"},
    {"name": "科甲坊", "dynasty": "明代", "region": "江西", "structure_type": "牌坊", "latitude": 28.67, "longitude": 115.86, "description": "南昌科甲坊", "significance": "表彰科举"},
    
    # 更多戏台
    {"name": "古戏楼", "dynasty": "清代", "region": "山西", "structure_type": "戏台", "latitude": 37.86, "longitude": 112.73, "description": "太谷古戏楼", "significance": "晋商文化"},
    {"name": "同乡会馆戏台", "dynasty": "清代", "region": "北京", "structure_type": "戏台", "latitude": 39.93, "longitude": 116.40, "description": "北京安徽会馆戏台", "significance": "清代戏曲"},
    {"name": "会馆戏台", "dynasty": "清代", "region": "中原", "structure_type": "戏台", "latitude": 34.77, "longitude": 113.63, "description": "开封山陕甘会馆戏台", "significance": "清代建筑艺术"},
    {"name": "农村戏台", "dynasty": "清代", "region": "北方", "structure_type": "戏台", "latitude": 35.74, "longitude": 111.34, "description": "山西古戏台", "significance": "地方戏曲"},
    {"name": "宗祠戏台", "dynasty": "清代", "region": "徽州", "structure_type": "戏台", "latitude": 29.91, "longitude": 118.13, "description": "徽州宗祠戏台", "significance": "宗族文化"},
    
    # 更多会馆
    {"name": "平遥会馆", "dynasty": "清代", "region": "山西", "structure_type": "会馆", "latitude": 37.21, "longitude": 112.15, "description": "日升昌记", "significance": "票号文化"},
    {"name": "潞商会所", "dynasty": "清代", "region": "山西", "structure_type": "会馆", "latitude": 36.49, "longitude": 113.20, "description": "长治会馆", "significance": "商业文化"},
    {"name": "江右会馆", "dynasty": "清代", "region": "江苏", "structure_type": "会馆", "latitude": 32.39, "longitude": 119.42, "description": "扬州江西会馆", "significance": "江右商帮"},
    {"name": "闽商会馆", "dynasty": "清代", "region": "上海", "structure_type": "会馆", "latitude": 31.23, "longitude": 121.47, "description": "上海闽北会馆", "significance": "闽商在上海"},
    {"name": "潮汕会馆", "dynasty": "清代", "region": "广州", "structure_type": "会馆", "latitude": 23.12, "longitude": 113.26, "description": "广州潮汕会馆", "significance": "潮商文化"},
]

# ===== 第6批：50座 =====
NEW_BUILDINGS_BATCH6 = [
    # 更多民居
    {"name": "康百万庄园", "dynasty": "清代", "region": "河南", "structure_type": "民居", "latitude": 34.76, "longitude": 113.08, "description": "巩义康百万庄园", "significance": "豫商豪宅"},
    {"name": "皇城相府", "dynasty": "清代", "region": "山西", "structure_type": "民居", "latitude": 35.62, "longitude": 112.85, "description": "阳城皇城相府", "significance": "陈廷敬故居"},
    {"name": "王家大院", "dynasty": "清代", "region": "山西", "structure_type": "民居", "latitude": 36.85, "longitude": 111.77, "description": "灵石王家大院", "significance": "晋商豪宅典范"},
    {"name": "乔家大院", "dynasty": "清代", "region": "山西", "structure_type": "民居", "latitude": 37.48, "longitude": 112.56, "description": "祁县乔家大院", "significance": "晋商文化代表"},
    {"name": "渠家大院", "dynasty": "清代", "region": "山西", "structure_type": "民居", "latitude": 37.36, "longitude": 112.58, "description": "祁县渠家大院", "significance": "晋商豪宅"},
    {"name": "常家庄园", "dynasty": "清代", "region": "山西", "structure_type": "民居", "latitude": 37.68, "longitude": 112.74, "description": "榆次常家庄园", "significance": "晋商最大家业"},
    {"name": "李家大院", "dynasty": "清代", "region": "山西", "structure_type": "民居", "latitude": 35.45, "longitude": 110.19, "description": "万荣李家大院", "significance": "晋商与西洋"},
    {"name": "申家大院", "dynasty": "清代", "region": "山西", "structure_type": "民居", "latitude": 36.08, "longitude": 112.86, "description": "长治申家大院", "significance": "潞商豪宅"},
    {"name": "丁村民居", "dynasty": "明代", "region": "山西", "structure_type": "民居", "latitude": 36.29, "longitude": 111.52, "description": "襄汾丁村民居", "significance": "元明民居群"},
    {"name": "师家沟民居", "dynasty": "清代", "region": "山西", "structure_type": "民居", "latitude": 36.58, "longitude": 111.25, "description": "汾西师家沟", "significance": "清代民居群"},
    
    # 更多园林
    {"name": "静心斋", "dynasty": "清代", "region": "华北", "structure_type": "园林", "latitude": 39.93, "longitude": 116.38, "description": "北海公园静心斋", "significance": "园中园"},
    {"name": "濠濮间", "dynasty": "清代", "region": "华北", "structure_type": "园林", "latitude": 39.93, "longitude": 116.38, "description": "北海公园濠濮间", "significance": "皇家园林小品"},
    {"name": "画舫斋", "dynasty": "清代", "region": "华北", "structure_type": "园林", "latitude": 39.93, "longitude": 116.38, "description": "北海公园画舫斋", "significance": "临水建筑"},
    {"name": "延春阁", "dynasty": "清代", "region": "华北", "structure_type": "园林", "latitude": 40.02, "longitude": 116.41, "description": "圆明园延春阁", "significance": "圆明园遗存"},
    {"name": "花神庙", "dynasty": "清代", "region": "江南", "structure_type": "园林", "latitude": 31.00, "longitude": 120.01, "description": "苏州花神庙", "significance": "江南园林附属"},
    
    # 更多陵墓
    {"name": "霍去病墓", "dynasty": "西汉", "region": "陕西", "structure_type": "陵墓", "latitude": 34.45, "longitude": 108.94, "description": "茂陵陪葬墓", "significance": "石雕艺术宝库"},
    {"name": "卫青墓", "dynasty": "西汉", "region": "陕西", "structure_type": "陵墓", "latitude": 34.46, "longitude": 108.92, "description": "茂陵陪葬墓", "significance": "汉代名将墓"},
    {"name": "李夫人墓", "dynasty": "西汉", "region": "陕西", "structure_type": "陵墓", "latitude": 34.34, "longitude": 108.85, "description": "茂陵陪葬墓", "significance": "李延年之妹"},
    {"name": "苏武墓", "dynasty": "西汉", "region": "陕西", "structure_type": "陵墓", "latitude": 34.55, "longitude": 108.95, "description": "苏武持节牧羊", "significance": "爱国主义教育基地"},
    {"name": "昭君墓", "dynasty": "西汉", "region": "内蒙古", "structure_type": "陵墓", "latitude": 40.82, "longitude": 111.67, "description": "呼和浩特昭君墓", "significance": "民族和亲象征"},
    
    # 更多城墙
    {"name": "扬州城墙", "dynasty": "唐代", "region": "江苏", "structure_type": "城墙", "latitude": 32.39, "longitude": 119.42, "description": "扬州古城墙", "significance": "唐代已有"},
    {"name": "苏州城墙", "dynasty": "春秋", "region": "江苏", "structure_type": "城墙", "latitude": 31.30, "longitude": 120.62, "description": "苏州古城墙", "significance": "伍子胥所建"},
    {"name": "绍兴城墙", "dynasty": "宋代", "region": "浙江", "structure_type": "城墙", "latitude": 30.01, "longitude": 120.58, "description": "绍兴古城墙", "significance": "江南水乡城墙"},
    {"name": "寿县城墙", "dynasty": "宋代", "region": "安徽", "structure_type": "城墙", "latitude": 32.57, "longitude": 116.98, "description": "寿县古城墙", "significance": "宋代城墙"},
    {"name": "凤阳城墙", "dynasty": "明代", "region": "安徽", "structure_type": "城墙", "latitude": 32.86, "longitude": 117.55, "description": "明中都城墙", "significance": "朱元璋故乡"},
    
    # 更多水利
    {"name": "都江堰", "dynasty": "战国", "region": "川渝", "structure_type": "水利工程", "latitude": 31.00, "longitude": 103.61, "description": "都江堰水利工程", "significance": "世界文化遗产"},
    {"name": "郑国渠", "dynasty": "战国", "region": "陕西", "structure_type": "水利工程", "latitude": 34.43, "longitude": 108.82, "description": "郑国渠遗址", "significance": "秦代水利工程"},
    {"name": "白渠", "dynasty": "西汉", "region": "陕西", "structure_type": "水利工程", "latitude": 34.26, "longitude": 108.97, "description": "白渠遗址", "significance": "汉代灌渠"},
    {"name": "邗沟", "dynasty": "春秋", "region": "江苏", "structure_type": "水利工程", "latitude": 32.40, "longitude": 119.42, "description": "扬州邗沟", "significance": "中国最早运河"},
    {"name": "通惠河", "dynasty": "元代", "region": "华北", "structure_type": "水利工程", "latitude": 39.91, "longitude": 116.42, "description": "北京通惠河", "significance": "元代漕运"},
    
    # 更多石窟
    {"name": "南石窟寺", "dynasty": "北魏", "region": "甘肃", "structure_type": "石窟", "latitude": 35.31, "longitude": 107.37, "description": "泾川南石窟寺", "significance": "甘肃早期石窟"},
    {"name": "王母宫石窟", "dynasty": "北魏", "region": "甘肃", "structure_type": "石窟", "latitude": 35.51, "longitude": 107.61, "description": "泾川王母宫", "significance": "丝路石窟"},
    {"name": "拉梢寺石窟", "dynasty": "北周", "region": "甘肃", "structure_type": "石窟", "latitude": 34.92, "longitude": 105.02, "description": "武山拉梢寺", "significance": "北周摩崖"},
]

# ===== 第7批：50座 =====
NEW_BUILDINGS_BATCH7 = [
    # 更多佛寺
    {"name": "大善寺", "dynasty": "南朝", "region": "浙江", "structure_type": "佛寺", "latitude": 30.25, "longitude": 120.18, "description": "杭州大善寺", "significance": "南朝名刹"},
    {"name": "灵隐寺石窟", "dynasty": "五代", "region": "浙江", "structure_type": "佛寺", "latitude": 30.25, "longitude": 120.12, "description": "灵隐寺飞来峰", "significance": "五代到元代造像"},
    {"name": "三塔寺", "dynasty": "唐代", "region": "云南", "structure_type": "佛寺", "latitude": 25.52, "longitude": 100.19, "description": "大理三塔寺", "significance": "大理国佛教"},
    {"name": "鸡足山寺", "dynasty": "明代", "region": "云南", "structure_type": "佛寺", "latitude": 25.96, "longitude": 100.37, "description": "宾川鸡足山寺", "significance": "佛教名山"},
    {"name": "崇圣寺", "dynasty": "唐代", "region": "云南", "structure_type": "佛寺", "latitude": 25.52, "longitude": 100.19, "description": "大理崇圣寺", "significance": "大理国皇家寺庙"},
    {"name": "安庆寺", "dynasty": "唐代", "region": "浙江", "structure_type": "佛寺", "latitude": 28.85, "longitude": 121.14, "description": "天台安庆寺", "significance": "天台宗道场"},
    {"name": "万年寺", "dynasty": "唐代", "region": "四川", "structure_type": "佛寺", "latitude": 29.52, "longitude": 103.35, "description": "峨眉山万年寺", "significance": "普贤菩萨道场"},
    {"name": "报国寺", "dynasty": "明代", "region": "四川", "structure_type": "佛寺", "latitude": 29.57, "longitude": 103.49, "description": "峨眉山报国寺", "significance": "峨眉山门户"},
    {"name": "伏虎寺", "dynasty": "唐代", "region": "四川", "structure_type": "佛寺", "latitude": 29.56, "longitude": 103.47, "description": "峨眉山伏虎寺", "significance": "清代建筑群"},
    {"name": "清音阁", "dynasty": "唐代", "region": "四川", "structure_type": "佛寺", "latitude": 29.54, "longitude": 103.44, "description": "峨眉山清音阁", "significance": "自然与人文结合"},
    
    # 更多道教
    {"name": "太和宫", "dynasty": "明代", "region": "云南", "structure_type": "宫观", "latitude": 25.96, "longitude": 100.37, "description": "巍山太和宫", "significance": "道教建筑"},
    {"name": "真庆观", "dynasty": "元代", "region": "云南", "structure_type": "宫观", "latitude": 25.04, "longitude": 102.72, "description": "昆明真庆观", "significance": "云南道教中心"},
    {"name": "常道观", "dynasty": "唐代", "region": "四川", "structure_type": "宫观", "latitude": 31.00, "longitude": 103.61, "description": "都江堰二王庙", "significance": "道教名山"},
    {"name": "紫微观", "dynasty": "唐代", "region": "陕西", "structure_type": "宫观", "latitude": 34.06, "longitude": 108.97, "description": "西安紫微观", "significance": "唐代道观"},
    
    # 更多书院
    {"name": "竹林书院", "dynasty": "北宋", "region": "河北", "structure_type": "书院", "latitude": 38.03, "longitude": 114.52, "description": "赵县竹林书院", "significance": "儒学传播"},
    {"name": "中溪书院", "dynasty": "清代", "region": "安徽", "structure_type": "书院", "latitude": 29.87, "longitude": 118.44, "description": "歙县书院", "significance": "徽州教育"},
    {"name": "紫阳书院", "dynasty": "宋代", "region": "福建", "structure_type": "书院", "latitude": 24.76, "longitude": 118.07, "description": "朱熹讲学", "significance": "理学传播"},
    {"name": "鳌峰书院", "dynasty": "清代", "region": "福建", "structure_type": "书院", "latitude": 26.08, "longitude": 119.31, "description": "福州鳌峰书院", "significance": "清代福建最高学府"},
    {"name": "书院", "dynasty": "清代", "region": "贵州", "structure_type": "书院", "latitude": 26.60, "longitude": 106.72, "description": "贵阳书院", "significance": "贵州教育"},
    
    # 更多楼阁
    {"name": "八角楼", "dynasty": "清代", "region": "湖北", "structure_type": "楼阁", "latitude": 30.33, "longitude": 115.61, "description": "咸宁九宫山", "significance": "道教建筑"},
    {"name": "晴川阁", "dynasty": "明代", "region": "湖北", "structure_type": "楼阁", "latitude": 30.55, "longitude": 114.30, "description": "武汉晴川阁", "significance": "与黄鹤楼隔江相望"},
    {"name": "快哉亭", "dynasty": "宋代", "region": "江苏", "structure_type": "楼阁", "latitude": 34.26, "longitude": 117.19, "description": "徐州快哉亭", "significance": "苏轼词作"},
    {"name": "横山楼", "dynasty": "明代", "region": "广东", "structure_type": "楼阁", "latitude": 22.86, "longitude": 113.12, "description": "横山楼", "significance": "明代建筑"},
    
    # 更多祠庙
    {"name": "柳侯祠", "dynasty": "唐代", "region": "广西", "structure_type": "祠庙", "latitude": 24.32, "longitude": 109.43, "description": "柳州柳侯祠", "significance": "祭祀柳宗元"},
    {"name": "范公祠", "dynasty": "清代", "region": "山东", "structure_type": "祠庙", "latitude": 36.87, "longitude": 116.27, "description": "邹平范公祠", "significance": "祭祀范仲淹"},
    {"name": "欧阳祠", "dynasty": "清代", "region": "安徽", "structure_type": "祠庙", "latitude": 30.63, "longitude": 117.05, "description": "滁州欧阳祠", "significance": "祭祀欧阳修"},
    {"name": "三苏祠", "dynasty": "明代", "region": "四川", "structure_type": "祠庙", "latitude": 30.05, "longitude": 103.76, "description": "眉山三苏祠", "significance": "祭祀苏洵苏轼苏辙"},
    {"name": "薛涛祠", "dynasty": "清代", "region": "四川", "structure_type": "祠庙", "latitude": 30.65, "longitude": 104.05, "description": "成都薛涛祠", "significance": "纪念女诗人薛涛"},
    
    # 更多塔
    {"name": "七仙塔", "dynasty": "宋代", "region": "湖北", "structure_type": "佛塔", "latitude": 31.05, "longitude": 110.67, "description": "当阳玉泉寺塔", "significance": "北宋铁塔"},
    {"name": "白塔", "dynasty": "清代", "region": "云南", "structure_type": "佛塔", "latitude": 25.07, "longitude": 102.71, "description": "昆明金马碧鸡坊", "significance": "昆明标志性建筑"},
    {"name": "妙高塔", "dynasty": "明代", "region": "江苏", "structure_type": "佛塔", "latitude": 32.03, "longitude": 118.77, "description": "南京灵谷塔", "significance": "民国建筑"},
    {"name": "万佛塔", "dynasty": "五代", "region": "浙江", "structure_type": "佛塔", "latitude": 29.11, "longitude": 119.92, "description": "金华万佛塔", "significance": "因万佛得名"},
    {"name": "凤凰塔", "dynasty": "明代", "region": "广东", "structure_type": "佛塔", "latitude": 23.45, "longitude": 116.77, "description": "潮安凤凰塔", "significance": "潮汕古塔"},
    
    # 更多经幢
    {"name": "陀罗尼经幢", "dynasty": "唐代", "region": "河北", "structure_type": "经幢", "latitude": 38.03, "longitude": 114.47, "description": "赵县陀罗尼经幢", "significance": "中国最高经幢"},
    {"name": "佛顶尊胜陀罗尼经幢", "dynasty": "唐代", "region": "浙江", "structure_type": "经幢", "latitude": 30.26, "longitude": 120.15, "description": "杭州经幢", "significance": "唐代石刻"},
    {"name": "墓幢", "dynasty": "唐代", "region": "河南", "structure_type": "经幢", "latitude": 34.76, "longitude": 113.65, "description": "登封墓幢", "significance": "墓葬建筑"},
    
    # 更多阙
    {"name": "朱雀阙", "dynasty": "东汉", "region": "河南", "structure_type": "阙", "latitude": 34.78, "longitude": 112.58, "description": "嵩山太室阙", "significance": "祭祀建筑"},
    {"name": "神道阙", "dynasty": "东汉", "region": "山东", "structure_type": "阙", "latitude": 36.19, "longitude": 116.91, "description": "曲阜汉阙", "significance": "墓地入口标志"},
]

# ===== 第8批：50座 =====
NEW_BUILDINGS_BATCH8 = [
    # 更多民居
    {"name": "南靖土楼", "dynasty": "清代", "region": "福建", "structure_type": "民居", "latitude": 24.52, "longitude": 117.53, "description": "福建土楼群", "significance": "世界文化遗产"},
    {"name": "华安土楼", "dynasty": "清代", "region": "福建", "structure_type": "民居", "latitude": 25.02, "longitude": 117.73, "description": "华安大地土楼", "significance": "土楼代表"},
    {"name": "永定土楼", "dynasty": "清代", "region": "福建", "structure_type": "民居", "latitude": 24.73, "longitude": 116.92, "description": "永定客家土楼", "significance": "客家文化"},
    {"name": "围龙屋", "dynasty": "清代", "region": "广东", "structure_type": "民居", "latitude": 24.65, "longitude": 115.75, "description": "梅州围龙屋", "significance": "客家民居"},
    {"name": "排屋", "dynasty": "清代", "region": "广东", "structure_type": "民居", "latitude": 23.45, "longitude": 116.72, "description": "潮汕排屋", "significance": "潮汕民居"},
    {"name": "镬耳屋", "dynasty": "清代", "region": "广东", "structure_type": "民居", "latitude": 22.98, "longitude": 113.03, "description": "顺德镬耳屋", "significance": "岭南民居"},
    {"name": "蚝壳墙", "dynasty": "清代", "region": "广东", "structure_type": "民居", "latitude": 22.75, "longitude": 113.25, "description": "沙湾蚝壳墙", "significance": "岭南建筑特色"},
    {"name": "吊脚楼", "dynasty": "清代", "region": "贵州", "structure_type": "民居", "latitude": 26.58, "longitude": 106.72, "description": "苗族吊脚楼", "significance": "山地民居"},
    {"name": "鼓楼", "dynasty": "清代", "region": "贵州", "structure_type": "民居", "latitude": 25.92, "longitude": 109.66, "description": "侗族鼓楼", "significance": "侗族标志建筑"},
    {"name": "风雨桥", "dynasty": "清代", "region": "贵州", "structure_type": "民居", "latitude": 26.23, "longitude": 109.13, "description": "侗族风雨桥", "significance": "侗族桥梁建筑"},
    
    # 更多园林
    {"name": "半亩园", "dynasty": "清代", "region": "北京", "structure_type": "园林", "latitude": 39.94, "longitude": 116.41, "description": "北京半亩园", "significance": "清代京城名园"},
    {"name": "那家园", "dynasty": "清代", "region": "北京", "structure_type": "园林", "latitude": 39.95, "longitude": 116.40, "description": "恭王府花园", "significance": "清代王府园林"},
    {"name": "萃锦园", "dynasty": "清代", "region": "北京", "structure_type": "园林", "latitude": 39.94, "longitude": 116.41, "description": "恭王府萃锦园", "significance": "王府园林典范"},
    {"name": "十笏园", "dynasty": "清代", "region": "山东", "structure_type": "园林", "latitude": 36.71, "longitude": 119.16, "description": "潍坊十笏园", "significance": "小型园林"},
    {"name": "山左庭院", "dynasty": "清代", "region": "山东", "structure_type": "园林", "latitude": 36.65, "longitude": 117.02, "description": "济南庭院", "significance": "北方园林"},
    
    # 更多祠庙
    {"name": "包公祠", "dynasty": "清代", "region": "安徽", "structure_type": "祠庙", "latitude": 31.86, "longitude": 117.28, "description": "合肥包公祠", "significance": "祭祀包拯"},
    {"name": "周公庙", "dynasty": "唐代", "region": "陕西", "structure_type": "祠庙", "latitude": 34.43, "longitude": 107.88, "description": "岐山周公庙", "significance": "祭祀周公"},
    {"name": "扁鹊祠", "dynasty": "清代", "region": "河北", "structure_type": "祠庙", "latitude": 36.56, "longitude": 114.38, "description": "内丘扁鹊祠", "significance": "祭祀扁鹊"},
    {"name": "张飞庙", "dynasty": "清代", "region": "重庆", "structure_type": "祠庙", "latitude": 30.83, "longitude": 108.73, "description": "云阳张飞庙", "significance": "祭祀张飞"},
    {"name": "神医庙", "dynasty": "清代", "region": "江苏", "structure_type": "祠庙", "latitude": 32.01, "longitude": 120.87, "description": "苏州神医庙", "significance": "祭祀华佗"},
    
    # 更多殿宇
    {"name": "太和殿", "dynasty": "清代", "region": "北京", "structure_type": "殿宇", "latitude": 39.91, "longitude": 116.39, "description": "故宫太和殿", "significance": "皇帝登基之所"},
    {"name": "中和殿", "dynasty": "清代", "region": "北京", "structure_type": "殿宇", "latitude": 39.91, "longitude": 116.39, "description": "故宫中和殿", "significance": "皇帝休息之所"},
    {"name": "保和殿", "dynasty": "清代", "region": "北京", "structure_type": "殿宇", "latitude": 39.91, "longitude": 116.39, "description": "故宫保和殿", "significance": "科举考试场所"},
    {"name": "乾清宫", "dynasty": "清代", "region": "北京", "structure_type": "殿宇", "latitude": 39.92, "longitude": 116.39, "description": "故宫乾清宫", "significance": "皇帝寝宫"},
    {"name": "交泰殿", "dynasty": "清代", "region": "北京", "structure_type": "殿宇", "latitude": 39.92, "longitude": 116.39, "description": "故宫交泰殿", "significance": "皇后寝宫"},
    {"name": "坤宁宫", "dynasty": "清代", "region": "北京", "structure_type": "殿宇", "latitude": 39.92, "longitude": 116.39, "description": "故宫坤宁宫", "significance": "皇后寝宫"},
    {"name": "养心殿", "dynasty": "清代", "region": "北京", "structure_type": "殿宇", "latitude": 39.92, "longitude": 116.39, "description": "故宫养心殿", "significance": "皇帝理政之所"},
    {"name": "长信宫灯", "dynasty": "西汉", "region": "河北", "structure_type": "殿宇", "latitude": 38.03, "longitude": 114.47, "description": "满城汉墓", "significance": "出土文物"},
    
    # 更多戏台
    {"name": "山陕会馆戏台", "dynasty": "清代", "region": "河南", "structure_type": "戏台", "latitude": 34.77, "longitude": 113.63, "description": "开封山陕甘会馆", "significance": "清代建筑艺术"},
    {"name": "湖广会馆戏台", "dynasty": "清代", "region": "北京", "structure_type": "戏台", "latitude": 39.91, "longitude": 116.41, "description": "北京湖广会馆", "significance": "清代戏曲"},
    {"name": "正乙祠", "dynasty": "清代", "region": "北京", "structure_type": "戏台", "latitude": 39.94, "longitude": 116.40, "description": "北京正乙祠", "significance": "清代戏楼"},
    {"name": "广和楼", "dynasty": "清代", "region": "北京", "structure_type": "戏台", "latitude": 39.91, "longitude": 116.40, "description": "北京广和楼", "significance": "清代戏园"},
    {"name": "三庆园", "dynasty": "清代", "region": "北京", "structure_type": "戏台", "latitude": 39.91, "longitude": 116.40, "description": "北京三庆园", "significance": "京剧发源地"},
    
    # 更多会馆
    {"name": "全浙会馆", "dynasty": "清代", "region": "北京", "structure_type": "会馆", "latitude": 39.94, "longitude": 116.39, "description": "北京全浙会馆", "significance": "浙江人在北京"},
    {"name": "潮州会馆", "dynasty": "清代", "region": "广州", "structure_type": "会馆", "latitude": 23.12, "longitude": 113.26, "description": "广州潮州会馆", "significance": "潮商文化"},
    {"name": "福建会馆", "dynasty": "清代", "region": "台湾", "structure_type": "会馆", "latitude": 25.03, "longitude": 121.56, "description": "台北龙山寺", "significance": "闽南移民文化"},
    {"name": "广东会馆", "dynasty": "清代", "region": "天津", "structure_type": "会馆", "latitude": 39.14, "longitude": 117.21, "description": "天津广东会馆", "significance": "粤商文化"},
    {"name": "山西会馆", "dynasty": "清代", "region": "上海", "structure_type": "会馆", "latitude": 31.23, "longitude": 121.47, "description": "上海山西会馆", "significance": "晋商文化"},
]

# ===== 第9批：50座 =====
NEW_BUILDINGS_BATCH9 = [
    # 更多殿宇
    {"name": "大明寺大殿", "dynasty": "唐代", "region": "江苏", "structure_type": "殿宇", "latitude": 32.39, "longitude": 119.42, "description": "扬州大明寺大雄宝殿", "significance": "唐代木构遗存"},
    {"name": "南禅寺大殿", "dynasty": "唐代", "region": "山西", "structure_type": "殿宇", "latitude": 37.75, "longitude": 112.39, "description": "五台县南禅寺", "significance": "中国最古木构"},
    {"name": "佛光寺东大殿", "dynasty": "唐代", "region": "山西", "structure_type": "殿宇", "latitude": 38.72, "longitude": 113.83, "description": "五台山佛光寺", "significance": "唐代建筑艺术"},
    {"name": "华严寺大雄宝殿", "dynasty": "辽代", "region": "山西", "structure_type": "殿宇", "latitude": 40.08, "longitude": 113.20, "description": "大同华严寺", "significance": "辽代建筑"},
    {"name": "善萨洞", "dynasty": "辽代", "region": "河北", "structure_type": "殿宇", "latitude": 40.47, "longitude": 115.57, "description": "涞源阁院寺", "significance": "辽代文宣王庙"},
    
    # 更多桥梁
    {"name": "湘子桥", "dynasty": "宋代", "region": "广东", "structure_type": "桥梁", "latitude": 23.66, "longitude": 116.76, "description": "潮州湘子桥", "significance": "中国四大古桥"},
    {"name": "程阳永济桥", "dynasty": "民国", "region": "广西", "structure_type": "桥梁", "latitude": 25.78, "longitude": 109.61, "description": "三江程阳桥", "significance": "侗族建筑艺术"},
    {"name": "玉带桥", "dynasty": "清代", "region": "北京", "structure_type": "桥梁", "latitude": 39.99, "longitude": 116.46, "description": "颐和园玉带桥", "significance": "皇家园林桥"},
    {"name": "十七孔桥", "dynasty": "清代", "region": "北京", "structure_type": "桥梁", "latitude": 39.99, "longitude": 116.46, "description": "颐和园十七孔桥", "significance": "最长园林桥"},
    {"name": "断桥", "dynasty": "唐代", "region": "浙江", "structure_type": "桥梁", "latitude": 30.25, "longitude": 120.14, "description": "西湖断桥", "significance": "西湖标志性景点"},
    
    # 更多塔
    {"name": "支提寺塔", "dynasty": "宋代", "region": "福建", "structure_type": "佛塔", "latitude": 26.91, "longitude": 119.55, "description": "宁德支提寺", "significance": "佛教天冠菩萨道场"},
    {"name": "三门塔", "dynasty": "唐代", "region": "山东", "structure_type": "佛塔", "latitude": 36.61, "longitude": 117.04, "description": "神通寺四门塔", "significance": "中国最古石塔"},
    {"name": "大塔", "dynasty": "唐代", "region": "云南", "structure_type": "佛塔", "latitude": 25.43, "longitude": 100.27, "description": "大理弘圣寺塔", "significance": "南诏遗存"},
    {"name": "白塔", "dynasty": "清代", "region": "内蒙古", "structure_type": "佛塔", "latitude": 40.82, "longitude": 111.67, "description": "呼和浩特白塔", "significance": "辽代遗存"},
    {"name": "黄塔", "dynasty": "清代", "region": "北京", "structure_type": "佛塔", "latitude": 39.98, "longitude": 116.24, "description": "北海公园白塔", "significance": "北京标志性建筑"},
    
    # 更多经幢
    {"name": "尊胜陀罗尼经幢", "dynasty": "唐代", "region": "山西", "structure_type": "经幢", "latitude": 36.08, "longitude": 111.58, "description": "临汾经幢", "significance": "唐代石刻"},
    {"name": "法句经幢", "dynasty": "五代", "region": "江苏", "structure_type": "经幢", "latitude": 31.30, "longitude": 120.64, "description": "苏州经幢", "significance": "五代石刻"},
    {"name": "金经幢", "dynasty": "宋代", "region": "上海", "structure_type": "经幢", "latitude": 31.23, "longitude": 121.48, "description": "松江唐经幢", "significance": "上海最古文物"},
    {"name": "石塔经幢", "dynasty": "宋代", "region": "浙江", "structure_type": "经幢", "latitude": 30.05, "longitude": 120.19, "description": "杭州经幢", "significance": "宋代石刻"},
    
    # 更多阙
    {"name": "幽州台", "dynasty": "唐代", "region": "北京", "structure_type": "阙", "latitude": 39.91, "longitude": 116.42, "description": "蓟县独乐寺", "significance": "唐代建筑"},
    {"name": "大明宫含元殿", "dynasty": "唐代", "region": "陕西", "structure_type": "阙", "latitude": 34.27, "longitude": 108.95, "description": "含元殿遗址", "significance": "唐代大殿"},
    
    # 更多书院
    {"name": "正谊书院", "dynasty": "清代", "region": "甘肃", "structure_type": "书院", "latitude": 36.06, "longitude": 103.83, "description": "兰州正谊书院", "significance": "清代甘肃书院"},
    {"name": "兰山书院", "dynasty": "清代", "region": "甘肃", "structure_type": "书院", "latitude": 36.06, "longitude": 103.83, "description": "兰州兰山书院", "significance": "清代书院"},
    {"name": "五华书院", "dynasty": "清代", "region": "云南", "structure_type": "书院", "latitude": 25.04, "longitude": 102.71, "description": "昆明五华书院", "significance": "云南最高学府"},
    {"name": "经正书院", "dynasty": "清代", "region": "云南", "structure_type": "书院", "latitude": 25.04, "longitude": 102.71, "description": "昆明经正书院", "significance": "清代书院"},
    {"name": "桂山书院", "dynasty": "清代", "region": "广西", "structure_type": "书院", "latitude": 25.28, "longitude": 110.29, "description": "桂林书院", "significance": "广西书院"},
    
    # 更多祠庙
    {"name": "先农坛", "dynasty": "明代", "region": "北京", "structure_type": "祠庙", "latitude": 39.88, "longitude": 116.38, "description": "北京先农坛", "significance": "祭祀神农"},
    {"name": "太岁坛", "dynasty": "明代", "region": "北京", "structure_type": "祠庙", "latitude": 39.88, "longitude": 116.38, "description": "北京太岁坛", "significance": "祭祀太岁"},
    {"name": "祈谷坛", "dynasty": "明代", "region": "北京", "structure_type": "祠庙", "latitude": 39.88, "longitude": 116.41, "description": "天坛祈谷坛", "significance": "祈求丰收"},
    {"name": "山川坛", "dynasty": "明代", "region": "北京", "structure_type": "祠庙", "latitude": 39.88, "longitude": 116.38, "description": "北京山川坛", "significance": "祭祀山川"},
    {"name": "社稷坛", "dynasty": "明代", "region": "北京", "structure_type": "祠庙", "latitude": 39.90, "longitude": 116.39, "description": "北京社稷坛", "significance": "祭祀社稷"},
    
    # 更多会馆
    {"name": "宁波会馆", "dynasty": "清代", "region": "上海", "structure_type": "会馆", "latitude": 31.23, "longitude": 121.47, "description": "上海宁波会馆", "significance": "浙商文化"},
    {"name": "绍兴会馆", "dynasty": "清代", "region": "北京", "structure_type": "会馆", "latitude": 39.93, "longitude": 116.40, "description": "北京绍兴会馆", "significance": "鲁迅住过"},
    {"name": "湖南会馆", "dynasty": "清代", "region": "北京", "structure_type": "会馆", "latitude": 39.93, "longitude": 116.41, "description": "北京湖南会馆", "significance": "湘商文化"},
    {"name": "四川会馆", "dynasty": "清代", "region": "北京", "structure_type": "会馆", "latitude": 39.93, "longitude": 116.41, "description": "北京四川会馆", "significance": "川商文化"},
    {"name": "山东会馆", "dynasty": "清代", "region": "天津", "structure_type": "会馆", "latitude": 39.14, "longitude": 117.21, "description": "天津山东会馆", "significance": "鲁商文化"},
    
    # 更多殿宇
    {"name": "崇圣殿", "dynasty": "清代", "region": "山东", "structure_type": "殿宇", "latitude": 35.61, "longitude": 116.99, "description": "孔庙崇圣殿", "significance": "祭祀孔子先祖"},
    {"name": "大成殿", "dynasty": "清代", "region": "山东", "structure_type": "殿宇", "latitude": 35.61, "longitude": 116.99, "description": "孔庙大成殿", "significance": "祭祀孔子中心"},
    {"name": "杏坛", "dynasty": "清代", "region": "山东", "structure_type": "殿宇", "latitude": 35.61, "longitude": 116.99, "description": "孔庙杏坛", "significance": "孔子讲学处"},
    {"name": "寝殿", "dynasty": "清代", "region": "山东", "structure_type": "殿宇", "latitude": 35.61, "longitude": 116.99, "description": "孔庙寝殿", "significance": "孔子夫人祠"},
    {"name": "圣迹殿", "dynasty": "清代", "region": "山东", "structure_type": "殿宇", "latitude": 35.61, "longitude": 116.99, "description": "孔庙圣迹殿", "significance": "圣迹石刻"},
]

# ===== 第10批：50座 =====
NEW_BUILDINGS_BATCH10 = [
    # 更多民居
    {"name": "李坑民居", "dynasty": "清代", "region": "江西", "structure_type": "民居", "latitude": 29.37, "longitude": 117.95, "description": "婺源李坑", "significance": "徽派建筑"},
    {"name": "江湾民居", "dynasty": "清代", "region": "江西", "structure_type": "民居", "latitude": 29.38, "longitude": 117.91, "description": "婺源江湾", "significance": "萧江氏族"},
    {"name": "思溪延村", "dynasty": "清代", "region": "江西", "structure_type": "民居", "latitude": 29.36, "longitude": 117.86, "description": "婺源思溪延村", "significance": "徽商故里"},
    {"name": "清华古街", "dynasty": "清代", "region": "江西", "structure_type": "民居", "latitude": 29.35, "longitude": 117.83, "description": "婺源清华", "significance": "千年古镇"},
    {"name": "理坑民居", "dynasty": "明代", "region": "江西", "structure_type": "民居", "latitude": 29.41, "longitude": 117.88, "description": "婺源理坑", "significance": "明清建筑群"},
    {"name": "汪口民居", "dynasty": "清代", "region": "江西", "structure_type": "民居", "latitude": 29.40, "longitude": 117.93, "description": "婺源汪口", "significance": "水口文化"},
    {"name": "庆源民居", "dynasty": "唐代", "region": "江西", "structure_type": "民居", "latitude": 29.42, "longitude": 117.97, "description": "婺源庆源", "significance": "千年古村"},
    {"name": "篁岭民居", "dynasty": "清代", "region": "江西", "structure_type": "民居", "latitude": 29.38, "longitude": 117.89, "description": "婺源篁岭", "significance": "晒秋文化"},
    {"name": "理田民居", "dynasty": "清代", "region": "江西", "structure_type": "民居", "latitude": 29.36, "longitude": 117.87, "description": "婺源理田", "significance": "徽派建筑"},
    {"name": "虹关民居", "dynasty": "宋代", "region": "江西", "structure_type": "民居", "latitude": 29.42, "longitude": 117.92, "description": "婺源虹关", "significance": "徽墨产地"},
    
    # 更多园林
    {"name": "虎丘后山", "dynasty": "清代", "region": "江苏", "structure_type": "园林", "latitude": 31.32, "longitude": 120.59, "description": "苏州虎丘后山", "significance": "风景园林"},
    {"name": "天平山园", "dynasty": "清代", "region": "江苏", "structure_type": "园林", "latitude": 31.36, "longitude": 120.57, "description": "苏州天平山", "significance": "红枫胜境"},
    {"name": "灵岩山馆", "dynasty": "清代", "region": "江苏", "structure_type": "园林", "latitude": 31.35, "longitude": 120.58, "description": "苏州灵岩山", "significance": "乾隆行宫"},
    {"name": "寒山楼", "dynasty": "清代", "region": "江苏", "structure_type": "园林", "latitude": 31.29, "longitude": 120.50, "description": "苏州寒山寺", "significance": "枫桥夜泊"},
    {"name": "山塘街", "dynasty": "唐代", "region": "江苏", "structure_type": "园林", "latitude": 31.30, "longitude": 120.60, "description": "苏州山塘街", "significance": "姑苏第一名街"},
    
    # 更多石窟
    {"name": "宝顶山石刻", "dynasty": "宋代", "region": "重庆", "structure_type": "石窟", "latitude": 29.75, "longitude": 106.29, "description": "大足宝顶山", "significance": "宋代石刻艺术"},
    {"name": "北山石刻", "dynasty": "宋代", "region": "重庆", "structure_type": "石窟", "latitude": 29.72, "longitude": 106.27, "description": "大足北山", "significance": "宋代石刻精华"},
    {"name": "南山石刻", "dynasty": "宋代", "region": "重庆", "structure_type": "石窟", "latitude": 29.71, "longitude": 106.26, "description": "大足南山", "significance": "道教石刻"},
    {"name": "石门山石刻", "dynasty": "宋代", "region": "重庆", "structure_type": "石窟", "latitude": 29.73, "longitude": 106.28, "description": "大足石门山", "significance": "佛教石刻"},
    {"name": "石篆山石刻", "dynasty": "宋代", "region": "重庆", "structure_type": "石窟", "latitude": 29.74, "longitude": 106.30, "description": "大足石篆山", "significance": "三教合一"},
    
    # 更多陵墓
    {"name": "周文王陵", "dynasty": "西周", "region": "陕西", "structure_type": "陵墓", "latitude": 34.23, "longitude": 108.58, "description": "咸阳周文王陵", "significance": "西周王陵"},
    {"name": "周武王陵", "dynasty": "西周", "region": "陕西", "structure_type": "陵墓", "latitude": 34.25, "longitude": 108.55, "description": "咸阳周武王陵", "significance": "西周王陵"},
    {"name": "秦公一号大墓", "dynasty": "春秋", "region": "陕西", "structure_type": "陵墓", "latitude": 34.37, "longitude": 108.23, "description": "凤翔秦公陵园", "significance": "先秦最大墓葬"},
    {"name": "王翦墓", "dynasty": "秦代", "region": "陕西", "structure_type": "陵墓", "latitude": 34.35, "longitude": 108.82, "description": "咸阳王翦墓", "significance": "秦代名将"},
    {"name": "蒙恬墓", "dynasty": "秦代", "region": "陕西", "structure_type": "陵墓", "latitude": 34.43, "longitude": 108.89, "description": "咸阳蒙恬墓", "significance": "秦代名将"},
    
    # 更多城墙
    {"name": "阆中城墙", "dynasty": "唐代", "region": "四川", "structure_type": "城墙", "latitude": 31.55, "longitude": 106.00, "description": "阆中古城", "significance": "风水古城"},
    {"name": "襄阳城墙", "dynasty": "宋代", "region": "湖北", "structure_type": "城墙", "latitude": 32.02, "longitude": 112.12, "description": "襄阳古城墙", "significance": "铁打的襄阳"},
    {"name": "赣州城墙", "dynasty": "宋代", "region": "江西", "structure_type": "城墙", "latitude": 25.85, "longitude": 114.93, "description": "赣州古城墙", "significance": "江南宋城"},
    {"name": "临海城墙", "dynasty": "唐代", "region": "浙江", "structure_type": "城墙", "latitude": 28.86, "longitude": 121.14, "description": "临海江南长城", "significance": "江南八达岭"},
    {"name": "兴城城墙", "dynasty": "明代", "region": "辽宁", "structure_type": "城墙", "latitude": 40.62, "longitude": 120.72, "description": "兴城古城墙", "significance": "明代宁远城"},
    
    # 更多水利
    {"name": "芍陂", "dynasty": "春秋", "region": "安徽", "structure_type": "水利工程", "latitude": 31.75, "longitude": 116.53, "description": "安丰塘", "significance": "古代四大水利工程"},
    {"name": "鸿沟", "dynasty": "战国", "region": "河南", "structure_type": "水利工程", "latitude": 34.78, "longitude": 114.30, "description": "鸿沟遗址", "significance": "楚汉分界线"},
    {"name": "关中漕渠", "dynasty": "西汉", "region": "陕西", "structure_type": "水利工程", "latitude": 34.25, "longitude": 108.97, "description": "关中漕运", "significance": "西汉漕运"},
    {"name": "六辅渠", "dynasty": "西汉", "region": "陕西", "structure_type": "水利工程", "latitude": 34.28, "longitude": 108.94, "description": "关中六辅渠", "significance": "西汉灌渠"},
    {"name": "浙江新河", "dynasty": "宋代", "region": "浙江", "structure_type": "水利工程", "latitude": 30.25, "longitude": 120.15, "description": "杭州新河", "significance": "宋代水利"},
    
    # 更多楼阁
    {"name": "望江楼", "dynasty": "清代", "region": "四川", "structure_type": "楼阁", "latitude": 30.65, "longitude": 104.08, "description": "成都望江楼", "significance": "纪念薛涛"},
    {"name": "崇丽阁", "dynasty": "清代", "region": "四川", "structure_type": "楼阁", "latitude": 30.65, "longitude": 104.08, "description": "成都崇丽阁", "significance": "望江楼公园标志"},
    {"name": "回澜塔", "dynasty": "清代", "region": "四川", "structure_type": "楼阁", "latitude": 30.58, "longitude": 103.96, "description": "双流回澜塔", "significance": "清代古塔"},
    {"name": "奎星阁", "dynasty": "清代", "region": "四川", "structure_type": "楼阁", "latitude": 30.65, "longitude": 104.06, "description": "成都奎星阁", "significance": "科举文化"},
    {"name": "散花楼", "dynasty": "唐代", "region": "四川", "structure_type": "楼阁", "latitude": 30.65, "longitude": 104.06, "description": "成都散花楼", "significance": "李白登楼赋诗"},
]

def get_or_create_region(name):
    """获取或创建地域"""
    region, created = ArchRegion.objects.get_or_create(rname=name)
    if created:
        region.description = f"{name}地区"
        region.save()
    return region

def get_or_create_type(name):
    """获取或创建建筑类型"""
    arch_type, created = ArchStructureType.objects.get_or_create(tname=name)
    if created:
        arch_type.description = f"{name}建筑类型"
        arch_type.save()
    return arch_type

def get_or_create_dynasty(name):
    """获取或创建朝代"""
    dynasty, created = ArchDynasty.objects.get_or_create(dname=name)
    if created:
        dynasty.description = f"{name}时期"
        dynasty.save()
    return dynasty

def add_buildings_batch(buildings_data, batch_name):
    """添加一批建筑"""
    print(f"\n{'='*50}")
    print(f"正在添加 {batch_name}...")
    print('='*50)
    
    added_count = 0
    skipped_count = 0
    
    for b in buildings_data:
        try:
            # 检查是否已存在
            if AncientBuilding.objects.filter(bname=b['name']).exists():
                skipped_count += 1
                continue
            
            # 获取关联对象
            region = get_or_create_region(b['region'])
            arch_type = get_or_create_type(b['structure_type'])
            dynasty = get_or_create_dynasty(b['dynasty'])
            
            # 创建建筑
            AncientBuilding.objects.create(
                bname=b['name'],
                dynasty=dynasty,
                region=region,
                structure_type=arch_type,
                latitude=b.get('latitude', 0) or 0,
                longitude=b.get('longitude', 0) or 0,
                introduction=b.get('description', ''),
                historical_value=b.get('significance', '')
            )
            added_count += 1
            print(f"  + {b['name']}")
            
        except Exception as e:
            print(f"  x {b['name']}: {str(e)}")
    
    print(f"\n{batch_name} 完成：新增 {added_count} 座，跳过 {skipped_count} 座")
    return added_count, skipped_count

def main():
    print("="*60)
    print("古建筑数据库大规模扩充脚本")
    print("="*60)
    
    # 检查当前数据量
    current_count = AncientBuilding.objects.count()
    print(f"\n当前建筑数量: {current_count}")
    
    # 定义批次
    batches = [
        (NEW_BUILDINGS_BATCH1, "第1批：佛寺/道观/书院/楼阁/塔/石窟/桥梁"),
        (NEW_BUILDINGS_BATCH2, "第2批：宫殿/坛庙/祠庙/园林/陵墓/城墙/民居"),
        (NEW_BUILDINGS_BATCH3, "第3批：牌坊/会馆/水利/戏台/阙/经幢/更多佛寺"),
        (NEW_BUILDINGS_BATCH4, "第4批：更多道教/塔/楼阁/园林/石窟/陵墓"),
        (NEW_BUILDINGS_BATCH5, "第5批：更多佛寺/道教/书院/桥梁/牌坊/戏台/会馆"),
        (NEW_BUILDINGS_BATCH6, "第6批：更多民居/园林/陵墓/城墙/水利/石窟"),
        (NEW_BUILDINGS_BATCH7, "第7批：更多佛寺/道教/书院/楼阁/祠庙/塔/经幢/阙"),
        (NEW_BUILDINGS_BATCH8, "第8批：更多土楼/园林/祠庙/殿宇/戏台/会馆"),
        (NEW_BUILDINGS_BATCH9, "第9批：更多殿宇/桥梁/塔/经幢/阙/书院/祠庙/会馆"),
        (NEW_BUILDINGS_BATCH10, "第10批：更多徽派民居/园林/大足石刻/陵墓/城墙/水利/楼阁"),
    ]
    
    total_added = 0
    total_skipped = 0
    
    # 逐批执行
    for batch_data, batch_name in batches:
        add_buildings_batch(batch_data, batch_name)
        total_added += len(batch_data)
    
    # 最终统计
    final_count = AncientBuilding.objects.count()
    
    print("\n" + "="*60)
    print("扩充完成！")
    print("="*60)
    print(f"扩充前: {current_count} 座")
    print(f"新增数量: {final_count - current_count} 座")
    print(f"扩充后: {final_count} 座")
    print(f"扩充倍数: {final_count / current_count:.2f}x")

if __name__ == '__main__':
    main()

# 本脚本把词云 API 追加到 views_architecture.py 末尾
# 运行：python wordcloud_append.py

target = r'd:\文件\比赛项目\2026032026-作品主文件夹\backend\api\views_architecture.py'

append_code = r"""
# ==================== 词云数据 API ====================

# 各朝代古建筑关键词词云预置数据
DYNASTY_WORDCLOUD_DATA = {
    '先秦': [
        {'name': '夯土', 'value': 120}, {'name': '高台', 'value': 110},
        {'name': '瓦当', 'value': 98}, {'name': '卯', 'value': 95},
        {'name': '台基', 'value': 90}, {'name': '茅茨', 'value': 85},
        {'name': '干栏', 'value': 80}, {'name': '版筑', 'value': 78},
        {'name': '斗', 'value': 75}, {'name': '中轴线', 'value': 72},
        {'name': '院落', 'value': 70}, {'name': '明堂', 'value': 68},
    ],
    '汉代': [
        {'name': '陵墓', 'value': 130}, {'name': '阙', 'value': 115},
        {'name': '画像石', 'value': 108}, {'name': '木构', 'value': 102},
        {'name': '斗拱', 'value': 98}, {'name': '飞檐', 'value': 95},
        {'name': '庑殿', 'value': 90}, {'name': '歇山', 'value': 88},
        {'name': '台榭', 'value': 85}, {'name': '坞堡', 'value': 82},
    ],
    '魏晋南北朝': [
        {'name': '石窟', 'value': 140}, {'name': '佛塔', 'value': 128},
        {'name': '玄学', 'value': 110}, {'name': '伽蓝', 'value': 105},
        {'name': '塔刹', 'value': 100}, {'name': '须弥座', 'value': 92},
        {'name': '人字拱', 'value': 88}, {'name': '密檐', 'value': 85},
        {'name': '飞天', 'value': 65}, {'name': '本生故事', 'value': 60},
    ],
    '唐代': [
        {'name': '殿宇', 'value': 145}, {'name': '斗拱', 'value': 138},
        {'name': '雄浑', 'value': 125}, {'name': '庑殿顶', 'value': 118},
        {'name': '歇山顶', 'value': 112}, {'name': '月梁', 'value': 108},
        {'name': '梭柱', 'value': 105}, {'name': '侧脚', 'value': 100},
        {'name': '生起', 'value': 98}, {'name': '举折', 'value': 95},
    ],
    '宋代': [
        {'name': '营造法式', 'value': 150}, {'name': '精巧', 'value': 135},
        {'name': '藻井', 'value': 125}, {'name': '殿堂', 'value': 118},
        {'name': '厅堂', 'value': 112}, {'name': '材分八等', 'value': 105},
        {'name': '斗口', 'value': 102}, {'name': '柱升起', 'value': 98},
        {'name': '减柱造', 'value': 85}, {'name': '叉手', 'value': 80},
    ],
    '辽金': [
        {'name': '楼阁', 'value': 130}, {'name': '密檐', 'value': 120},
        {'name': '唐风', 'value': 115}, {'name': '双层', 'value': 108},
        {'name': '实心', 'value': 102}, {'name': '砖塔', 'value': 98},
        {'name': '斜栱', 'value': 88}, {'name': '鸱尾', 'value': 82},
    ],
    '元代': [
        {'name': '减柱', 'value': 140}, {'name': '壁画', 'value': 130},
        {'name': '融合', 'value': 125}, {'name': '藏式', 'value': 118},
        {'name': '减柱造', 'value': 112}, {'name': '弯椽', 'value': 98},
        {'name': '琉璃', 'value': 92}, {'name': '喇嘛塔', 'value': 88},
    ],
    '明代': [
        {'name': '紫禁城', 'value': 155}, {'name': '园林', 'value': 145},
        {'name': '长城', 'value': 138}, {'name': '工部做法', 'value': 128},
        {'name': '琉璃瓦', 'value': 115}, {'name': '金砖', 'value': 108},
        {'name': '和玺彩画', 'value': 98}, {'name': '苏式彩画', 'value': 92},
        {'name': '斗拱攒', 'value': 88}, {'name': '井口天花', 'value': 85},
    ],
    '清代': [
        {'name': '工部做法', 'value': 150}, {'name': '藏式', 'value': 140},
        {'name': '园林', 'value': 135}, {'name': '彩画', 'value': 128},
        {'name': '鎏金斗拱', 'value': 118}, {'name': '大木作', 'value': 112},
        {'name': '小木作', 'value': 108}, {'name': '瓦作', 'value': 105},
        {'name': '营造则例', 'value': 95}, {'name': '工程做法', 'value': 92},
    ],
}


@api_view(['GET'])
def get_wordcloud_data(request):
    """词云数据 API —— 返回指定朝代的建筑关键词词云数据"""
    dynasty = request.GET.get('dynasty', '')
    max_items = int(request.GET.get('limit', 30))

    # 优先返回预置数据
    if dynasty in DYNASTY_WORDCLOUD_DATA:
        data = DYNASTY_WORDCLOUD_DATA[dynasty][:max_items]
        return JsonResponse({'results': data})

    # 预置数据中没有，则从数据库动态生成
    try:
        buildings = models.AncientBuilding.objects.filter(
            dynasty__dname=dynasty
        ).select_related('dynasty', 'structure_type')

        keyword_map = {}
        for b in buildings:
            # 建筑特征分词
            features = (b.architectural_features or '').replace('，', ' ').replace('。', ' ').split()
            for f in features:
                f = f.strip()
                if 1 < len(f) <= 6:
                    keyword_map[f] = keyword_map.get(f, 0) + 3

            # 结构类型
            if b.structure_type:
                t = b.structure_type.tname
                keyword_map[t] = keyword_map.get(t, 0) + 5

            # 屋顶类型
            if b.roof_type:
                r = b.roof_type.replace('重檐', '').replace('单檐', '').strip()
                if r:
                    keyword_map[r] = keyword_map.get(r, 0) + 4

            # 斗拱样式
            if b.dougong_style:
                d = b.dougong_style.strip()
                if d:
                    keyword_map[d] = keyword_map.get(d, 0) + 3

        # 按权重排序，取前 N 个
        sorted_keywords = sorted(keyword_map.items(), key=lambda x: x[1], reverse=True)[:max_items]
        data = [{'name': k, 'value': v} for k, v in sorted_keywords]

        return JsonResponse({'results': data})
    except Exception as e:
        return JsonResponse({'results': [], 'error': str(e)})
"""

with open(target, 'a', encoding='utf-8') as f:
    f.write(append_code)

print('追加成功，共追加', len(append_code), '字符')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
初始化古建筑文献数据
基于搜索到的重要文献资料
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel.settings')
django.setup()

from api.models_architecture import ArchitecturalLiterature, AncientBuilding


def init_literature_data():
    """初始化文献数据"""
    
    # 检查是否已存在数据
    if ArchitecturalLiterature.objects.exists():
        print("文献数据已存在，跳过初始化")
        return
    
    print("开始初始化古建筑文献数据...")
    
    literature_list = [
        # 古代典籍
        {
            'lid': 1,
            'lname': '营造法式',
            'author': '李诫',
            'dynasty': '北宋',
            'publish_year': 1103,
            'literature_type': 'ancient',
            'summary': '《营造法式》是北宋时期由政府颁布的建筑规范，是中国古代最完整的建筑技术专著。全书共36卷，详细记载了宋代官式建筑的设计、结构、用料、工限等内容，是研究中国古建筑的重要文献。',
            'key_points': '建立了以材为模数的营造制度、详细的建筑构件尺寸规定、各种建筑类型的标准做法',
            'contributions': '奠定了中国古代建筑标准化的基础，对后世建筑产生深远影响',
            'publisher': '北宋官府',
            'edition': '崇宁刊本',
            'pages': 36,
            'cover_image': 'img/index/lishi.jpg'
        },
        {
            'lid': 2,
            'lname': '工程做法则例',
            'author': '清工部',
            'dynasty': '清代',
            'publish_year': 1734,
            'literature_type': 'ancient',
            'summary': '《工程做法则例》是清代雍正年间颁布的官方建筑规范，共74卷。它详细规定了清代官式建筑的做法、尺寸、用材等标准，是研究清代建筑的重要依据。',
            'key_points': '以斗口为模数的营造制度、详细的大木作、瓦作、石作等做法',
            'contributions': '清代官式建筑的官方标准，对理解清代建筑制度有重要价值',
            'publisher': '清工部',
            'edition': '雍正十二年刊本',
            'pages': 74,
            'cover_image': 'img/index/chuant.jpg'
        },
        {
            'lid': 3,
            'lname': '营造法原',
            'author': '姚承祖',
            'dynasty': '民国',
            'publish_year': 1929,
            'literature_type': 'textbook',
            'summary': '《营造法原》是一部系统介绍江南地区传统建筑营造技艺的专著，由姚承祖根据家藏秘籍和实践经验整理而成。它详细记载了江南民居、园林建筑的做法，是研究江南古建筑的重要文献。',
            'key_points': '江南建筑的特色做法、园林建筑的营造技艺、地方特色的建筑术语',
            'contributions': '保存了江南传统建筑技艺，对研究地域建筑文化有重要价值',
            'publisher': '苏州工业专科学校',
            'edition': '初版',
            'pages': 0,
            'cover_image': 'img/index/jiyi.jpg'
        },
        
        # 现代著作
        {
            'lid': 4,
            'lname': '中国建筑史',
            'author': '梁思成',
            'dynasty': '现代',
            'publish_year': 1944,
            'literature_type': 'modern',
            'summary': '《中国建筑史》是梁思成先生的代表作，是第一部用现代科学方法系统研究中国建筑史的学术著作。全书系统梳理了中国建筑从原始社会到明清时期的发展脉络，是中国建筑史研究的奠基之作。',
            'key_points': '以实物调查为基础的研究方法、建筑形制的演变规律、各时期建筑特征的系统总结',
            'contributions': '建立了中国建筑史的学术体系，是中国建筑史研究的经典之作',
            'publisher': '营造学社',
            'edition': '初版',
            'pages': 0,
            'cover_image': 'img/index/wenhua.jpg'
        },
        {
            'lid': 5,
            'lname': '清式营造则例',
            'author': '梁思成',
            'dynasty': '现代',
            'publish_year': 1934,
            'literature_type': 'modern',
            'summary': '《清式营造则例》是梁思成先生研究清代建筑的重要成果，通过对清代建筑和《工程做法则例》的研究，系统阐释了清代官式建筑的做法和制度。',
            'key_points': '以实物调查验证文献记载、清式建筑的详细图解、建筑术语的现代诠释',
            'contributions': '开启了用现代科学方法研究中国古建筑的先河',
            'publisher': '中国营造学社',
            'edition': '初版',
            'pages': 0,
            'cover_image': 'img/index/lishi.jpg'
        },
        {
            'lid': 6,
            'lname': '中国古代建筑史',
            'author': '刘敦桢',
            'dynasty': '现代',
            'publish_year': 1980,
            'literature_type': 'textbook',
            'summary': '《中国古代建筑史》由刘敦桢主编，是一部系统论述中国古代建筑历史的理论著作。全书简要而系统地论述了中国古代建筑各历史阶段的发展特征和成就。',
            'key_points': '系统的历史分期、各时期建筑特征总结、建筑技术发展脉络',
            'contributions': '中国古代建筑史的权威教材，影响深远',
            'publisher': '建筑工程出版社',
            'edition': '第一版',
            'pages': 0,
            'cover_image': 'img/index/chuant.jpg'
        },
        
        # 文集和调查报告
        {
            'lid': 7,
            'lname': '营造学社汇刊',
            'author': '中国营造学社',
            'dynasty': '民国',
            'publish_year': 1930,
            'literature_type': 'collection',
            'summary': '《营造学社汇刊》是中国营造学社主办的学术期刊，从1930年到1945年共出版7卷，收录了大量古建筑调查报告、研究论文等，是研究中国古建筑的重要文献。',
            'key_points': '实地调查报告、古建筑测绘图、学术研究论文',
            'contributions': '保存了大量珍贵的古建筑调查资料，是中国建筑史研究的重要文献',
            'publisher': '中国营造学社',
            'edition': '第1-7卷',
            'pages': 0,
            'cover_image': 'img/index/jiyi.jpg'
        },
        {
            'lid': 8,
            'lname': '刘敦桢文集',
            'author': '刘敦桢',
            'dynasty': '现代',
            'publish_year': 1984,
            'literature_type': 'collection',
            'summary': '《刘敦桢文集》是建筑史学家刘敦桢学术成果的系统汇编，收录了作者1935—1944年间撰写的论文、调查报告、工作日记等不同类型文献。',
            'key_points': '河南古建筑调查笔记、建筑史研究论文、营造学社工作记录',
            'contributions': '刘敦桢先生学术思想的集中体现',
            'publisher': '中国建筑工业出版社',
            'edition': '第一版',
            'pages': 0,
            'cover_image': 'img/index/wenhua.jpg'
        },
        
        # 多卷本建筑史
        {
            'lid': 9,
            'lname': '中国古代建筑史 第一卷',
            'author': '中国建筑史编写组',
            'dynasty': '现代',
            'publish_year': 2003,
            'literature_type': 'textbook',
            'summary': '《中国古代建筑史》共五卷，是中国建筑史研究的集大成之作。第一卷涵盖原始社会、夏、商、周、秦、汉建筑，系统论述了中国建筑的起源和早期发展。',
            'key_points': '用现代科学方法进行传统建筑研究、各时期建筑的详细分析、大量实物资料',
            'contributions': '中国古代建筑史的权威巨著',
            'publisher': '中国建筑工业出版社',
            'edition': '第一版',
            'pages': 0,
            'cover_image': 'img/index/lishi.jpg'
        }
    ]
    
    # 批量创建文献记录
    for lit_data in literature_list:
        lit = ArchitecturalLiterature.objects.create(**lit_data)
        print(f"创建文献: {lit.lname}")
    
    print(f"\n成功初始化 {len(literature_list)} 条文献数据！")


if __name__ == '__main__':
    init_literature_data()

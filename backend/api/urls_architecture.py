from django.urls import re_path
from . import views_architecture as views
from .views_wordcloud import get_wordcloud_data

app_name = 'architecture'

urlpatterns = [
    # ========== 仪表盘统计 ==========
    re_path(r'^dashboard_stats/$', views.dashboard_stats, name="dashboard-stats"),

    # ========== 词云数据 ==========
    re_path(r'^wordcloud/$', get_wordcloud_data, name="wordcloud"),
    
    # ========== 古建筑 CRUD ==========
    re_path(r'^buildings/$', views.buildings_list, name="buildings-list"),
    re_path(r'^buildings/(?P<pk>\d+)/$', views.buildings_detail, name="buildings-detail"),
    re_path(r'^building/(?P<pk>\d+)/$', views.BuildingDetail.as_view(), name="building-detail"),
    re_path(r'^search/$', views.search_building, name="search-building"),
    re_path(r'^building-detail/$', views.get_building_detail, name="get-building-detail"),
    
    # ========== 朝代 CRUD ==========
    re_path(r'^dynasty/$', views.dynasty_list, name="dynasty-list"),
    re_path(r'^dynasty/(?P<pk>\d+)/$', views.dynasty_detail, name="dynasty-detail"),
    
    # ========== 地域 CRUD ==========
    re_path(r'^region/$', views.region_list, name="region-list"),
    re_path(r'^region/(?P<pk>\d+)/$', views.region_detail, name="region-detail"),
    
    # ========== 省份统计 API ==========
    re_path(r'^province_stats/$', views.province_stats, name="province-stats"),
    
    # ========== 结构类型 CRUD ==========
    re_path(r'^structure_type/$', views.structure_type_list, name="structure-type-list"),
    re_path(r'^structure_type/(?P<pk>\d+)/$', views.structure_type_detail, name="structure-type-detail"),
    
    # ========== 建筑元素 CRUD ==========
    re_path(r'^elements/$', views.element_list, name="element-list"),
    re_path(r'^elements/(?P<pk>\d+)/$', views.element_detail, name="element-detail"),
    
    # ========== 文献资料 CRUD ==========
    re_path(r'^literatures/$', views.literature_list, name="literature-list"),
    re_path(r'^literatures/(?P<pk>\d+)/$', views.get_literature_detail, name="literature-detail"),
    
    # ========== 可视化数据 ==========
    re_path(r'^buildings_by_dynasty/$', views.get_buildings_by_dynasty, name="buildings-by-dynasty"),
    re_path(r'^buildings_by_region/$', views.get_buildings_by_region, name="buildings-by-region"),
    re_path(r'^roof_type_distribution/$', views.get_roof_type_distribution, name="roof-distribution"),
    re_path(r'^timeline/$', views.get_timeline_data, name="timeline-data"),
    re_path(r'^charts_data/$', views.get_charts_data, name="charts-data"),
    
    # ========== 用户认证 ==========
    re_path(r'^register/$', views.register, name="register"),
    re_path(r'^login/$', views.login, name="login"),
    
    # ========== AI问答 ==========
    re_path(r'^chat/$', views.chat, name="chat"),
    
    # ========== 数据导出 ==========
    re_path(r'^export_all/$', views.export_all_data, name="export-all"),
    
    # ========== 个性化推荐 ==========
    re_path(r'^recommendations/$', views.get_recommendations, name="recommendations"),
    
    # ========== 旧版API兼容 ==========
    re_path(r'^update-list/$', views.update_building_list, name="update-building-list"),
    re_path(r'^element_detail/$', views.get_element_detail, name="element-detail"),
    re_path(r'^viz_examples/$', views.get_viz_examples, name="viz-examples"),
]

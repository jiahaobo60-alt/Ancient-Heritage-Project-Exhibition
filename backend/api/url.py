from django.urls import re_path
from . import views

# 必须加上，且同 project 下 urls 中的 namespace 同值
app_name = 'api'

urlpatterns = [
    re_path(r'^scenery/(?P<pk>\d+)$', views.scenery.as_view(), name="scenery"),
    re_path(r'^province/(?P<pk>\d+)$', views.province.as_view(), name="province"),
    re_path(r'^dynasty$', views.dynasty.as_view(), name="dynasty"),
    re_path(r'search', views.search, name="search"),
    re_path(r'updateList', views.updateList, name="updateList"),
    re_path(r'click', views.click, name="click"),
    re_path(r'map', views.map, name="map"),
    re_path(r'heatMap', views.heatMap, name="heatMap"),
    re_path(r'scatter', views.scatter, name="scatter"),
    re_path(r'getDynastyNum', views.getDynastyNum, name="getDynastyNum"),
    re_path(r'getRecommendation', views.getRecommendation, name="getRecommendation"),
    re_path(r'getBarChart', views.getBarChart, name="getBarChart"),
    re_path(r'getLineChart', views.getLineChart, name="getLineChart"),
    re_path(r'register', views.register, name="register"),
    re_path(r'details', views.details, name="details"),
    re_path(r'login', views.login, name="login"),
    re_path(r'chat', views.chat, name="chat"),
    re_path(r'get_weather', views.get_weather, name="get_weather"),
    re_path(r'viz-examples/', views.get_viz_examples, name="viz-examples"),
    re_path(r'scenery/', views.get_scenery_data, name="scenery-data"),
]
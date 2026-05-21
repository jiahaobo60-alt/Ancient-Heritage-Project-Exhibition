from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.decorators import api_view
from . import models
from . import serializers
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from openai import OpenAI
import json
import requests

class dynasty(generics.ListAPIView):
    """
    查看接口列表
    """
    queryset = models.Dynasty.objects.all()
    serializer_class = serializers.DynastySerializer


class province(generics.RetrieveAPIView):
    """
    查看接口详细
    """
    queryset = models.Province.objects.all()
    serializer_class = serializers.ProvinceSerializer


class scenery(generics.RetrieveUpdateDestroyAPIView):
    """
    更新接口内容
    """
    queryset = models.Scenery.objects.all()
    serializer_class = serializers.ScenerySerializer


@api_view(['POST'])
@csrf_exempt
def search(request):
    query = request.POST.get('input')
    results = models.Scenery.objects.filter(sname__icontains=query)
    sceneryList = []
    for obj in results:
        p = models.Province.objects.filter(pid=obj.pid)
        sceneryList.append({'sid': obj.sid,'sname': obj.sname, 'introduction': obj.introduction, 'pname':p[0].pname, 'lng':obj.longitude ,'lat':obj.latitude})
    response_data = {'results':sceneryList}
    return JsonResponse(response_data,safe=False)

@api_view(['POST'])
@csrf_exempt
def updateList(request):
    query = request.POST.get('input')
    results = models.Scenery.objects.filter(sname__icontains=query)
    sceneryList = []
    for obj in results:
        p = models.Province.objects.filter(pid=obj.pid)
        sceneryList.append({'sid': obj.sid,'sname': obj.sname})
    response_data = {'results':sceneryList}
    return JsonResponse(response_data,safe=False)

@api_view(['POST'])
@csrf_exempt
def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    like = request.POST.get('like')
    print(username,password,email,like)
    # 将注册信息存储到数据库
    user = models.Users(username=username, password=password,email=email,like=like)
    user.save()
    # 构建响应数据
    response_data = {'status': 'success', 'message': 'Registration successful.'}
    return JsonResponse(response_data)

@api_view(['POST'])
@csrf_exempt
def login(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    message = "所有字段都必须填写！"
    if username and password:  # 确保用户名和密码都不为空
        print(username,password)
        try:
            user = models.Users.objects.get(username=username)
            if user.password == password:
                return JsonResponse({'status': 'success', 'message': '登录成功', 'redirect_url': '/index/'})
            else:
                message = "密码不正确！"
                return JsonResponse({'status': 'error', 'message': message})
        except:
            message = "用户名不存在！"
            return JsonResponse({'status': 'error', 'message': message})
    return JsonResponse({'status': 'error', 'message': message})

@api_view(['POST'])
@csrf_exempt
def click(request):
    query = request.POST.get('input')
    result = models.Scenery.objects.filter(sid=query)
    p = models.Province.objects.filter(pid=result.pid)
    response_data = {'results':{'sid': result.sid,'sname': result.sname, 'introduction': result.introduction,'category': result.category, 'pname':p[0].pname}}
    return JsonResponse(response_data,safe=False)

@api_view(['POST'])
@csrf_exempt
def map(request):
    query = request.POST.get('province')
    p = models.Province.objects.get(pname=query)
    pro = p.pname
    sceneryInProvince = models.Scenery.objects.filter(pid=p.pid)
    dist = sceneryInProvince.values("sname").distinct()
    response_data = {}
    results= []
    for obj in sceneryInProvince:
        if {'sname':obj.sname} in dist:
            dist = dist.exclude(sname=obj.sname)
            results.append({'name': obj.sname,'longitude': obj.longitude, 'introduction': obj.introduction,'category': obj.category,'latitude': obj.latitude})

    response_data['results'] = results
    return JsonResponse(response_data,safe=False)


@api_view(['POST'])
@csrf_exempt
def getDynastyNum(request):
    query = request.POST.get('province')
    p = models.Province.objects.get(pname=query)
    sceneryInProvince = models.Scenery.objects.filter(pid=p.pid)
    shangzhou = sceneryInProvince.filter(did__in=[1,2])
    qinhan = sceneryInProvince.filter(did__in=[3,4])
    suitang = sceneryInProvince.filter(did__in=[5,6])
    songyuan = sceneryInProvince.filter(did__in=[7,8])
    mingqing = sceneryInProvince.filter(did__in=[9,10])
    results= [shangzhou.count(),qinhan.count(),suitang.count(),songyuan.count(),mingqing.count()]
    response_data ={}
    response_data['results'] = results
    return JsonResponse(response_data,safe=False)


@api_view(['POST'])
@csrf_exempt
def heatMap(request):
    # query = request.POST.get("token")
    res = models.Scenery.objects.all()
    response_data = {}
    results = []
    for obj in res:
        results.append({'name': obj.sname, 'longitude': obj.longitude, 'city': obj.city, 'latitude': obj.latitude})
    response_data['results'] = results
    return JsonResponse(response_data, safe=False)


@api_view(['POST'])
@csrf_exempt
def scatter(request):
    query = request.POST.get()
    res = models.Scenery.objects.all()
    response_data = {}
    results = []
    for obj in res:
        results.append({'name': obj.sname, 'longitude': obj.longitude, 'city': obj.city, 'latitude': obj.latitude})
    response_data['results'] = results
    return JsonResponse(response_data, safe=False)


@api_view(['POST'])
@csrf_exempt
def getRecommendation(request):
    query = request.POST.get()
    res = models.Scenery.objects.all()
    response_data = {}
    results = []
    for obj in res:
        results.append({'name': obj.sname, 'longitude': obj.longitude, 'city': obj.city, 'latitude': obj.latitude})
    response_data['results'] = results
    return JsonResponse(response_data, safe=False)


@api_view(['POST'])
@csrf_exempt
def getBarChart(request):
    query = request.POST.get('province')
    p = models.Province.objects.get(pname=query)
    sceneryInProvince = models.Scenery.objects.filter(pid=p.pid)
    category = ['传统体育、游艺与杂技','传统美术','民俗','传统舞蹈','传统戏剧','传统医药']
    results = []
    response_data = {}
    for index,c in enumerate(category):
        shangzhou = sceneryInProvince.filter(did__in=[1, 2],category=c)
        qinhan = sceneryInProvince.filter(did__in=[3, 4],category=c)
        suitang = sceneryInProvince.filter(did__in=[5, 6],category=c)
        songyuan = sceneryInProvince.filter(did__in=[7, 8],category=c)
        mingqing = sceneryInProvince.filter(did__in=[9, 10],category=c)
        results.extend([[index,0,shangzhou.count()],[index,1,qinhan.count()],[index,2,suitang.count()],[index,3,songyuan.count()],[index,4,mingqing.count()]])
    response_data['results'] = results
    print("收到前端请求省份：", query)
    print("匹配到的pid：", p.pid)
    print("该省非遗项目总数：", sceneryInProvince.count())
    return JsonResponse(response_data, safe=False)


@api_view(['POST'])
@csrf_exempt
def getLineChart(request):
    query = request.POST.get('province')
    p = models.Province.objects.get(pname=query)
    sceneryInProvince = models.Scenery.objects.filter(pid=p.pid)
    category = ['传统体育、游艺与杂技','传统美术','民俗','传统舞蹈','传统戏剧','传统医药']
    results = []
    response_data = {}
    for c in category:
        shangzhou = sceneryInProvince.filter(did__in=[1, 2],category=c)
        qinhan = sceneryInProvince.filter(did__in=[3, 4],category=c)
        suitang = sceneryInProvince.filter(did__in=[5, 6],category=c)
        songyuan = sceneryInProvince.filter(did__in=[7, 8],category=c)
        mingqing = sceneryInProvince.filter(did__in=[9, 10],category=c)
        results.append([shangzhou.count(),qinhan.count(),suitang.count(),songyuan.count(),mingqing.count()])
    response_data['results'] = results
    print("收到前端请求省份：", query)
    print("匹配到的pid：", p.pid)
    print("该省非遗项目总数：", sceneryInProvince.count())
    return JsonResponse(response_data, safe=False)

@api_view(['POST'])
@csrf_exempt
def getbbjson(request):
    with open('bb.json') as file:
        data = json.load(file)

    return JsonResponse(data, safe=False)

@api_view(['GET'])
@csrf_exempt
def details(request):
    query = request.GET.get('kw')
    print(query)
    queryset = models.Details.objects.filter(introduction__icontains=query)
    result = []
    for obj in queryset:
        details_id = obj.id
        one_intro = models.Introduction.objects.get(id=details_id)
        result.append({
            'project_id':one_intro.project_id,
            'number': one_intro.number,
            'public_time': one_intro.public_time,
            'category': one_intro.category,
            'type': one_intro.type,
            'district': one_intro.district,
            'protection_department': one_intro.protection_department,
            'name': obj.name,
            'introduction': obj.introduction})
    # print(result)
    result.sort(key=lambda x: x["introduction"].count(query), reverse=True)
    response_data = {'results': result}
    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False})


client = OpenAI(api_key="sk-66aa0630dbc74247b71fbd0d5bef0417", base_url="https://api.deepseek.com")

@api_view(['POST'])
@csrf_exempt
def chat(request):
    if request.method == "POST":
        try:
            # 获取前端传来的用户消息
            body = json.loads(request.body.decode('utf-8'))
            user_message = body.get('message')
            
            # 如果收到图片相关请求，返回提示
            if user_message and ('图片' in user_message or 'image' in user_message.lower()):
                return JsonResponse({
                    'reply': '抱歉，当前版本仅支持文字问答。如需分析图片，请使用支持多模态的模型。'
                })

            # 使用 DeepSeek API 获取模型的回复
            response = client.chat.completions.create(
                model="deepseek-chat",  # 使用 DeepSeek 的聊天模型（纯文本）
                messages=[
                    {"role": "system", "content": "你是一个关于中国古建筑的专业助手，基于梁思成《中国建筑史》提供知识解答。"},
                    {"role": "user", "content": user_message},
                ],
                stream=False
            )

            # 获取 AI 回复并返回
            bot_reply = response.choices[0].message.content

        except Exception as e:
            bot_reply = f"抱歉，出现了错误: {str(e)}"

        # 返回 AI 的回答
        return JsonResponse({'reply': bot_reply})

    return JsonResponse({'reply': '无效请求方式。'})

@api_view(['POST'])
@csrf_exempt
def get_weather(request):
    """
    根据经纬度获取城市和天气信息
    """
    if request.method == 'POST':
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        api_key = '0fdb5ad11f0b03de8709e35eff77d423'

        if not lat or not lng:
            return JsonResponse({'status': 'error', 'message': '缺少经纬度参数'})

        try:
            # 1. 调用逆地理编码API获取城市信息
            regeo_url = f'https://restapi.amap.com/v3/geocode/regeo?location={lng},{lat}&key={api_key}&extensions=base'
            regeo_response = requests.get(regeo_url)
            regeo_data = regeo_response.json()

            if regeo_data and regeo_data.get('status') == '1' and regeo_data.get('regeocode') and regeo_data['regeocode'].get('addressComponent'):
                adcode = regeo_data['regeocode']['addressComponent'].get('adcode')
                city = regeo_data['regeocode']['addressComponent'].get('city') or regeo_data['regeocode']['addressComponent'].get('province')

                if adcode:
                    # 2. 使用城市编码调用天气查询API
                    weather_url = f'https://restapi.amap.com/v3/weather/weatherInfo?city={adcode}&key={api_key}&extensions=base'
                    weather_response = requests.get(weather_url)
                    weather_data = weather_response.json()

                    if weather_data and weather_data.get('status') == '1' and weather_data.get('lives') and len(weather_data['lives']) > 0:
                        live_weather = weather_data['lives'][0]
                        weather_info = {
                            'city': city,
                            'weather': live_weather.get('weather'),
                            'temperature': live_weather.get('temperature')
                        }
                        return JsonResponse({'status': 'success', 'weather': weather_info})
                    else:
                        return JsonResponse({'status': 'error', 'message': '无法获取天气数据'})
                else:
                    return JsonResponse({'status': 'error', 'message': '无法获取城市编码'})
            else:
                return JsonResponse({'status': 'error', 'message': '无法获取城市信息'})

        except requests.exceptions.RequestException as e:
            return JsonResponse({'status': 'error', 'message': f'API请求失败: {str(e)}'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'服务器内部错误: {str(e)}'})

    return JsonResponse({'status': 'error', 'message': '无效请求方式。'})


@api_view(['GET'])
@csrf_exempt
def get_viz_examples(request):
    """
    获取数据可视化案例
    """
    try:
        import os
        import json
        # 读取本地的 viz_examples.json 文件
        file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'frontend', 'data', 'viz_examples.json')
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['GET'])
@csrf_exempt
def get_scenery_data(request):
    """
    获取所有建筑数据用于可视化
    """
    try:
        scenery_list = models.Scenery.objects.all()
        results = []
        
        for scenery in scenery_list:
            # 获取朝代名称
            dynasty_name = ''
            try:
                dynasty = models.Dynasty.objects.get(did=scenery.did)
                dynasty_name = dynasty.dname
            except:
                dynasty_name = '未知'
            
            # 获取地区名称
            province_name = ''
            try:
                province = models.Province.objects.get(pid=scenery.pid)
                province_name = province.pname
            except:
                province_name = '未知'
            
            # 获取分类名称
            category_name = scenery.category or '未知'
            
            results.append({
                'sid': scenery.sid,
                'sname': scenery.sname,
                'dynasty_name': dynasty_name,
                'province_name': province_name,
                'category': category_name,
                'introduction': scenery.introduction,
                'city': scenery.city,
                'longitude': float(scenery.longitude) if scenery.longitude else None,
                'latitude': float(scenery.latitude) if scenery.latitude else None
            })
        
        return JsonResponse(results, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

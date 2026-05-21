from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.decorators import api_view
from . import models_architecture as models
from . import serializers_architecture as serializers
from django.shortcuts import render, redirect
import json
import requests
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.http import JsonResponse


# ==================== 古建筑 CRUD API ====================

@api_view(['GET', 'POST'])
def buildings_list(request):
    """古建筑列表 - GET查询 / POST创建"""
    if request.method == 'GET':
        buildings = models.AncientBuilding.objects.select_related(
            'dynasty', 'region', 'structure_type'
        ).all()
        
        # 支持筛选
        dynasty_id = request.GET.get('dynasty')
        region_id = request.GET.get('region')
        structure_type_id = request.GET.get('type')
        search = request.GET.get('search')
        
        if dynasty_id:
            buildings = buildings.filter(dynasty_id=dynasty_id)
        if region_id:
            buildings = buildings.filter(region_id=region_id)
        if structure_type_id:
            buildings = buildings.filter(structure_type_id=structure_type_id)
        if search:
            buildings = buildings.filter(bname__icontains=search)
        
        building_list = []
        for building in buildings:
            building_list.append({
                'bid': building.bid,
                'bname': building.bname,
                'dynasty_id': building.dynasty.did,
                'dynasty_name': building.dynasty.dname,
                'region_id': building.region.rid,
                'region_name': building.region.rname,
                'structure_type_id': building.structure_type.tid,
                'structure_type_name': building.structure_type.tname,
                'roof_type': building.roof_type,
                'dougong_style': building.dougong_style,
                'introduction': building.introduction,
                'historical_value': building.historical_value,
                'architectural_features': building.architectural_features,
                'liang_sicheng_note': building.liang_sicheng_note,
                'longitude': float(building.longitude) if building.longitude else 0,
                'latitude': float(building.latitude) if building.latitude else 0,
                'address': building.address,
                'image_url': building.image_url,
                'model_3d_url': building.model_3d_url
            })
        return JsonResponse({'results': building_list, 'total': len(building_list)})
    
    elif request.method == 'POST':
        try:
            data = request.data
            # 获取下一个 bid
            max_bid = models.AncientBuilding.objects.order_by('-bid').first()
            next_bid = (max_bid.bid + 1) if max_bid else 1
            
            building = models.AncientBuilding.objects.create(
                bid=next_bid,
                bname=data.get('bname'),
                dynasty_id=data.get('dynasty_id'),
                region_id=data.get('region_id'),
                structure_type_id=data.get('structure_type_id'),
                roof_type=data.get('roof_type', ''),
                dougong_style=data.get('dougong_style', ''),
                longitude=float(data.get('longitude', 0)),
                latitude=float(data.get('latitude', 0)),
                address=data.get('address', ''),
                introduction=data.get('introduction', ''),
                historical_value=data.get('historical_value', ''),
                architectural_features=data.get('architectural_features', ''),
                liang_sicheng_note=data.get('liang_sicheng_note', ''),
                image_url=data.get('image_url', ''),
                model_3d_url=data.get('model_3d_url', '')
            )
            return JsonResponse({'success': True, 'bid': building.bid, 'message': '创建成功'}, status=201)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def buildings_detail(request, pk):
    """古建筑详情 - GET查询 / PUT更新 / DELETE删除"""
    try:
        building = models.AncientBuilding.objects.select_related(
            'dynasty', 'region', 'structure_type'
        ).get(bid=pk)
    except models.AncientBuilding.DoesNotExist:
        return JsonResponse({'error': '建筑不存在'}, status=404)
    
    if request.method == 'GET':
        return JsonResponse({
            'bid': building.bid,
            'bname': building.bname,
            'dynasty_id': building.dynasty.did,
            'dynasty_name': building.dynasty.dname,
            'region_id': building.region.rid,
            'region_name': building.region.rname,
            'structure_type_id': building.structure_type.tid,
            'structure_type_name': building.structure_type.tname,
            'roof_type': building.roof_type,
            'dougong_style': building.dougong_style,
            'longitude': float(building.longitude) if building.longitude else 0,
            'latitude': float(building.latitude) if building.latitude else 0,
            'address': building.address,
            'introduction': building.introduction,
            'historical_value': building.historical_value,
            'architectural_features': building.architectural_features,
            'liang_sicheng_note': building.liang_sicheng_note,
            'image_url': building.image_url,
            'model_3d_url': building.model_3d_url
        })
    
    elif request.method == 'PUT':
        try:
            data = request.data
            building.bname = data.get('bname', building.bname)
            if data.get('dynasty_id'):
                building.dynasty_id = data['dynasty_id']
            if data.get('region_id'):
                building.region_id = data['region_id']
            if data.get('structure_type_id'):
                building.structure_type_id = data['structure_type_id']
            building.roof_type = data.get('roof_type', building.roof_type)
            building.dougong_style = data.get('dougong_style', building.dougong_style)
            if data.get('longitude') is not None:
                building.longitude = float(data['longitude'])
            if data.get('latitude') is not None:
                building.latitude = float(data['latitude'])
            building.address = data.get('address', building.address)
            building.introduction = data.get('introduction', building.introduction)
            building.historical_value = data.get('historical_value', building.historical_value)
            building.architectural_features = data.get('architectural_features', building.architectural_features)
            building.liang_sicheng_note = data.get('liang_sicheng_note', building.liang_sicheng_note)
            building.image_url = data.get('image_url', building.image_url)
            building.model_3d_url = data.get('model_3d_url', building.model_3d_url)
            building.save()
            return JsonResponse({'success': True, 'message': '更新成功'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    
    elif request.method == 'DELETE':
        building.delete()
        return JsonResponse({'success': True, 'message': '删除成功'}, status=204)


# ==================== 朝代 CRUD API ====================

@api_view(['GET', 'POST'])
def dynasty_list(request):
    """朝代列表 - GET查询 / POST创建"""
    if request.method == 'GET':
        dynasties = models.ArchDynasty.objects.all()
        dynasty_list = [{
            'did': d.did,
            'dname': d.dname,
            'period': d.period,
            'description': d.description
        } for d in dynasties]
        return JsonResponse({'results': dynasty_list, 'total': len(dynasty_list)})
    
    elif request.method == 'POST':
        try:
            data = request.data
            max_did = models.ArchDynasty.objects.order_by('-did').first()
            next_did = (max_did.did + 1) if max_did else 1
            
            dynasty = models.ArchDynasty.objects.create(
                did=next_did,
                dname=data.get('dname'),
                period=data.get('period', ''),
                description=data.get('description', '')
            )
            return JsonResponse({'success': True, 'did': dynasty.did}, status=201)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def dynasty_detail(request, pk):
    """朝代详情"""
    try:
        dynasty = models.ArchDynasty.objects.get(did=pk)
    except models.ArchDynasty.DoesNotExist:
        return JsonResponse({'error': '朝代不存在'}, status=404)
    
    if request.method == 'GET':
        return JsonResponse({
            'did': dynasty.did,
            'dname': dynasty.dname,
            'period': dynasty.period,
            'description': dynasty.description
        })
    elif request.method == 'PUT':
        data = request.data
        dynasty.dname = data.get('dname', dynasty.dname)
        dynasty.period = data.get('period', dynasty.period)
        dynasty.description = data.get('description', dynasty.description)
        dynasty.save()
        return JsonResponse({'success': True})
    elif request.method == 'DELETE':
        dynasty.delete()
        return JsonResponse({'success': True}, status=204)


# ==================== 地域 CRUD API ====================

@api_view(['GET', 'POST'])
def region_list(request):
    """地域列表"""
    if request.method == 'GET':
        regions = models.ArchRegion.objects.all()
        region_list = [{
            'rid': r.rid,
            'rname': r.rname,
            'description': r.description
        } for r in regions]
        return JsonResponse({'results': region_list, 'total': len(region_list)})
    
    elif request.method == 'POST':
        try:
            data = request.data
            max_rid = models.ArchRegion.objects.order_by('-rid').first()
            next_rid = (max_rid.rid + 1) if max_rid else 1
            
            region = models.ArchRegion.objects.create(
                rid=next_rid,
                rname=data.get('rname'),
                description=data.get('description', '')
            )
            return JsonResponse({'success': True, 'rid': region.rid}, status=201)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def region_detail(request, pk):
    """地域详情"""
    try:
        region = models.ArchRegion.objects.get(rid=pk)
    except models.ArchRegion.DoesNotExist:
        return JsonResponse({'error': '地域不存在'}, status=404)
    
    if request.method == 'GET':
        return JsonResponse({
            'rid': region.rid,
            'rname': region.rname,
            'description': region.description
        })
    elif request.method == 'PUT':
        data = request.data
        region.rname = data.get('rname', region.rname)
        region.description = data.get('description', region.description)
        region.save()
        return JsonResponse({'success': True})
    elif request.method == 'DELETE':
        region.delete()
        return JsonResponse({'success': True}, status=204)


# ==================== 省份统计 API ====================

@api_view(['GET'])
def province_stats(request):
    """省份古建筑统计数据 - 从province表获取"""
    from django.db import connection
    
    cursor = connection.cursor()
    
    # 获取省份数据（包含count字段）
    cursor.execute('SELECT pid, pname, count FROM province WHERE count > 0 ORDER BY count DESC')
    provinces = cursor.fetchall()
    
    province_list = [{
        'pid': p[0],
        'pname': p[1],
        'count': p[2]
    } for p in provinces]
    
    return JsonResponse({'results': province_list, 'total': len(province_list)})


# ==================== 结构类型 CRUD API ====================

@api_view(['GET', 'POST'])
def structure_type_list(request):
    """结构类型列表"""
    if request.method == 'GET':
        types = models.ArchStructureType.objects.all()
        type_list = [{
            'tid': t.tid,
            'tname': t.tname,
            'description': t.description
        } for t in types]
        return JsonResponse({'results': type_list, 'total': len(type_list)})
    
    elif request.method == 'POST':
        try:
            data = request.data
            max_tid = models.ArchStructureType.objects.order_by('-tid').first()
            next_tid = (max_tid.tid + 1) if max_tid else 1
            
            stype = models.ArchStructureType.objects.create(
                tid=next_tid,
                tname=data.get('tname'),
                description=data.get('description', '')
            )
            return JsonResponse({'success': True, 'tid': stype.tid}, status=201)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def structure_type_detail(request, pk):
    """结构类型详情"""
    try:
        stype = models.ArchStructureType.objects.get(tid=pk)
    except models.ArchStructureType.DoesNotExist:
        return JsonResponse({'error': '类型不存在'}, status=404)
    
    if request.method == 'GET':
        return JsonResponse({
            'tid': stype.tid,
            'tname': stype.tname,
            'description': stype.description
        })
    elif request.method == 'PUT':
        data = request.data
        stype.tname = data.get('tname', stype.tname)
        stype.description = data.get('description', stype.description)
        stype.save()
        return JsonResponse({'success': True})
    elif request.method == 'DELETE':
        stype.delete()
        return JsonResponse({'success': True}, status=204)


# ==================== 建筑元素 CRUD API ====================

@api_view(['GET', 'POST'])
def element_list(request):
    """建筑元素列表"""
    if request.method == 'GET':
        category = request.GET.get('category')
        if category:
            elements = models.ArchitecturalElement.objects.filter(category=category)
        else:
            elements = models.ArchitecturalElement.objects.all()
        
        element_list = [{
            'eid': e.eid,
            'ename': e.ename,
            'category': e.category,
            'explanation': e.explanation[:200] + '...' if len(e.explanation) > 200 else e.explanation,
            'image_url': e.image_url
        } for e in elements]
        return JsonResponse({'results': element_list, 'total': len(element_list)})
    
    elif request.method == 'POST':
        try:
            data = request.data
            max_eid = models.ArchitecturalElement.objects.order_by('-eid').first()
            next_eid = (max_eid.eid + 1) if max_eid else 1
            
            element = models.ArchitecturalElement.objects.create(
                eid=next_eid,
                ename=data.get('ename'),
                category=data.get('category'),
                original_text=data.get('original_text', ''),
                explanation=data.get('explanation', ''),
                structure_description=data.get('structure_description', ''),
                function_description=data.get('function_description', ''),
                evolution=data.get('evolution', ''),
                image_url=data.get('image_url', ''),
                diagram_url=data.get('diagram_url', '')
            )
            return JsonResponse({'success': True, 'eid': element.eid}, status=201)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def element_detail(request, pk):
    """建筑元素详情"""
    try:
        element = models.ArchitecturalElement.objects.get(eid=pk)
    except models.ArchitecturalElement.DoesNotExist:
        return JsonResponse({'error': '元素不存在'}, status=404)
    
    if request.method == 'GET':
        return JsonResponse({
            'eid': element.eid,
            'ename': element.ename,
            'category': element.category,
            'original_text': element.original_text,
            'explanation': element.explanation,
            'structure_description': element.structure_description,
            'function_description': element.function_description,
            'evolution': element.evolution,
            'image_url': element.image_url,
            'diagram_url': element.diagram_url
        })
    elif request.method == 'PUT':
        data = request.data
        element.ename = data.get('ename', element.ename)
        element.category = data.get('category', element.category)
        element.original_text = data.get('original_text', element.original_text)
        element.explanation = data.get('explanation', element.explanation)
        element.structure_description = data.get('structure_description', element.structure_description)
        element.function_description = data.get('function_description', element.function_description)
        element.evolution = data.get('evolution', element.evolution)
        element.image_url = data.get('image_url', element.image_url)
        element.diagram_url = data.get('diagram_url', element.diagram_url)
        element.save()
        return JsonResponse({'success': True})
    elif request.method == 'DELETE':
        element.delete()
        return JsonResponse({'success': True}, status=204)


# ==================== 文献资料 CRUD API ====================

@api_view(['GET', 'POST'])
def literature_list(request):
    """文献列表"""
    if request.method == 'GET':
        literatures = models.ArchitecturalLiterature.objects.all()
        lit_list = [{
            'lid': l.lid,
            'lname': l.lname,
            'author': l.author,
            'dynasty': l.dynasty,
            'publish_year': l.publish_year,
            'literature_type': l.literature_type,
            'literature_type_display': l.get_literature_type_display(),
            'summary': l.summary[:200] + '...' if len(l.summary) > 200 else l.summary,
            'cover_image': l.cover_image
        } for l in literatures]
        return JsonResponse({'results': lit_list, 'total': len(lit_list)})
    
    elif request.method == 'POST':
        try:
            data = request.data
            max_lid = models.ArchitecturalLiterature.objects.order_by('-lid').first()
            next_lid = (max_lid.lid + 1) if max_lid else 1
            
            literature = models.ArchitecturalLiterature.objects.create(
                lid=next_lid,
                lname=data.get('lname'),
                author=data.get('author'),
                dynasty=data.get('dynasty', ''),
                publish_year=data.get('publish_year'),
                literature_type=data.get('literature_type', 'modern'),
                summary=data.get('summary', ''),
                key_points=data.get('key_points', ''),
                contributions=data.get('contributions', ''),
                publisher=data.get('publisher', ''),
                edition=data.get('edition', ''),
                pages=data.get('pages'),
                cover_image=data.get('cover_image', ''),
                pdf_url=data.get('pdf_url', '')
            )
            return JsonResponse({'success': True, 'lid': literature.lid}, status=201)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)


# ==================== 仪表盘统计数据 API ====================

@api_view(['GET'])
def dashboard_stats(request):
    """仪表盘统计数据"""
    buildings = models.AncientBuilding.objects.select_related('dynasty', 'region', 'structure_type').all()
    
    # 总数统计
    total_buildings = buildings.count()
    total_dynasties = models.ArchDynasty.objects.count()
    total_regions = models.ArchRegion.objects.count()
    total_elements = models.ArchitecturalElement.objects.count()
    
    # 朝代分布
    dynasty_counts = {}
    for b in buildings:
        key = b.dynasty.dname
        dynasty_counts[key] = dynasty_counts.get(key, 0) + 1
    dynasty_data = [{'name': k, 'value': v} for k, v in dynasty_counts.items()]
    
    # 地域分布
    region_counts = {}
    for b in buildings:
        key = b.region.rname
        region_counts[key] = region_counts.get(key, 0) + 1
    region_data = [{'name': k, 'value': v} for k, v in region_counts.items()]
    
    # 屋顶形式分布
    roof_counts = {}
    for b in buildings:
        if b.roof_type:
            roof_counts[b.roof_type] = roof_counts.get(b.roof_type, 0) + 1
    roof_data = [{'name': k, 'value': v} for k, v in roof_counts.items()]
    
    # 结构类型分布
    type_counts = {}
    for b in buildings:
        key = b.structure_type.tname
        type_counts[key] = type_counts.get(key, 0) + 1
    type_data = [{'name': k, 'value': v} for k, v in type_counts.items()]
    
    # 散点数据（用于地图）
    scatter_data = [{
        'bid': b.bid,
        'bname': b.bname,
        'lon': float(b.longitude) if b.longitude else 0,
        'lat': float(b.latitude) if b.latitude else 0,
        'dynasty': b.dynasty.dname,
        'region': b.region.rname,
        'image_url': b.image_url
    } for b in buildings]
    
    return JsonResponse({
        'total_buildings': total_buildings,
        'total_dynasties': total_dynasties,
        'total_regions': total_regions,
        'total_elements': total_elements,
        'dynasty_data': dynasty_data,
        'region_data': region_data,
        'roof_data': roof_data,
        'type_data': type_data,
        'scatter_data': scatter_data
    })


# ==================== 导出所有数据 API ====================

@api_view(['GET'])
def export_all_data(request):
    """导出所有数据用于备份"""
    buildings = models.AncientBuilding.objects.select_related('dynasty', 'region', 'structure_type').all()
    dynasties = models.ArchDynasty.objects.all()
    regions = models.ArchRegion.objects.all()
    structure_types = models.ArchStructureType.objects.all()
    elements = models.ArchitecturalElement.objects.all()
    
    return JsonResponse({
        'buildings': [{
            'bid': b.bid, 'bname': b.bname,
            'dynasty': b.dynasty.dname, 'region': b.region.rname,
            'structure_type': b.structure_type.tname,
            'roof_type': b.roof_type, 'longitude': float(b.longitude), 'latitude': float(b.latitude),
            'address': b.address, 'introduction': b.introduction,
            'image_url': b.image_url
        } for b in buildings],
        'dynasties': [{'did': d.did, 'dname': d.dname, 'period': d.period, 'description': d.description} for d in dynasties],
        'regions': [{'rid': r.rid, 'rname': r.rname, 'description': r.description} for r in regions],
        'structure_types': [{'tid': t.tid, 'tname': t.tname, 'description': t.description} for t in structure_types],
        'elements': [{'eid': e.eid, 'ename': e.ename, 'category': e.category, 'explanation': e.explanation} for e in elements]
    })


# ==================== 古建筑基础API ====================

class DynastyList(generics.ListAPIView):
    """朝代列表API"""
    queryset = models.ArchDynasty.objects.all()
    serializer_class = serializers.DynastySerializer


class RegionList(generics.ListAPIView):
    """地域列表API"""
    queryset = models.ArchRegion.objects.all()
    serializer_class = serializers.RegionSerializer


class StructureTypeList(generics.ListAPIView):
    """结构类型列表API"""
    queryset = models.ArchStructureType.objects.all()
    serializer_class = serializers.StructureTypeSerializer


class BuildingDetail(generics.RetrieveUpdateDestroyAPIView):
    """古建筑详情API"""
    queryset = models.AncientBuilding.objects.all()
    serializer_class = serializers.BuildingSerializer


class DynastyDetail(generics.RetrieveUpdateDestroyAPIView):
    """朝代详情API"""
    queryset = models.ArchDynasty.objects.all()
    serializer_class = serializers.DynastySerializer


class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    """地域详情API"""
    queryset = models.ArchRegion.objects.all()
    serializer_class = serializers.RegionSerializer


class StructureTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    """结构类型详情API"""
    queryset = models.ArchStructureType.objects.all()
    serializer_class = serializers.StructureTypeSerializer


# ==================== 搜索与查询API ====================

@api_view(['GET'])
def get_buildings(request):
    """获取建筑列表"""
    buildings = models.AncientBuilding.objects.all()
    
    # 支持筛选
    dynasty_id = request.GET.get('dynasty')
    region_id = request.GET.get('region')
    structure_type_id = request.GET.get('type')
    
    if dynasty_id:
        buildings = buildings.filter(dynasty_id=dynasty_id)
    if region_id:
        buildings = buildings.filter(region_id=region_id)
    if structure_type_id:
        buildings = buildings.filter(structure_type_id=structure_type_id)
    
    building_list = []
    for building in buildings:
        building_list.append({
            'bid': building.bid,
            'bname': building.bname,
            'dynasty': building.dynasty.did,
            'dynasty_name': building.dynasty.dname,
            'region': building.region.rid,
            'region_name': building.region.rname,
            'structure_type': building.structure_type.tid,
            'structure_type_name': building.structure_type.tname,
            'roof_type': building.roof_type,
            'dougong_style': building.dougong_style,
            'introduction': building.introduction,
            'historical_value': building.historical_value,
            'architectural_features': building.architectural_features,
            'liang_sicheng_note': building.liang_sicheng_note,
            'longitude': building.longitude,
            'latitude': building.latitude,
            'address': building.address,
            'image_url': building.image_url,
            'model_3d_url': building.model_3d_url
        })
    return JsonResponse({'results': building_list})

@api_view(['POST'])
@csrf_exempt
def search_building(request):
    """搜索古建筑"""
    query = request.POST.get('input')
    results = models.AncientBuilding.objects.filter(bname__icontains=query)
    building_list = []
    for obj in results:
        building_list.append({
            'bid': obj.bid,
            'bname': obj.bname,
            'dynasty': obj.dynasty.dname,
            'region': obj.region.rname,
            'structure_type': obj.structure_type.tname,
            'roof_type': obj.roof_type,
            'introduction': obj.introduction,
            'longitude': obj.longitude,
            'latitude': obj.latitude,
            'image_url': obj.image_url
        })
    return JsonResponse({'results': building_list}, safe=False)


@api_view(['POST'])
@csrf_exempt
def update_building_list(request):
    """更新古建筑列表（用于自动完成）"""
    query = request.POST.get('input')
    results = models.AncientBuilding.objects.filter(bname__icontains=query)
    building_list = []
    for obj in results:
        building_list.append({
            'bid': obj.bid,
            'bname': obj.bname
        })
    return JsonResponse({'results': building_list}, safe=False)


@api_view(['POST'])
@csrf_exempt
def get_building_detail(request):
    """获取古建筑详情"""
    bid = request.POST.get('bid')
    try:
        building = models.AncientBuilding.objects.get(bid=bid)
        detail = {
            'bid': building.bid,
            'bname': building.bname,
            'dynasty': building.dynasty.dname,
            'region': building.region.rname,
            'structure_type': building.structure_type.tname,
            'roof_type': building.roof_type,
            'dougong_style': building.dougong_style,
            'introduction': building.introduction,
            'historical_value': building.historical_value,
            'architectural_features': building.architectural_features,
            'liang_sicheng_note': building.liang_sicheng_note,
            'longitude': building.longitude,
            'latitude': building.latitude,
            'image_url': building.image_url,
            'model_3d_url': building.model_3d_url
        }
        return JsonResponse({'results': detail})
    except models.AncientBuilding.DoesNotExist:
        return JsonResponse({'error': '建筑不存在'}, status=404)


# ==================== 建筑元素知识库API ====================

@api_view(['GET'])
def get_architectural_elements(request):
    """获取建筑元素列表"""
    category = request.GET.get('category', '')
    if category:
        elements = models.ArchitecturalElement.objects.filter(category=category)
    else:
        elements = models.ArchitecturalElement.objects.all()
    
    element_list = []
    for elem in elements:
        element_list.append({
            'eid': elem.eid,
            'ename': elem.ename,
            'category': elem.category,
            'explanation': elem.explanation[:200] + '...' if len(elem.explanation) > 200 else elem.explanation,
            'image_url': elem.image_url
        })
    return JsonResponse({'results': element_list})


@api_view(['GET'])
def get_element_detail(request):
    """获取建筑元素详情"""
    eid = request.GET.get('eid')
    try:
        elem = models.ArchitecturalElement.objects.get(eid=eid)
        detail = {
            'eid': elem.eid,
            'ename': elem.ename,
            'category': elem.category,
            'original_text': elem.original_text,
            'explanation': elem.explanation,
            'structure_description': elem.structure_description,
            'function_description': elem.function_description,
            'evolution': elem.evolution,
            'image_url': elem.image_url,
            'diagram_url': elem.diagram_url
        }
        return JsonResponse({'results': detail})
    except models.ArchitecturalElement.DoesNotExist:
        return JsonResponse({'error': '元素不存在'}, status=404)


# ==================== 可视化数据API ====================

@api_view(['GET'])
def get_buildings_by_dynasty(request):
    """按朝代统计古建筑分布"""
    dynasty_id = request.GET.get('dynasty_id')
    if dynasty_id:
        buildings = models.AncientBuilding.objects.filter(dynasty_id=dynasty_id)
    else:
        buildings = models.AncientBuilding.objects.all()
    
    data = []
    for building in buildings:
        data.append({
            'name': building.bname,
            'value': [building.longitude, building.latitude, building.bname],
            'dynasty': building.dynasty.dname,
            'region': building.region.rname
        })
    return JsonResponse({'results': data})


@api_view(['GET'])
def get_buildings_by_region(request):
    """按地域统计古建筑分布"""
    region_id = request.GET.get('region_id')
    if region_id:
        buildings = models.AncientBuilding.objects.filter(region_id=region_id)
    else:
        buildings = models.AncientBuilding.objects.all()
    
    region_stats = {}
    for building in buildings:
        region_name = building.region.rname
        if region_name not in region_stats:
            region_stats[region_name] = 0
        region_stats[region_name] += 1
    
    data = [{'name': k, 'value': v} for k, v in region_stats.items()]
    return JsonResponse({'results': data})


@api_view(['GET'])
def get_roof_type_distribution(request):
    """获取屋顶形式分布统计"""
    buildings = models.AncientBuilding.objects.exclude(roof_type='')
    roof_stats = {}
    for building in buildings:
        roof_type = building.roof_type
        if roof_type not in roof_stats:
            roof_stats[roof_type] = 0
        roof_stats[roof_type] += 1
    
    data = [{'name': k, 'value': v} for k, v in roof_stats.items()]
    return JsonResponse({'results': data})


@api_view(['GET'])
def get_timeline_data(request):
    """获取时间轴数据"""
    buildings = models.AncientBuilding.objects.all().order_by('dynasty__did')
    timeline_data = []
    for building in buildings:
        timeline_data.append({
            'bid': building.bid,
            'bname': building.bname,
            'dynasty': building.dynasty.dname,
            'period': building.dynasty.period,
            'region': building.region.rname,
            'image_url': building.image_url,
            'introduction': building.introduction[:100] + '...'
        })
    return JsonResponse({'results': timeline_data})


# ==================== 个性化推荐API ====================

@api_view(['POST'])
@csrf_exempt
def get_recommendations(request):
    """基于用户偏好获取推荐"""
    # 获取用户偏好参数
    dynasty_prefs = request.POST.getlist('dynasty_prefs[]', [])
    region_prefs = request.POST.getlist('region_prefs[]', [])
    type_prefs = request.POST.getlist('type_prefs[]', [])
    
    buildings = models.AncientBuilding.objects.all()
    
    # 根据偏好筛选
    if dynasty_prefs:
        buildings = buildings.filter(dynasty__dname__in=dynasty_prefs)
    if region_prefs:
        buildings = buildings.filter(region__rname__in=region_prefs)
    if type_prefs:
        buildings = buildings.filter(structure_type__tname__in=type_prefs)
    
    # 如果没有偏好，返回热门建筑
    if not buildings.exists():
        buildings = models.AncientBuilding.objects.all()[:10]
    
    result = []
    for building in buildings[:10]:
        result.append({
            'bid': building.bid,
            'bname': building.bname,
            'dynasty': building.dynasty.dname,
            'region': building.region.rname,
            'structure_type': building.structure_type.tname,
            'introduction': building.introduction[:150] + '...',
            'image_url': building.image_url
        })
    
    return JsonResponse({'results': result})


# ==================== 用户认证API ====================

@api_view(['POST'])
@csrf_exempt
def register(request):
    """用户注册"""
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    like = request.POST.get('like', '')
    
    if models.ArchUsers.objects.filter(username=username).exists():
        return JsonResponse({'status': 'error', 'message': '用户名已存在'})
    
    user = models.ArchUsers(username=username, password=password, email=email, like=like)
    user.save()
    return JsonResponse({'status': 'success', 'message': '注册成功'})


@api_view(['POST'])
@csrf_exempt
def login(request):
    """用户登录"""
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    if not username or not password:
        return JsonResponse({'status': 'error', 'message': '请填写所有字段'})
    
    try:
        user = models.ArchUsers.objects.get(username=username)
        if user.password == password:
            return JsonResponse({
                'status': 'success', 
                'message': '登录成功',
                'user_id': user.id,
                'username': user.username
            })
        else:
            return JsonResponse({'status': 'error', 'message': '密码错误'})
    except models.ArchUsers.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': '用户不存在'})


# ==================== AI问答API ====================

@api_view(['POST'])
@csrf_exempt
def chat(request):
    """AI问答接口 - 支持古建筑知识问答"""
    import json
    
    try:
        # 解析JSON请求体
        if request.content_type == 'application/json':
            data = json.loads(request.body.decode('utf-8'))
        else:
            data = request.POST
        
        user_message = data.get('message', '').strip()
        building = data.get('building', '')
        context = data.get('context', '古建筑知识问答')
        
        if not user_message:
            return JsonResponse({'status': 'error', 'message': '请输入问题'}, status=400)
        
        # 智能回复逻辑（模拟AI）
        reply = generate_smart_reply(user_message, building, context)
        
        return JsonResponse({
            'status': 'success',
            'reply': reply,
            'building': building,
            'context': context
        })
        
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f'AI服务异常: {str(e)}'
        }, status=500)


def generate_smart_reply(message, building=None, context=None):
    """智能回复生成器（模拟AI，可替换为真实大模型API）"""
    import re
    
    msg_lower = message.lower()
    
    # 斗拱相关问题
    if re.search(r'斗拱|斗栱', msg_lower):
        return ('斗拱是中国古建筑特有的结构构件，由斗、拱、昂等部件组成。它不仅具有承重、悬挑的结构功能，还具有装饰作用。'
               '梁思成先生在《中国建筑史》中详细描述了斗拱的演变过程：唐代斗拱雄大有力，宋代斗拱精巧华丽，明清斗拱趋于装饰化。'
               + (building and f'您提到的{building}，其斗拱是{get_dynasty_by_building(building)}时期的典型代表。' or ''))
    
    # 屋顶相关问题
    if re.search(r'屋顶|庑殿|歇山|悬山|硬山', msg_lower):
        return ('中国古建筑屋顶形式丰富，主要有庑殿顶、歇山顶、悬山顶、硬山顶、攒尖顶等。'
               '庑殿顶等级最高，五脊四坡，常用于皇家重要建筑；歇山顶次之，九脊二坡，应用最广泛。'
               '屋顶的坡度、脊饰、瓦件都有严格的等级制度，体现了中国古代的礼制思想。')
    
    # 木结构相关问题
    if re.search(r'木构|榫卯|结构', msg_lower):
        return ('中国古建筑以木结构为主，采用榫卯连接，不用一钉一铆。'
               '主要结构形式有抬梁式、穿斗式、井干式。'
               '这种柔性结构具有良好的抗震性能，体现了"墙倒屋不塌"的特点。')
    
    # 朝代相关问题
    if re.search(r'唐代|唐朝|唐', msg_lower):
        return ('唐代建筑的特点是气魄宏伟、严整开朗。'
               '代表建筑有山西五台山的佛光寺东大殿、南禅寺大殿等。'
               '唐代斗拱雄大有力，出檐深远，屋顶坡度平缓，整体风格雄浑庄重。')
    
    if re.search(r'宋代|宋朝|宋', msg_lower):
        return ('宋代建筑的特点是精巧秀丽、注重装饰。'
               '斗拱尺寸减小，出现真昂与假昂，屋顶坡度变陡，建筑风格更加柔和细腻。'
               '代表建筑有晋祠圣母殿、隆兴寺摩尼殿等。')
    
    if re.search(r'明代|明朝|明', msg_lower):
        return ('明代建筑的特点是制度化、标准化。'
               '斗拱比例缩小，装饰性增强，建筑规模宏大。'
               '官式建筑严格按照《营造法式》建造，地方建筑则保留了地域特色。')
    
    if re.search(r'清代|清朝|清', msg_lower):
        return ('清代建筑的特点是繁琐华丽、装饰性强。'
               '斗拱进一步缩小，成为纯粹的装饰构件，彩画工艺达到顶峰。'
               '代表建筑有北京故宫建筑群，体现了清代建筑的辉煌成就。')
    
    # 推荐建筑
    if re.search(r'推荐|介绍', msg_lower):
        if re.search(r'唐', msg_lower):
            return ('强烈推荐您参观佛光寺东大殿，这是中国现存最早的木构建筑之一，建于公元857年。' +
                   '其七铺作斗拱雄大有力，是唐代建筑的典范，被梁思成先生誉为"中国第一国宝"。')
        if re.search(r'宋', msg_lower):
            return ('推荐您参观晋祠圣母殿，体现了宋代建筑精巧细致的特点。' +
                   '重檐歇山顶，木雕精美，斗拱华丽，是宋代建筑的代表作品。')
        if re.search(r'明', msg_lower):
            return ('推荐您参观岳阳楼，盔顶结构独特，濒临洞庭湖，' +
                   '因范仲淹《岳阳楼记》而闻名，体现了明代楼阁建筑的高超技艺。')
        if re.search(r'清', msg_lower):
            return ('推荐您参观太和殿，中国现存最大的木结构大殿。' +
                   '重檐庑殿顶，金龙和玺彩画，体现了清代皇家建筑的辉煌成就。')
        
        return ('根据您的兴趣，我建议参观路线：\n' +
               '1. 佛光寺东大殿（唐代）- 了解中国最早的木构建筑\n' +
               '2. 应县木塔（辽代）- 世界最高木塔的抗震智慧\n' +
               '3. 太和殿（清代）- 感受皇家建筑的恢弘气势\n' +
               '4. 拙政园（明代）- 欣赏江南园林的精巧雅致')
    
    # 具体建筑问题
    if building:
        if re.search(r'特点|特色|特色|建筑|风格', msg_lower):
            dynasty = get_dynasty_by_building(building)
            features = get_building_features(building)
            return f'{building}是{dynasty}建筑的代表作品。{features}'
        
        if re.search(r'历史|年代|建造|时间', msg_lower):
            return (f'{building}建于{get_dynasty_by_building(building)}时期，{get_historical_desc(building)}。' +
                   '这座建筑承载了深厚的历史文化价值，是研究中国古代建筑的重要实例。')
    
    # 梁思成相关问题
    if re.search(r'梁思成|梁|营造法式', msg_lower):
        return ('梁思成（1901-1972）是中国著名建筑学家，被誉为"中国建筑史之父"。' +
               '他的《中国建筑史》是第一部由中国人自己编写的中国古代建筑史，' +
               '系统整理了中国古代建筑的发展历程、技术成就和艺术特色。' +
               '梁思成先生还参与了佛光寺、应县木塔等重要古建筑的调查与研究。')
    
    # 默认回复
    return ('感谢您的提问！' +
           (building and f'关于{building}，我可以为您介绍：\n' +
            '• 建筑特色与结构特点\n' +
            '• 历史背景与文化价值\n' +
            '• 相关人物与历史事件\n' or '') +
           '您也可以问我：\n' +
           '• 斗拱的结构与演变\n' +
           '• 屋顶形式与等级制度\n' +
           '• 推荐参观路线\n' +
           '• 梁思成的建筑思想')


def get_dynasty_by_building(building_name):
    """根据建筑名称返回朝代"""
    dynasty_map = {
        '佛光寺': '唐代',
        '南禅寺': '唐代',
        '应县木塔': '辽代',
        '独乐寺': '辽代',
        '晋祠圣母殿': '宋代',
        '隆兴寺': '宋代',
        '岳阳楼': '明代',
        '滕王阁': '明代',
        '黄鹤楼': '明代',
        '太和殿': '清代',
        '避暑山庄': '清代',
        '颐和园': '清代',
        '拙政园': '明代',
        '云冈石窟': '魏晋南北朝',
        '敦煌莫高窟': '魏晋南北朝',
        '秦始皇陵': '汉代',
        '客家土楼': '明代',
        '长城': '明代'
    }
    
    for name, dynasty in dynasty_map.items():
        if name in building_name:
            return dynasty
    return '古代'


def get_building_features(building_name):
    """获取建筑特点描述"""
    features_map = {
        '佛光寺': '其七铺作斗拱雄大有力，是唐代建筑的典范，被梁思成誉为"中国第一国宝"。',
        '应县木塔': '世界现存最高、最古老的木塔，采用双层套筒结构，展现了辽代建筑的高超技艺。',
        '太和殿': '中国现存最大的木结构大殿，重檐庑殿顶，金龙和玺彩画，彰显皇家威严。',
        '岳阳楼': '盔顶结构独特，濒临洞庭湖，因范仲淹《岳阳楼记》而闻名，文化底蕴深厚。',
        '拙政园': '江南园林的代表，以水为中心，布局精巧，体现了明代园林建筑的艺术成就。'
    }
    
    for name, feature in features_map.items():
        if name in building_name:
            return feature
    return '具有重要的历史文化价值和建筑艺术价值。'


def get_historical_desc(building_name):
    """获取历史描述"""
    desc_map = {
        '佛光寺': '公元857年建造，历经千年风雨仍保存完好，是研究唐代建筑的珍贵实例',
        '应县木塔': '建于辽代，近千年来历经多次地震仍屹立不倒，展现了古代抗震智慧',
        '太和殿': '明清两代皇家重要典礼场所，见证了中国封建王朝的兴衰',
        '岳阳楼': '历代多次重建，承载着深厚的文化内涵，是中华文化的重要象征'
    }
    
    for name, desc in desc_map.items():
        if name in building_name:
            return desc
    return '历经千年传承，承载了深厚的历史文化内涵'


@api_view(['GET'])
def get_viz_examples(request):
    """数据可视化案例参考图片（前端可用的图片卡片集合）"""
    examples = [
        {
            'id': 'gapminder-logo',
            'title': 'Gapminder Logo',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/2/2f/Gapminder_Logo.jpg',
            'link': 'https://commons.wikimedia.org/wiki/File:Gapminder_Logo.jpg',
            'description': 'Gapminder 品牌标识'
        },
        {
            'id': 'gapminder-sample',
            'title': 'Gapminder Sample',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/6/6b/Gapminder_sample.png',
            'link': 'https://commons.wikimedia.org/wiki/File:Gapminder_sample.png',
            'description': 'Gapminder 示例数据图片'
        },
        {
            'id': 'ola-rosling',
            'title': 'Ola Rosling (Gapminder)',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/4/41/Ola_Rosling,_President_and_Co-Founder_of_Gapminder_Foundation.jpg',
            'link': 'https://commons.wikimedia.org/wiki/File:Ola_Rosling,_President_and_Co-Founder_of_Gapminder_Foundation.jpg',
            'description': 'Gapminder 创始人形象图片'
        },
        {
            'id': 'gapminder-world',
            'title': 'Gapminder World (示例)',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/5/5c/Gapminder.jpg',
            'link': 'https://commons.wikimedia.org/wiki/File:Gapminder.jpg',
            'description': 'Gapminder 世界地图示例图片'
        }
    ]
    return JsonResponse({'results': examples})


@api_view(['GET'])
def get_charts_data(request):
    """提供给前端的数据，包含散点数据与朝代分布（简易图表数据）"""
    buildings = models.AncientBuilding.objects.select_related('dynasty', 'region', 'structure_type').all()
    scatter = []
    dynasty_counts = {}
    for b in buildings:
        name = b.bname
        scatter.append({
            'bid': b.bid,
            'bname': name,
            'lon': b.longitude if b.longitude is not None else 0,
            'lat': b.latitude if b.latitude is not None else 0,
            'dynasty': b.dynasty.dname if b.dynasty else '未知',
            'region': b.region.rname if b.region else '',
            'structure_type': b.structure_type.tname if b.structure_type else ''
        })
        key = b.dynasty.dname if b.dynasty else '未知'
        dynasty_counts[key] = dynasty_counts.get(key, 0) + 1

    dynasties = [{'name': k, 'count': v} for k, v in dynasty_counts.items()]
    return JsonResponse({'scatter': scatter, 'dynasties': dynasties})


# ==================== 文献资料API ====================

@api_view(['GET'])
def get_literatures(request):
    """获取文献列表"""
    literatures = models.ArchitecturalLiterature.objects.all()
    
    # 支持按类型筛选
    lit_type = request.GET.get('type')
    if lit_type:
        literatures = literatures.filter(literature_type=lit_type)
    
    literature_list = []
    for lit in literatures:
        literature_list.append({
            'lid': lit.lid,
            'lname': lit.lname,
            'author': lit.author,
            'dynasty': lit.dynasty,
            'publish_year': lit.publish_year,
            'literature_type': lit.literature_type,
            'literature_type_display': lit.get_literature_type_display(),
            'summary': lit.summary,
            'key_points': lit.key_points,
            'contributions': lit.contributions,
            'publisher': lit.publisher,
            'edition': lit.edition,
            'pages': lit.pages,
            'cover_image': lit.cover_image,
            'pdf_url': lit.pdf_url
        })
    
    return JsonResponse({'results': literature_list})


@api_view(['GET'])
def get_literature_detail(request, lid):
    """获取文献详情"""
    try:
        lit = models.ArchitecturalLiterature.objects.get(lid=lid)
        
        # 获取相关建筑
        related_buildings = []
        for building in lit.related_buildings.all():
            related_buildings.append({
                'bid': building.bid,
                'bname': building.bname,
                'image_url': building.image_url
            })
        
        return JsonResponse({
            'lid': lit.lid,
            'lname': lit.lname,
            'author': lit.author,
            'dynasty': lit.dynasty,
            'publish_year': lit.publish_year,
            'literature_type': lit.literature_type,
            'literature_type_display': lit.get_literature_type_display(),
            'summary': lit.summary,
            'key_points': lit.key_points,
            'contributions': lit.contributions,
            'publisher': lit.publisher,
            'edition': lit.edition,
            'pages': lit.pages,
            'cover_image': lit.cover_image,
            'pdf_url': lit.pdf_url,
            'related_buildings': related_buildings
        })
    except models.ArchitecturalLiterature.DoesNotExist:
        return JsonResponse({'error': '文献不存在'}, status=404)

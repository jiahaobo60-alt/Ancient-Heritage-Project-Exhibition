from rest_framework import serializers
from . import models_architecture as models


class DynastySerializer(serializers.ModelSerializer):
    """朝代序列化器"""
    class Meta:
        model = models.ArchDynasty
        fields = ['did', 'dname', 'period', 'description']


class RegionSerializer(serializers.ModelSerializer):
    """地域序列化器"""
    class Meta:
        model = models.ArchRegion
        fields = ['rid', 'rname', 'description']


class StructureTypeSerializer(serializers.ModelSerializer):
    """结构类型序列化器"""
    class Meta:
        model = models.ArchStructureType
        fields = ['tid', 'tname', 'description']


class BuildingSerializer(serializers.ModelSerializer):
    """古建筑序列化器"""
    dynasty_name = serializers.CharField(source='dynasty.dname', read_only=True)
    region_name = serializers.CharField(source='region.rname', read_only=True)
    structure_type_name = serializers.CharField(source='structure_type.tname', read_only=True)
    
    class Meta:
        model = models.AncientBuilding
        fields = [
            'bid', 'bname', 'dynasty', 'dynasty_name', 'region', 'region_name',
            'structure_type', 'structure_type_name', 'roof_type', 'dougong_style',
            'longitude', 'latitude', 'address', 'introduction', 'historical_value',
            'architectural_features', 'liang_sicheng_note', 'image_url', 'model_3d_url'
        ]


class ArchitecturalElementSerializer(serializers.ModelSerializer):
    """建筑元素序列化器"""
    class Meta:
        model = models.ArchitecturalElement
        fields = [
            'eid', 'ename', 'category', 'original_text', 'explanation',
            'structure_description', 'function_description', 'evolution',
            'image_url', 'diagram_url'
        ]


class UserSerializer(serializers.ModelSerializer):
    """用户序列化器"""
    class Meta:
        model = models.ArchUsers
        fields = ['id', 'username', 'email', 'like', 'created_at']
        extra_kwargs = {'password': {'write_only': True}}

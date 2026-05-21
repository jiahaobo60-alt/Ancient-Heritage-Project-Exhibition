from rest_framework import serializers
from api.models import *


class DynastySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dynasty
        fields = "__all__"


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = "__all__"


class ScenerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenery
        fields = "__all__"
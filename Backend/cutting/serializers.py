from rest_framework import serializers
from .models import Cutting, Size, Material, Color, WorkTable, Reference, WorkShop, CuttingAssignment


class CuttingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cutting
        fields = '__all__'  # Serialize all fields of the Cutting model


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class WorkTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTable
        fields = '__all__'


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = '__all__'


class WorkShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkShop
        fields = '__all__'


class CuttingAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuttingAssignment
        fields = '__all__'

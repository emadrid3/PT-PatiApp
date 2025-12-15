from rest_framework import viewsets
from .models import Cutting, Size, Material, Color, WorkTable, Reference, WorkShop, CuttingAssignment
from .serializers import (
    CuttingSerializer,
    SizeSerializer,
    MaterialSerializer,
    ColorSerializer,
    WorkTableSerializer,
    ReferenceSerializer,
    WorkShopSerializer,
    CuttingAssignmentSerializer
)


class CuttingViewSet(viewsets.ModelViewSet):
    queryset = Cutting.objects.all()
    serializer_class = CuttingSerializer


class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class WorkTableViewSet(viewsets.ModelViewSet):
    queryset = WorkTable.objects.all()
    serializer_class = WorkTableSerializer


class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer


class WorkShopViewSet(viewsets.ModelViewSet):
    queryset = WorkShop.objects.all()
    serializer_class = WorkShopSerializer


class CuttingAssignmentViewSet(viewsets.ModelViewSet):
    queryset = CuttingAssignment.objects.all()
    serializer_class = CuttingAssignmentSerializer

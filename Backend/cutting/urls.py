from django.urls import path, include
from .views import CuttingViewSet, SizeViewSet, MaterialViewSet, ColorViewSet, WorkTableViewSet, ReferenceViewSet, WorkShopViewSet, CuttingAssignmentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cuttings', CuttingViewSet, basename='cutting')
router.register(r'sizes', SizeViewSet, basename='size')
router.register(r'materials', MaterialViewSet, basename='material')
router.register(r'colors', ColorViewSet, basename='color')
router.register(r'work-tables', WorkTableViewSet, basename='worktable')
router.register(r'references', ReferenceViewSet, basename='reference')
router.register(r'work-shops', WorkShopViewSet, basename='workshop')
router.register(r'cutting-assignments', CuttingAssignmentViewSet,
                basename='cuttingassignment')

urlpatterns = [
    path('', include(router.urls)),
]

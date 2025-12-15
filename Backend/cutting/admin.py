from django.contrib import admin
from .models import Cutting, Size, Material, Color, WorkTable, Reference, WorkShop, CuttingAssignment

admin.site.register(Cutting)
admin.site.register(Size)
admin.site.register(Material)
admin.site.register(Color)
admin.site.register(WorkTable)
admin.site.register(Reference)
admin.site.register(WorkShop)
admin.site.register(CuttingAssignment)

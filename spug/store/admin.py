from django.contrib import admin

# import models
from store.models import (Brand,
                          Manufacturer,
                          Product
                          )


class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'manufacturer', 'name', 'enabled']
    search_fields = ['id', 'name']
    list_filter = ['manufacturer', 'enabled']


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'name', 'enabled']
    search_fields = ['id', 'name']
    list_filter = ['enabled']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['sku', 'created_at', 'updated_at', 'brand', 'description', 'enabled']
    search_fields = ['sku', 'description']
    list_filter = ['brand', 'enabled']


# register models
admin.site.register(Brand, BrandAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Product, ProductAdmin)

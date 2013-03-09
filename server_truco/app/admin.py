from django.contrib import admin
from app.models import *

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)


class ConsumerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Consumer, ConsumerAdmin)


class ManagerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Manager, ManagerAdmin)


class StoreAdmin(admin.ModelAdmin):
    pass
admin.site.register(Store, StoreAdmin)


class BrandAdmin(admin.ModelAdmin):
    pass
admin.site.register(Brand, BrandAdmin)


class TagAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tag, TagAdmin)


class VirtualProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Virtual_product, VirtualProductAdmin)


class CountryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Country, CountryAdmin)


class ProvinceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Province, ProvinceAdmin)


class CityAdmin(admin.ModelAdmin):
    pass
admin.site.register(City, CityAdmin)


class ListAdmin(admin.ModelAdmin):
    pass
admin.site.register(List, ListAdmin)


class ListItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(List_item, ListItemAdmin)


class LocalizationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Localization, LocalizationAdmin)


class OfferAdmin(admin.ModelAdmin):
    pass
admin.site.register(Offer, OfferAdmin)


class PlaceHasProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Place_has_product, PlaceHasProductAdmin)

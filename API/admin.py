from django.contrib import admin
from .models import Location,Property,Images



@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ['property_id','title','location','price','featured','deal_type','date_added']




@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    search_fields = ('location',)
    list_display = ['location',]


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    search_fields = ('property__property_id','property__title',)
    list_display = ['property',]


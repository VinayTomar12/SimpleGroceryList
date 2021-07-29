from django.contrib import admin
from django.db import models
from .models import (
    ListCategory, ItemCategory, BuyingList, BuyingListItem, ItemQuantity, Item
)

class ItemCategoryAdmin(admin.ModelAdmin):
    list_display     = ('name', 'description', 'created_at')
    search_fields    = ('name',)

admin.site.register(ItemCategory, ItemCategoryAdmin)


class ItemQuantityAdmin(admin.ModelAdmin):
    list_display     = ('name', 'description',)

admin.site.register(ItemQuantity, ItemQuantityAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display     = ('user', 'name', 'category',)
    list_filter      = ('category',)
    search_fields    = ('user','name',)
    
admin.site.register(Item, ItemAdmin)


class ListCategoryAdmin(admin.ModelAdmin):
    list_display     = ('name', 'description', 'created_at')
    search_fields    = ('name',)

admin.site.register(ListCategory, ListCategoryAdmin)


class BuyingListAdmin(admin.ModelAdmin):
    list_display     = ('name', 'list_user', 'category', 'created_at', 'is_completed', 'is_deleted')
    search_fields    = ('name','list_user')
    list_filter      = ('category', 'is_completed', 'is_deleted')

admin.site.register(BuyingList, BuyingListAdmin)


class BuyingListItemAdmin(admin.ModelAdmin):
    list_display     = ('display_list_name', 'display_list_item', 'is_purchased', 'created_at', 'updated_at')

admin.site.register(BuyingListItem, BuyingListItemAdmin)
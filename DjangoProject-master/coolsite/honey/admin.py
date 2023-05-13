from django.contrib import admin

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','content','time_create','photo','is_published')
    list_display_links = ('id','name')
    search_fields = ('name','content')
    list_editable = ('is_published',)
    list_filter = ('is_published','time_create')
    prepopulated_fields = {"slug":("name",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name',)
    prepopulated_fields = {"slug":("name",)}


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name',)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','email')
    list_display_links = ('id','email')
    search_fields = ('email',)




admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Bailanys,ContactAdmin)
admin.site.register(New,NewsAdmin)





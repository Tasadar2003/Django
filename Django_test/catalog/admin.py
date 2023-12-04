from django.contrib import admin
from .models import Category, Goods, Tags
import admin_thumbnails

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'activate', 'created', 'updated']
    list_filter = ['id', 'name', 'activate', 'created', 'updated']
    search_fields = ['name', 'description']
@admin_thumbnails.thumbnail('image')
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'activate', 'category']
    list_filter = ['id', 'name', 'activate', 'category']
    search_fields = ['name', 'description']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Tags)

admin.site.site_header = "Orion Administrator"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Admin Portal 'Orion'"

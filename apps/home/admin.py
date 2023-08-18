from django.contrib import admin
from .models import Title, Category, Tags, Products, Products1, Goods


class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')
    search_fields = ('title',)
    list_filter = ('category',)
    date_hierarchy = 'created_at'


class Products1Admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')
    search_fields = ('title',)
    list_filter = ('category',)
    date_hierarchy = 'created_at'


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')
    search_fields = ('title',)
    list_filter = ('category',)
    date_hierarchy = 'created_at'


admin.site.register(Products, ProductsAdmin)
admin.site.register(Products1, Products1Admin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Category)
admin.site.register(Tags)

admin.site.register(Title, TitleAdmin)

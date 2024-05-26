from django.contrib import admin

from .models import Categories, Products


# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = []


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'slug', 'description', 'image', 'price', 'discount', 'quantity', 'category']
    list_editable= ['price', 'discount', 'quantity']
    save_on_top = True

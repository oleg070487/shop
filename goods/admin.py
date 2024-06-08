from django.contrib import admin

from .models import Categories, ProductImage, Products


# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name",]


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = [
        "name",
        "slug",
        "description",
        "image",
        "price",
        "discount",
        "quantity",
        "category",
    ]
    fields = [
        "name",
        "category",
        "slug",
        "description",
        "image",
        ("price", "discount"),
        "quantity",
    ]
    list_editable = ["price", "discount", "quantity"]
    list_filter = ["discount", "quantity", "category"]
    search_fields = ["name", "description"]
    save_on_top = True
    inlines = [ProductImageInline]

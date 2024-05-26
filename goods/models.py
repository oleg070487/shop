from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Категория")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="Slug"
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"


class Products(models.Model):
    name = models.CharField(max_length=150, verbose_name="Товар")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="Slug"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="Фото"
    )
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена"
    )
    discount = models.DecimalField(
        default=0.00, max_digits=4, decimal_places=2, verbose_name="Скидка в %"
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="Категория"
    )

    def __str__(self) -> str:
        return f"{self.name} Количество - {self.quantity}"

    class Meta:
        db_table = "product"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        # ordering = ['price']

    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price


class ProductImage(models.Model):
    product = models.ForeignKey(
        Products, related_name="images", blank=True, null=True, on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="Фото"
    )

    class Meta:
        verbose_name = "Фото товара"
        verbose_name_plural = "Фото товара"

    def __str__(self):
        return f"Image for {self.product.name}"

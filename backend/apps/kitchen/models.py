from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField("Название", max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    order_number = models.PositiveSmallIntegerField(blank=True, null=True)
    icon = models.ImageField(upload_to="category/imgs/")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural="Категории"
        ordering = ["-order_number"]

    def __str__(self):
        return self.name


# Модель для продукта
class Product(models.Model):
    name = models.CharField("Название", max_length=200)
    description = models.CharField("Описание")
    image = models.ImageField("Фото", upload_to="/products/imgs/")
    price = models.DecimalField("Цена",max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
        ordering = ["category","is_available"]
    
    def __str__(self) -> str:
            return self.name

        


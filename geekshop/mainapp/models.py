from django.db import models


class ProductCategory(models.Model):
    name = models.CharField('Имя категории', max_length=64)
    description = models.TextField('Описание', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=200, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория продукта'
        verbose_name_plural = 'категории продуктов'
        ordering = ['name']


class Product(models.Model):
    # создаем внешний ключ. указываесм родительскую таблицу и метод удаления/обновления /изменения
    # связь один-ко -многим
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=64)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=200, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    def __str__(self):
        return f"{self.name} ( {self.category.name} )"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']

from django.db import models

class Shop(models.Model):
    # user=models.ForeignKey("User.User", blank=False, null=False, on_delete=models.CASCADE, verbose_name="Пользователь")
    user=models.OneToOneField("User.User", blank=False, null=False, on_delete=models.CASCADE, verbose_name="Пользователь")
    name=models.CharField(max_length=50, blank=False, null=False, unique=True, verbose_name="Название магазина")
    description=models.CharField(max_length=250, blank=True, null=False, default="", verbose_name="Описание")
    url=models.URLField(blank=False, null=False, verbose_name="Ссылка")
    logo=models.ImageField(upload_to="logo/", null=True, blank=True, verbose_name="Логотип")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

class Goods(models.Model):
    shop=models.ForeignKey(Shop, blank=False, null=False, on_delete=models.CASCADE, verbose_name="Магазин")
    stream=models.ForeignKey("Stream.Stream", blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Стрим")
    name=models.CharField(max_length=50, blank=False, null=False, verbose_name="Название товара")
    description=models.CharField(max_length=250, blank=True, null=False, default="", verbose_name="Описание")
    cost=models.PositiveIntegerField(blank=False, null=False, verbose_name="Стоимость")
    url=models.URLField(blank=False, null=False, verbose_name="Ссылка")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'



from django.db import models

class Stream(models.Model):
    token=models.CharField(max_length=100, blank=False, null=True, unique=True, verbose_name="Токен")
    shop=models.ForeignKey("Shop.Shop", blank=False, null=False, on_delete=models.CASCADE, verbose_name="Магазин")
    def __str__(self):
        return shop.name

    class Meta:
        verbose_name = 'Стрим'
        verbose_name_plural = 'Стримы'

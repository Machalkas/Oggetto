from django.db import models

class Stream(models.Model):
    url=models.URLField(blank=False, null=True, default=None, verbose_name="Ссылка")
    title=models.CharField(max_length=50, blank=False, null=False, default="",  unique=True, verbose_name="Название")
    shop=models.ForeignKey("Shop.Shop", blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name="Магазин")
    is_active=models.BooleanField(blank=False, unique=False, default=True, verbose_name="Стрим активен")
    def __str__(self):
        return self.shop.name

    class Meta:
        verbose_name = 'Стрим'
        verbose_name_plural = 'Стримы'

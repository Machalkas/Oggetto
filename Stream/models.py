from django.db import models

class Stream(models.Model):
    url=models.CharField(max_length=250, blank=False, null=True, default=None, verbose_name="Ссылка")
    stream_key=models.CharField(max_length=25, blank=False, null=False, default="", verbose_name="StreamKey")
    title=models.CharField(max_length=50, blank=False, null=False, default="",  unique=True, verbose_name="Название")
    shop=models.ForeignKey("Shop.Shop", blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name="Магазин")
    is_active=models.BooleanField(blank=True, unique=False, default=True, verbose_name="Стрим активен")
    date=models.DateTimeField(blank=False, null=True, auto_now_add=True, verbose_name="Создано")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стрим'
        verbose_name_plural = 'Стримы'

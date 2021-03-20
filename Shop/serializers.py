from rest_framework import serializers

from .models import Shop, Goods

class ShopSerializers(serializers.ModelSerializer):
    class Meta:
        model=Shop
        exclude=("user",)

class GoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Goods
        exclude=("shop",)

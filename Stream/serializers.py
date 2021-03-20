from rest_framework import serializers

from .models import Stream
# from Shop.models import Goods

class StreamSerializers(serializers.ModelSerializer):
    class Meta:
        model=Stream
        fields="__all__"
        # exclude = ("shop",)


# class AddGoodsSerializers(serializers.ModelSerializer):
#     stream=AddStreamSerializers(many=True)
#     class Meta:
#         model=Goods
#         fields="__all__"

# class AddStreamSerializers(serializers.ModelSerializer):
#     class Meta:
#         model=Stream
#         fields="__all__"

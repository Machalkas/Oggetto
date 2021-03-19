from django import forms
from .models import Shop, Goods

class ShopForm(forms.ModelForm):
    class Meta:
        model=Shop
        fields="__all__"

class GoodsForm(forms.ModelForm):
    class Meta:
        model=Goods
        fields="__all__"
from django import forms
from .models import Shop, Goods
from User.models import User

class ShopForm(forms.ModelForm):
    # user=forms.ModelMultipleChoiceField(widget = forms.HiddenInput(), queryset=User.objects.all(), required=False)
    class Meta:
        model=Shop
        fields="__all__"
        exclude = ["user"]
        

class GoodsForm(forms.ModelForm):
    class Meta:
        model=Goods
        fields="__all__"
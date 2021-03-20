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
    # def __init__(self, qs=None, *args, **kwargs):
    #     super(ProjectSettings, self).__init__(*args, **kwargs)
    #     if qs:
    #         self.fields user=forms.ModelMultipleChoiceField( queryset=User.objects.all(), required=False)
    class Meta:
        model=Goods
        fields="__all__"
        exclude = ["shop"]
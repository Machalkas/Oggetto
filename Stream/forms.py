from django import forms
from .models import Stream

class StreamForm(forms.ModelForm):
    url=forms.URLField(widget = forms.HiddenInput(), required=True)
    class Meta:
        model=Stream
        fields="__all__"
        exclude = ["shop"]


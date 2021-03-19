from django import forms
from .models import Stream

class StreamForm(forms.ModelForm):
    class Meta:
        model=Stream
        fields="__all__"


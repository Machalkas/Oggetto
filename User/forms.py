from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    # email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class':'form-control mt-1', 'placeholder':'Email'}))
    # first_name = forms.CharField(label="Имя", max_length=30, widget=forms.TextInput(attrs={'class':'form-control mt-1', 'placeholder':'Имя'}))
    # last_name = forms.CharField(label="Фамилия", max_length=30, widget=forms.TextInput(attrs={'class':'form-control mt-1', 'placeholder':'Фамилия'}))
    # specialization = forms.CharField(max_length=250, required=False, widget=forms.TextInput(attrs={'class':'form-control mt-1',  'placeholder':'Специализация'}))

    class Meta:
        model=User
        fields = ''('email',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'class':'form-control mt-1',  'placeholder':'Пароль'})
        self.fields['password2'].widget = PasswordInput(attrs={'class':'form-control mt-1',  'placeholder':'Повторите пароль'})
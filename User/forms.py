from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class':'form-control mt-1', 'placeholder':'Email'}))
    is_shop=forms.BooleanField(widget=forms.CheckboxInput(attrs={'placeholder':'Ето магазин'}))

    class Meta:
        model=User
        fields = ('email','is_shop')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder':'Пароль'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder':'Повторите пароль'})

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class':'', 'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'',  'placeholder':'Пароль'}))
    class Meta:
        model=User
        fields = ('email',)


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email', )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)
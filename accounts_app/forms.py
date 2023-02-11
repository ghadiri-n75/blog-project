
from django import forms
from django .forms import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginUserForm(forms.Form):
    username = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_password(self):
        user = authenticate(username=self.cleaned_data.get(
            'username'), password=self.cleaned_data.get('password'))
        if user is not None:
            return self.cleaned_data.get('username')
        else:
            raise ValidationError(
                'your data is incorrect !!', code='invalid-info')


class RegisterUserForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'email'}))
    password_1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'password'}))
    password_2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'please  repeat your password'}))
    
    
    def clean_username(self):
        username =User.objects.filter(username=self.cleaned_data.get(
            'username'))
        if username :
            raise ValidationError('this username has already exist !!!',code='existed-user')
        return username

    def clean_password_1(self):
        password_1=self.cleaned_data.get('password_1')
        password_2=self.cleaned_data.get('password_2')
        if password_1 != password_2:
            raise ValidationError('your passwords are not match',code='match-passwords')
        
        
class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']
        
    
from .models import  sport_Game,Volunteer_Programs,News,comments,sport
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import CommonPasswordValidator
from django.conf import settings


class ActorSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label='Search teams or type',
                    widget=forms.TextInput(attrs={'placeholder': 'search here!'})
                  )

            
class Sport(forms.ModelForm):
    class Meta:
        model= sport_Game
        fields = "__all__"  

class  Volunteer(forms.ModelForm):
    class Meta:
        model= Volunteer_Programs
        fields = "__all__"        

class  Newsform(forms.ModelForm):
    class Meta:
        model= News
        fields = "__all__"   
class  commentsform(forms.ModelForm):
    class Meta:
        model= comments
        fields = "__all__"          
             
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=150, required=True)
   
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2',)


class SignIn(forms.Form):
    password = forms.CharField(label=('Password'), strip=False, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if settings.USE_REMEMBER_ME:
            self.fields['remember_me'] = forms.BooleanField(label=('Remember me'), required=False)

    def clean_password(self):
        password = self.cleaned_data['password']

        if not self.user_cache:
            return password

        if not self.user_cache.check_password(password):
            raise ValidationError(('You entered an invalid password.'))

        return password        

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)        
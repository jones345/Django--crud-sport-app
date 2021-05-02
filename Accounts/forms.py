from .models import sport,News,Volunteer,sportGame
from django import forms


class GamesForm(forms.ModelForm):
    class Meta:
        model = sport
        fields = "__all__"                      

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = "__all__"  
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"    
class sportGameForm(forms.ModelForm):
    class Meta:
        model = sportGame
        fields = "__all__"  
from django.forms.fields import DateTimeField
from datetimepicker.widgets import DateTimePicker
from.widgets import  BootstrapDateTimePickerInput

class sClass(forms.Form): 
  types = forms.CharField(max_length=200, help_text='sport type ')
  Date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=BootstrapDateTimePickerInput())
  Venue = forms.CharField(max_length=200,help_text='vanue of the sport classes ')
  sportImage = forms.ImageField()
  sportvideo = forms.FileField()
  instructure = forms.CharField(max_length=30,help_text='Instruture')   

class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )

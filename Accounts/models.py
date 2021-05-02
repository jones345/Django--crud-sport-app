from django.db import models

# Create your models here.
class sport(models.Model):
   types = models.CharField(max_length=200, help_text='sport type ')
   Date = models.DateTimeField(null=True,blank=True)
   Venue = models.CharField(max_length=200,help_text='vanue of the sport classes ')
   sportImage = models.ImageField(upload_to='sportimages',null = False)
   sportvideo = models.FileField(upload_to='sportvid',null= True)
   instructure = models.CharField(max_length=30,help_text='Instruture')

class sportGame(models.Model):
    Teams = models.CharField(max_length=200,help_text='teams playing against each other')
    Type = models.CharField(max_length=200, help_text='sport type ')
    Date = models.DateTimeField(null=True,blank=True)
    Venue = models.CharField(max_length=200,help_text='vanue of the sport classes ')
    Description = models.CharField(max_length=50,help_text='About the sport game')
class Volunteer(models.Model): 
    Title = models.CharField(max_length=200,help_text='title of the programs')
    Description = models.CharField(max_length=400,help_text='description of the program')
    
class News(models.Model):       
       Title= models.CharField(max_length=200,help_text='title of the news')
       Nimage = models.ImageField(upload_to='newsIamge')
       Nbody = models.CharField(max_length=500,help_text='news body')
       NdateTime = models.DateTimeField(null=True,blank=True)  
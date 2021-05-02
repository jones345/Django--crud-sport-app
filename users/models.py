from django.db import models

# Create your models here.
class sport_Game(models.Model):
    Teams = models.CharField(max_length=200,help_text='teams playing against each other')
    Type = models.CharField(max_length=200, help_text='sport type ')
    Date = models.DateTimeField(null=True,blank=True)
    Venue = models.CharField(max_length=200,help_text='vanue of the sport classes ')
    Description = models.CharField(max_length=50,help_text='About the sport game')



class Volunteer_Programs(models.Model): 
    Title = models.CharField(max_length=200,help_text='title of the programs')
    Description = models.CharField(max_length=400,help_text='description of the program')    

class News(models.Model):       
       Title= models.CharField(max_length=200,help_text='title of the news')
       Nimage = models.ImageField(upload_to='newsIamge')
       Nbody = models.CharField(max_length=500,help_text='news body')
       NdateTime = models.DateTimeField(null=True,blank=True)  




class sport(models.Model):
   types = models.CharField(max_length=200, help_text='sport type ')
   Date = models.DateTimeField(null=True,blank=True)
   Venue = models.CharField(max_length=200,help_text='vanue of the sport classes ')
   sportImage = models.ImageField(upload_to='sportimages',null = False)
   sportvideo = models.FileField(upload_to='sportvid',null= True)
   instructure = models.CharField(max_length=30,help_text='Instruture')

class sportSummar(models.Model):   
    headlings = models.CharField(max_length=200, help_text='sport summar headlings ')
    body =  models.CharField(max_length=200, help_text='sport summary body ')
    HImage = models.ImageField(upload_to='sportimages',null = False)
    Date = models.DateTimeField(null=True,blank=True)

class comments(models.Model):
     names = models.CharField(max_length=200, )
     emails =  models.EmailField(max_length=200, )
     usercomments = models.CharField( max_length=200,)
      
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import GamesForm,VolunteerForm,NewsForm,sportGameForm,sClass
from .models import sport,sportGame,Volunteer,News
# Create your views here.
def index(request):
   
    return render(request,'index.html')

def login_views(request):
    form = AuthenticationForm()
    return render (request,'login.html' ,{'form':form})
def login_request(request): 
   if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                
                return render(request,'dash.html')
            
   form = AuthenticationForm()
   return render (request,'login.html' ,{'form':form})  

def home(request):
    return render(request,'dash.html')

def Newsm(request):
    newslist = News.objects.all()
    return render(request,'News.html',{'NewsList': newslist})
    
def classv(request):   
    classsp= sport.objects.all()
    return render(request,'Classes.html',{'classList':classsp})
def sportgames(request):  
    games =  sportGame.objects.all()
    return render(request,'games.html',{'gamesList':games}) 
def Creat_Classn(request):
    Games = GamesForm()
    return render(request,'create_new_Sport.html',{'form':Games})
def Creat_Game(request):
    Csport =sportGameForm()
    return render(request,'create_new_Class.html',{'form':Csport})
def ADDn(request):
    News= NewsForm()
    return render(request,'create_new_News.html', {'form':News})  
#create_News
#ADDn
def create_News(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'indexG.html')
    
    return render(request,'create_new_News.html')         

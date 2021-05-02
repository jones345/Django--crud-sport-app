from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .form import Sport,Volunteer,Newsform,RegisterForm,commentsform,ActorSearchForm
from .models import  sport_Game,Volunteer_Programs,News,sport,sportSummar,comments
from django.views.generic import TemplateView

############ dashbaord home view 
class index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
         context = super(index, self).get_context_data(**kwargs)
         context['gamesList'] = sport_Game.objects.all()
         context['classList'] = sport.objects.all()
         context['form'] = Volunteer_Programs.objects.all()
         context['NewsList'] =News.objects.all()
         context['sports'] =sportSummar.objects.all()
         return context
  

    
############
def home(request):
    return render(request,'dash.html')
def Add_V(request):
    Sports=sport()
    return render(request,'create_new_Sport.html', {'form':Sports}) 
#############
def Create_Sport(request):
    if request.method == 'POST':
        form = Sport(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"games.html")
    return render(request,"create_new_sport.html")        

def sportViews (request):
    sportGames = sport_Game.objects.all()
    return render(request,'games.html',{'gamesList':sportGames})

def deleteS(request,id):
    sportDitem= get_object_or_404(sport_Game, id=id)
    if request.method=='POST':
        sportDitem.delete()
        return render(request,"dash.html")
    return render(request, 'deleteconfirm.html', {'object':sportDitem})

def editSport(request,id):
    sportEitem= get_object_or_404(sport_Game, id=id)
    form = Sport(request.POST or None, instance=sportEitem)
    if form.is_valid():
        form.save()
        return render(request,"dash.html")
    return render(request, "editSport.html", {'form':form})

#######################################################################################
#### sport games crud fuctions done at the top

#######################################################################################

def volunteView(request):
    vform = Volunteer_Programs.objects.all()
    return render(request,'Volunteer.html',{'form':vform})

def volunteViewAdd(request):
    vform = Volunteer()
    return render(request,'create_new_Volunteering.html',{'form':vform})


def volunterAdd(request):
    if request.method == 'POST':
        form=Volunteer(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'dash.html')
    return render(request,'create_new_Volunteering.htm')    

def deleteV(request,id):
    VDitem= get_object_or_404(Volunteer_Programs, id=id)
    if request.method=='POST':
        VDitem.delete()
        return render(request,"dash.html")
    return render(request, 'deleteconfirm.html', {'object':VDitem})


def editV(request,id):
    VEitem= get_object_or_404(Volunteer_Programs, id=id)
    form = Volunteer(request.POST or None, instance=VEitem)
    if form.is_valid():
        form.save()
        return render(request,"dash.html")
    return render(request, "editSport.html", {'form':form})

    
################################################################################
#########volunteering programs crud ########################
################################################################################

def newsp(request):
    if request.method == 'POST':
        form=Newsform(request.POST)
        if form.is_valid():
            form.save()  
            return render(request,'dash.html')
    Snews=Newsform()        
    return render(request,'create_new_News.html', {'form':Snews}) 
 
def Newsm(request): 
    Snews=News.objects.all()
    return render(request,'News.html', {'NewsList':Snews})   



##############################################################
# ##########      def classv(request):   
    #classsp= sport.objects.all()
    #return render(request,'Classes.html',{'classList':classsp})  
# #########     
# #########
   

def classv(request):

    classsp= sport.objects.all()
    return render(request,'Classes.html',{'classList':classsp})  


#########################################
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

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


   ################################################
   #####
   #######################################



from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .form import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


def bookings(request):
    return render(request,'home.html')

   
def register(request):
    if request.method  == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
           
            

            return render(request, 'log_in.html', {
              'form': AuthenticationForm()
              
            })
    else:
        form = CustomUserCreationForm()
    return render(request, 'results.html', {'form': form})




def login_(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                
                return render(request,'home.html')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "log_in.html",
                    context={"form":form})

@login_required
def bookClasses(request):
    Bc= sport.objects.all()
    context = {'classlist': Bc}
    return render(request,'HotelApp/showhotels.html',context)
@login_required
def booksport(request):
   sport = sport_Game.objects.all()
   context = {'gamesList': sport}
   return render(request,'HotelApp/showGames.html',context)


from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


def reg(request):
    template = 'vlounter.html'
    form = RegisterForm()

    return render(request, template, {'form': form})

def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'vlounter.html'
    
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()
               
                # Login the user
                login(request, user)
               
                # redirect to accounts page:
                return render(request, 'done.html')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})
def faq(request):
    return render(request,'FAQ.html')

class endGames(TemplateView): 
    template_name = 'sportComments.html'

    def get_context_data(self, **kwargs):
         context = super (endGames, self).get_context_data(**kwargs)
         context['form'] = commentsform() 
         context['com'] = comments.objects.all()
         return context  
    

def post_summary(request): 
    
    if request.method == 'POST':
        form=commentsform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'sportComments.html')
       
              
    return render(request,'sportComments.html') 

def teams(request):
    sport = sport_Game.objects.all()
    return render(request,'single.html',{'gamesList':sport}) 

def GamesFull(request):
    classsp = sport.objects.all()
    return render(request,'classsingle.html',{'classList':classsp})  

from search_views.search import SearchListView
from search_views.filters import BaseFilter
class ActorsFilter(BaseFilter):
    search_fields = {
        'search_text' : ['teams', 'type'],
    
    }
class ActorsSearchList(SearchListView):
    model = sport_Game
    paginate_by = 30
    template_name = "actors/actors_list.html"
    form_class = ActorSearchForm
    filter_class = ActorsFilter    

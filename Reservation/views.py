from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import CustomUserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, authenticate
def index(request):
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




def login_request(request):
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
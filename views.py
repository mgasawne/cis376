from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def profile_list(request):
    #will have to modfy to better fit requirements/access allocation for certain pages.  
    if request.user.is_authenticated: 
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {"profiles":profiles})
    else:
        messages.success(request, ("Blah blah/log in?"))
        return redirect('home')
    
#will controll which profile/s get access to what 
# !!! will have to edit to fit reqs
def profile(request, pk):
    if request.user.is_authenticated: 
        profile = Profile.objects.get(user_id = pk)
        return render(request, "profile.html", {"profile":profile})
    else:
        messages.success(request, ("Blah blah/log in?"))
        return redirect('home')
from contextlib import redirect_stderr
from multiprocessing import context
from traceback import print_tb
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Events
import datetime
from .form import EventsForm



def home(request):
    events = Events.objects.all()
    context = {'events': events}
    return render(request, 'base/home.html', context)

def events(request):
    events = None

    return render(request, 'base/dashboard.html')

# @login_required(login_url='login')
def createEvent(request):
    if request.method=="POST":
        form = Events()
        form.title = request.POST.get('title')
        form.name = request.POST.get('description')
        form.about = request.POST.get('about')
        form.event_start_date = request.POST.get('start_date')
        form.event_end_date = request.POST.get('end_date')
        form.department = request.POST.getlist('department[]')
        form.campus = request.POST.getlist('campus[]')
        form.tags = request.POST.getlist('tag[]')
        form.email = request.POST.get('email')
        if len(request.FILES) != 0:
         form.featured_img = request.FILES.get('featured_img')
        form.event_start_time = request.POST.get('start_time')
        form.event_end_time = request.POST.get('end_time')
        form.contact = request.POST.get('contact')
        form.address = request.POST.get('address')
        form.is_online_event = request.POST.get('is_online_event')
        form.website = request.POST.get('website')
        form.facebook = request.POST.get('facebook')
        form.youtube = request.POST.get('youtube')
        form.instagram = request.POST.get('instagram')
        form.twitter = request.POST.get('twitter')
        form.external_link = request.POST.get('external_link')
        form.club_name = request.POST.get('club_name')
        form.button_name = request.POST.get('button_name')
        form.custom_text = request.POST.get('custom_text')
        form.event_attendees = request.POST.get('event_attendees')
        form.publish = request.POST.get('publish')
        form.google_map = request.POST.get('google_map')
        form.save()
        return redirect('home')
    context = {}
    return render(request, 'base/create-event.html', context)

def singlEvent(request,pk):
    singEv = Events.objects.filter(id=pk)
    context={'singEv':singEv}
    return render(request, 'base/singlevent.html',context)  

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User Does not exist')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')

        
    context = {}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def updateEvent(request, pk):
    edited = Events.objects.get(id=pk)
    form = EventsForm(instance=edited)

    if request.method == 'POST':
        form = Events(request.POST, instance=edited)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, "base/create-event.html", context)

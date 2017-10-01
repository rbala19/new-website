from django.shortcuts import render
from django.http import HttpResponse

from .models import Event

def event_list(request):
    lst = Event.objects.filter(complete=False).order_by('name')
    context = {'event_list': lst}
    return render(request, 'internal/event_list.html', context)

def event_details(request, event_name):
	event = Event.objects.get(name=event_name)
	context = {'event': event}
	return render(request, 'internal/event_details.html', context)

def register(request):
    return HttpResponse("You're trying to register")

def member_list(request):
    context = {}
    return render(request, 'internal/member_list.html', context)

def member_details(request, username):
    return HttpResponse("You're looking at member %s" % username)

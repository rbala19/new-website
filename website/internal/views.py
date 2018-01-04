from django.shortcuts import render
from django.http import HttpResponse

from .models import Event
from .models import Member
from .models import Committee

def event_list(request):
    lst = Event.objects.all().order_by('name')
    context = {'event_list': lst}
    return render(request, 'internal/event_list.html', context)

def event_details(request, event_name):
	event = Event.objects.get(name=event_name)
	context = {'event': event}
	return render(request, 'internal/event_details.html', context)

def register(request):
    return HttpResponse("You're trying to register")

def member_list(request):
    lst = Member.objects.all()
    context = {'member_list': lst}
    return render(request, 'internal/member_list.html', context)

def member_details(request, username):
    member = Member.objects.get(username=username)
    context = {'member': member}
    return render(request, 'internal/member_details.html', context)

def committees(request):
    lst = Committee.objects.all()
    context = {'committees': lst}
    return render(request, 'internal/committees.html', context)

def committee_members(request, name):
    comm = Committee.objects.get(name = name)
    print(comm)
    lst = Member.objects.filter(committees__in=[comm])
    print(lst)
    context = {'members': lst}
    return render(request, 'internal/committee_members.html', context)




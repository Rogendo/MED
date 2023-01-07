from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, HttpResponse
from medexpert.models import Msgs
from medexpert.models import Emergency
from medics.forms import Tableform
from django.contrib import messages



def viewmessage(request):
    users =Msgs.objects.all()
    args ={'users':users}
    return render(request, 'medics/message.html', args)



def viewemergency(request):
    users =Emergency.objects.all()
    args ={'users':users}
    return render(request, 'medics/emergency.html', args)


def home(request):
    return render(request,'medics/index.html')

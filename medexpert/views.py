from django.shortcuts import render, get_list_or_404, redirect
from .models import Updates
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Hospitals,Map
from .models import FirstAid,Emergency,Profile
from .forms import Table,Reg
from medics.forms import Tableform
from django.contrib.auth import authenticate, get_user_model, login, logout



def submit(request):
    if request.method == 'POST':
        form = Table(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data saved in the resipitory')

    else:
        form = Table()
        args = {'form': form}
        return render(request, 'medexpert/emergency.html', args)


def home(request):
    return render(request,"medexpert/home.html")



def updateview(request):
    latest_updates=get_list_or_404(Updates)
    print(latest_updates)
    context= {'latest_updates': latest_updates }
    return render(request,'medexpert/index.html',context)





def view_hospital(request):
    nearby_hospitals=get_list_or_404(Hospitals)
    print(nearby_hospitals)
    arg= {'nearby_hospitals':  nearby_hospitals }
    return render(request, 'medexpert/hospitals.html', arg)


def view_firstaid(request):
    firstaid_operations=get_list_or_404(FirstAid)
    print(firstaid_operations)
    cnxt= {'firstaid_operations':  firstaid_operations }
    return render(request, 'medexpert/firstaid.html', cnxt)


def view_maps(request):
    # location=get_list_or_404(Map)
    # print(location)
    # cnxt= {'location':  location }
    return render(request, 'medexpert/maps.html')


def Register(request):
    if request.method == 'POST':
        form = Reg(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medexpert:login')

    else:
        form = Reg()
    args = {'form': form}
    return render(request, 'medexpert/register.html', args)


#########################################################################
# def login(request):
#     if request.method =='POST':
#         Data=Profile(username=request.POST['username'],
#                   password=request.POST['password'])
#         Data.save()
#         return render(request,'medexpert/home.html')
#     else:
#         return render(request,'medexpert/login.html')

###########################################################################

def send(request):
    if request.method == 'POST':
        form = Tableform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'medexpert/message.html')


    else:
        form = Tableform()
    args = {'form':form}
    return render(request, 'medexpert/message.html', args)






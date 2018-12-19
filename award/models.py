
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from .models import Project,Profile,Rate
# from .forms import ProjectForm,ProfileForm,RateForm
# from django.contrib.auth.models import User
# import datetime as dt
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializer import ProfileSerializer,ProjectSerializer
# from rest_framework import status
# from .permissions import IsAdminOrReadOnly

def convert_dates(dates):
    # function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','thursday','Friday','Saturday','Sunday']
    '''
    Returns the actual day of the week
    '''
    day = days[day_number]
    return day

def index_page(request):
    date = dt.date.today()
    project = Project.objects.all()
    return render(request,'home.html',locals())

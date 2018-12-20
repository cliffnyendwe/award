from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .forms import NewProjectForm, NewRatingForm, NewProfileForm
from .models import Project, Rating, Profile
# Create your views here.

@login_required(login_url='/accounts/login/')
def index_page(request):
  id = request.user.id
  profile = Profile.objects.get(user=id)

  projects = Project.objects.all().order_by('-pub_date')

  return render(request, 'index.html',{'projects':projects,'profile':profile})


@login_required(login_url='/accounts/login/')
def update_project(request):
  ida = request.user.id
  profile = Profile.objects.get(user=ida)

  current_user = request.user
  current_username = request.user.username

  if request.method == 'POST':
    form = NewProjectForm(request.POST, request.FILES)
    if form.is_valid():
      project = form.save(commit=False)
      project.poster = current_user
      project.postername = current_username
      project.save()
    return redirect('index_page')

  else:
    form = NewProjectForm()

  return render(request, 'update_project.html',{'form':form,'profile':profile})



@login_required(login_url='/accounts/login/')
def rating(request,id):
  ida = request.user.id
  profile = Profile.objects.get(user=ida)
  idd = id

  current_username = request.user.username

  if request.method == 'POST':
    form = NewRatingForm(request.POST)
    if form.is_valid():
      rating = form.save(commit=False)

      design_rating = form.cleaned_data['design']
      usability_rating = form.cleaned_data['usability']
      content_rating = form.cleaned_data['content']

      avg = ((design_rating + usability_rating + content_rating)/3)

      rating.average = avg
      rating.postername = current_username
      rating.project = Project.objects.get(pk=id)

      rating.save()
    return redirect('project',id)

  else:
    form = NewRatingForm()

  return render(request, 'rating.html',{'form':form,'profile':profile,'idd':idd})



@login_required(login_url='/accounts/login/')
def profile(request, id):
  ida = request.user.id
  profile = Profile.objects.get(user=ida)
  user = request.user
  myprofile = Profile.objects.get(pk=id)
  projects = Project.objects.filter(poster=ida).order_by('-pub_date')
  projectcount=projects.count()

  return render(request, 'profile.html',{'profile':profile,'myprofile':myprofile,'user':user,'projectcount':projectcount,'projects':projects})

@login_required(login_url='/accounts/login/')
def search(request):
  ida = request.user.id
  profile = Profile.objects.get(user=ida)

  if 'project' in request.GET and request.GET['project']:
    search_term = request.GET.get('project')
    message = f'{search_term}'
    title = 'Search Results'

    try:
      no_ws = search_term.strip()
      searched_projects = Project.objects.filter(title__icontains = no_ws)

    except ObjectDoesNotExist:
      searched_projects = []

    return render(request, 'search.html',{'message':message ,'title':title, 'searched_projects':searched_projects,'profile':profile})

  else:
    message = 'You have not searched any user'
    
    title = 'Search Error'
    return render(request,'search.html',{'message':message,'title':title,'profile':profile})

@login_required(login_url='/accounts/login/')
def project(request, id):
  ida = request.user.id
  profile = Profile.objects.get(user=ida)
  project = Project.objects.get(pk=id)
  ratings = Rating.objects.filter(project=id)

  project = Project.objects.get(pk=id)

  a = Rating.objects.filter(project=id).aggregate(('design'))
  b = Rating.objects.filter(project=id).aggregate(('usability'))
  c = Rating.objects.filter(project=id).aggregate(('content'))
  
  return render(request, 'pics/project.html',{'profile':profile,'project':project,'ratings':ratings,'a':a,'b':b,'c':c,'d':d})

@login_required(login_url='/accounts/login/')
def update_profile(request):
  ida = request.user.id
  profile = Profile.objects.get(user=ida)
  
  if request.method == 'POST':
    instance = get_object_or_404(Profile, user=ida)
    form = NewProfileForm(request.POST, request.FILES,instance=instance)
    if form.is_valid():
      form.save()

    return redirect('profile', ida)

  else:
    form = NewProfileForm()

  return render(request, 'update_profile.html',{'form':form,'profile':profile})
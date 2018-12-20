from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    url(r'^$',views.index_page,name='index_page'),
  url(r'^update/project$',views.update_project, name='update_project'),
  url(r'^search/', views.search,name = 'search'),
  url(r'^profile/(\d+)', views.profile, name='profile'),
  url(r'^project/(\d+)', views.project, name='project'),
  url(r'^rating/(\d+)',views.rating, name='rating'), 
  url(r'^update/profile$',views.update_profile, name='update_profile'),
]

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^project/(\d+)',views.project,name ='project'),
    url(r'^new_projects$', views.new_projects, name='new_projects'),
    url(r'^profile/',views.profile,name = 'profile'),
    url(r'^newprofile/$',views.newprofile,name = 'newprofile'),
    url(r'^myprojects/$',views.myprojects,name = 'myprojects'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^project_detail/(\d+)',views.search_project,name = 'project-detail'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^api/project/$', views.ProjectList.as_view()),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
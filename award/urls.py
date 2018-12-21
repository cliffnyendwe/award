from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    url('^$',views.index_page,name = 'index_page'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^upload/$', views.upload_project, name='upload_project'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^edit$', views.edit, name='edit_profile'),
    url(r'^rate/(?P<project_id>\d+)',views.rate_project, name='rate'),
    url(r'^vote/(?P<project_id>\d+)',views.vote, name='vote'),
    url(r'^api/profile/$', views.ProfileList.as_view())
]

from django.db import models
from django.core.validators import URLValidator
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'projects/')
    description = models.TextField(max_length = 500)
    link = models.TextField(validators=[URLValidator()],null=True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    
  

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def get_all(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def get_project(cls, project_id):
        project = cls.objects.get(id=site_id)
        return projects

    @classmethod
    def search_by_title(cls,search_term):
        projects_title = cls.objects.filter(title__icontains=search_term)
        return sites_title

class Profile(models.Model):
    photo = models.ImageField(upload_to = 'profile/')
    profile = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    bio = models.TextField(max_length = 100)
    contact = models.IntegerField()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class AwardsProfiles(models.Model):
    name = models.CharField(max_length=40)
    bio = models.TextField()
    projects = models.CharField(max_length=70)
    dp = models.ImageField(upload_to = 'dp/')

class AwardsProjects(models.Model):
    project_name = models.CharField(max_length=40)
    description = models.TextField()


class Rating(models.Model):

  CHOICES = [(i,i) for i in range(11)]

  design = models.IntegerField(choices=CHOICES)
  usability = models.IntegerField(choices=CHOICES)
  content = models.IntegerField(choices=CHOICES)
  average = models.IntegerField()
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  postername = models.CharField(max_length=60)
  pub_date = models.DateTimeField(auto_now_add=True)


  def save_rating(self):
    self.save()

  def delete_rating(self):
    self.delete()
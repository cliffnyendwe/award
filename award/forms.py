from django import forms

from .models import Profile, Project, Rating

class NewProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    exclude = ['poster','postername', 'pub_date']


class NewRatingForm(forms.ModelForm):
  class Meta:
    model = Rating
    exclude = ['project','postername','pub_date']


class NewProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']
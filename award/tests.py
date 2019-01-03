from django.test import TestCase
from .models import Profile, Project

# Create your tests here.

class ProfileTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.new_profile =Profile()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_method(self):
        """
        Function to test that profile is being saved
        """
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)



class ProjecTestClass(TestCase):
    """  
    Tests Project class and its functions
    """
    def setUp(self):
        self.project = Project()

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_method(self):
        """
        Function to test that a project is being saved
        """
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

  


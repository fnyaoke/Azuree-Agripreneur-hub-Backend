from django.test import TestCase
from agripreneur.models import *

# Create your tests here.
class UserTestCase(TestCase):
    def test_user(self):
        self.assertTrue

    def test_save_user(self):
        self.assertTrue
    #Set up method

    def setUp(self):
        self.new_user = User(username="Your Name", email="youremail@domain.com", password="my password")
        self.new_user.save()
        self.new_location = User(user=self.new_user, email = "myemail@domain.com", location="your location",category="your category")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))

    def test_save_method(self):
        self.new_user.save_user()
        profile = User.objects.all()
        self.assertTrue(len(User)>0)

    def test_delete_method(self):
        self.new_user.save_user()
        self.new_user.delete_user()
        profile = User.objects.all()
        self.assertTrue(len(User)==0)

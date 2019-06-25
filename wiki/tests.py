from django.test import TestCase
from .models import Page
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .views import upload_file
# Create your tests here.

# index page tests
class IndexPageTesting(TestCase):

    def index_test(self):
        response = self.client.get(reverse('wiki:index'))# gets contents of the page.
        self.assertEqual(response.status_code, 200)# Checks if  page responds with 200 status code.
        self.assertContains(response, "Your Screen resolution is currently")# Checks if the page contains the content"


    def no_pages(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, "No pages are available at this time.") 

class PageCreationTestCase(TestCase):
    def setUp(self):
        page = Page.objects.create(title="Test", content="Hello world") # Creates a page called Test and creates some content.
        page.save()
        self.user = User.objects.create_user('User1', 'TestUser@mywiki.com', 'Password1') # Creates a user with the specified details.

    def test_page_setup_case_1_content(self):
        response = self.client.get('/Test/') 
        self.assertContains(response, "Hello world") 

class LoginTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('User1', 'TestUser@mywiki.com', 'Password1') 

    def testLogin(self):
        self.client.login(username='User1', password='Password1') # logs in the test user or page will respond with the login screen.
        response = self.client.get(reverse('wiki:index'))  
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, "logout") 
        
class PageViewTests(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('wiki:index')) 
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, "Your Screen resolution is currently")
    def test_sign_in_page_view(self):
        response = self.client.get('/accounts/login/')  
        self.assertContains(response, "Log into your account here") 

    def setUp(self):
        self.user = User.objects.create_user('User1', 'TestUser@mywiki.com', 'Password1') 

    def test_upload_page_view(self):
        self.client.login(username='User1', password='Password1') 
        response = self.client.post('/upload/', follow=True)  
        self.assertContains(response, "Uploaded Files") 

    def test_edit_page_view(self):
        self.client.login(username='User1', password='Password1') 
        response = self.client.post('/PageNotFound/edit', follow=True)  
        self.assertContains(response, "Edit") 
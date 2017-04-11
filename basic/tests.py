from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from views import index, login, register
from models import Conference, UserConference, Item, Comment
from capstone.forms import LoginForm, UserForm, ConferenceForm
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import json
# Create your tests here.


class HomePageTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user('temporary', 'temporary@louisivlle.edu', 'temporary')
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()

    def tearDown(self):
        # Call tearDown to close the web browser
        self.selenium.quit()

    def test_root_direct_to_basic_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_navigation_bar(self):
        self.selenium.get('http://127.0.0.1:8000/')
        assert 'Hello' in self.selenium.page_source
        self.selenium.find_element(By.XPATH, "//a[@href='/']").click()
        assert 'Hello' in self.selenium.page_source
        self.selenium.get('http://127.0.0.1:8000/')
        self.selenium.find_element(By.XPATH, "//a[@href='/logout']").click()
        assert 'Login' in self.selenium.page_source


class LoginTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user('temporary', 'temporary@louisivlle.edu', 'temporary')
        self.user = User.objects.create_user('DROP SCHEMA public CASCADE', 'temporary1@louisivlle.edu', 'temp')
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()

    def tearDown(self):
        # Call tearDown to close the web browser
        self.selenium.quit()

    def test_login_view(self):
        request = self.factory.get('/')
        response = login(request)
        self.assertEquals(200, response.status_code)
        self.assertIn('login-submit', response.content)

    def test_login_form_correct(self):
        form_data = {'username': 'temporary', 'password': 'temporary'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_incorrect_username(self):
        form_data = {'username': 'temporary1', 'password': 'temporary'}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals([u'Please enter a correct username and password. Note that both fields may be case-sensitive.'],form.errors['__all__'])

    def test_login_form_incorrect_password(self):
        form_data = {'username': 'temporary', 'password': 'temporary1'}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals([u'Please enter a correct username and password. Note that both fields may be case-sensitive.'],form.errors['__all__'])

    def test_login_form_username_not_entered(self):
        form_data = {'username': '', 'password': 'temporary'}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals({'username': [u'This field is required.']},form.errors)

    def test_login_form_password_not_entered(self):
        form_data = {'username': 'temporary', 'password': ''}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals({'password': [u'This field is required.']},form.errors)

    def test_login_form_sanitation(self):
        form_data = {'username': 'DROP SCHEMA public CASCADE', 'password': 'temp'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())
        form_data = {'username': 'temporary', 'password': 'temporary'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())
        form_data = {'username': ' temporary ', 'password': ' temporary '}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_gui(self):
        self.selenium.get('http://127.0.0.1:8000/login')
        assert 'Login' in self.selenium.page_source
        self.selenium.find_element(By.NAME, "username").send_keys('temporary')
        self.selenium.find_element(By.NAME, "password").send_keys('temporary')
        self.selenium.find_element(By.ID, "login-submit").click()
        assert 'Hello, temporary' in self.selenium.page_source

class RegisterTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

    def test_register_view(self):
        request = self.factory.get('/')
        response = register(request)
        self.assertEquals(200, response.status_code)
        self.assertIn('<p>Create Account</p>', response.content)

    def test_register_form_correct(self):
        form_data = {'username': 'temporary', 'email': 'temporary@louisville.edu', 'password': 'temporary'}
        form = UserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_register_form_username_not_entered(self):
        form_data = {'username': '', 'email': 'temporary@louisville.edu', 'password': 'temporary'}
        form = UserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals({'username': [u'This field is required.']},form.errors)

    # def test_create_form_email_not_entered(self):
    #     form_data = {'username': 'temporary', 'email': '', 'password': 'temporary'}
    #     form = UserForm(data=form_data)
    #     self.assertFalse(form.is_valid())
    #     self.assertEquals({'email': [u'This field is required.']},form.errors)

    def test_register_form_password_not_entered(self):
        form_data = {'username': 'temporary', 'email': 'temporary@louisville.edu', 'password': ''}
        form = UserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals({'password': [u'This field is required.']},form.errors)

    def test_register_user_post(self):
        response = self.client.post('/register/', {'username': 'temporary', 'email': 'temporary@louisville.edu', 'password': 'temporary'})
        user = User.objects.get(username='temporary')
        self.assertEqual(user.username, 'temporary')
        self.assertEqual(user.email, 'temporary@louisville.edu')
        self.assertTrue(self.client.login(username='temporary', password='temporary'))


# class ProfileTests(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#         self.factory = RequestFactory()
#         self.user = User.objects.create_user('temporary', 'temporary@louisivlle.edu', 'temporary')
#
#     def test_profile_view(self):
#         request = self.factory.get('/')
#         request.user = authenticate(username='temporary', password='temporary')
#         response = profile(request)
#         self.assertEqual(200, response.status_code)
#         self.assertIn('', response.content)
#
#     def test_redirect_to_login_when_not_logged_in_profile(self):
#         response = self.client.get('/profile', follow=False)
#         self.assertEquals(301, response.status_code)
#         response = self.client.get('/profile', follow=True)
#         self.assertIn('<p>Login</p>', response.content)
#
#     def test_user_info_display(self):
#         request = self.factory.get('/')
#         request.user = authenticate(username='blakrtest', password='blakrtest')
#         response = profile(request)
#         self.assertIn('<h2>temporary</h2>', response.content)
#         self.assertIn('', response.content)

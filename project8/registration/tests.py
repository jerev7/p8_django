from django.test import TestCase
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template import loader
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .register_form import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User


# Create an account
class AccountPageTest(TestCase):
    def test_account_creation(self):
        new_form = RegisterForm()
        # new_form.username = "Bob"
        # new_form.email = "bobby@gmail.com"
        # new_form.password1 = "mypass13"
        # new_form.password2 = "mypass13"
        response = self.client.post(reverse('register'), {'form': new_form})
        self.assertEqual(response.status_code, 200)

# Login


# Logout

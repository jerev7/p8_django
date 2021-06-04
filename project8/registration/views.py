from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template import loader
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .register_form import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User


def registration_ok(request):
    return render(request, 'registration/registration_ok.html')

def logged_out(request):
    return render(request, 'registration/logged_out.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully') # appears only in /admin
            return redirect('registration_ok')
    else:
        form = RegisterForm()
    context = {
        "form": form
    }
    return render(request, 'registration/register.html', context)

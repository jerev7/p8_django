# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	message = "Salut tout le monde !"
	return HttpResponse(message)

def myapp_index(request):
	message = "Index de mon application"
	return HttpResponse(message)
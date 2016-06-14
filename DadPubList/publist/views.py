from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from publist.models import Pub

def index(request):
	return render(request, 'publist/index.html')

def results(request):
	return HttpResponse('Work in Progess')

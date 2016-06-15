from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from publist.models import Pub
from django.db.models import Q

def index(request):
	return render(request, 'publist/index.html')


def search(request):
	query = request.GET.get('q')
	results = Pub.objects.filter(Q(name__icontains=query) | Q(address__icontains=query) | Q(area__icontains=query) | Q(county__icontains=query)).order_by('name')

	return render(request, 'publist/results.html', {'results' : results})	

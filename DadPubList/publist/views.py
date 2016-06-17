from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from publist.models import Pub
from publist.forms import AddPub
from django.db.models import Q

def index(request):
	return render(request, 'publist/index.html')


def search(request):
	query = request.GET.get('q')
	results = Pub.objects.filter(Q(name__icontains=query) | Q(address__icontains=query) | Q(area__icontains=query) | Q(county__icontains=query)).order_by('name')

	return render(request, 'publist/results.html', {'results' : results})	

def add_pub(request):
	if request.method == 'POST':
		pub_form = AddPub(data=request.POST)

		if pub_form.is_valid():
			pub = Pub()
			pub.name = pub_form.cleaned_data['name']
			pub.address = pub_form.cleaned_data['address']
			pub.area = pub_form.cleaned_data['area']
			pub.county = pub_form.cleaned_data['county']
			pub.thisyear = pub_form.cleaned_data['thisyear']
			pub.fromapp = pub_form.cleaned_data['fromapp']

			pub.save()
			return HttpResponseRedirect('/publist/')

		else:
			print pub_form.errors

	else:
		pub_form = AddPub()

	return render(request, 'publist/add_pub.html', {'pub_form': pub_form})

def all_pubs(request):
	counter = Pub.objects.all().count()
	pubs = Pub.objects.all().order_by('name')

	return render(request, 'publist/all_pubs.html', {'pubs': pubs, 'counter' : counter})
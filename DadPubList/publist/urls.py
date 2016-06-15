from django.conf.urls import patterns, url
from publist import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^results/$', views.search, name='results'),
	url(r'^addpub/$', views.add_pub, name='addpub'),
	#url(r'^results/$', views.results, name='results'),
)
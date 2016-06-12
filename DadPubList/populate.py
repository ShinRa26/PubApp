import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DadPubList.settings')

import django
django.setup()

from publist.models import Pub

def populate():
	f = open('publist.txt', 'r')

	while f.readline != '':
		l = f.readline()
		
		if l[:-3].endswith('Y'):
			print l
		else:
			print "No Y"
	

def addPub(name, address, area, county, thisyear, fromapp):
	p = Pub.objects.get_or_create(name=name, address=address, area=area, county=county, thisyear=thisyear, fromapp=fromapp)

if __name__ == '__main__':
	print 'Populating Pub Database...'
	populate()
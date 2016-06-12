import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DadPubList.settings')

import django
django.setup()

from publist.models import Pub
import re

def populate():
	f = open('publist.txt', 'r')

	while f.readline() != '':
		l = f.readline()
		words = l.split(',')
		last = words[-1]
		if len(words) == 6:
			print words
		"""
		if 'Y' in last:
			split = last.split('**')
			if '**' in last:
				addPub(words[0], words[1], words[2], split[0], True, True)
			else:
				addPub(words[0], words[1], words[2], split[0], True, False)
		else:
			if len(words) == 4:
				addPub(words[0], words[1], words[2], words[3], False, False)
			elif len(words) == 3:
				addPub(words[0], words[1], words[2], "None", False, False)
		"""
	f.close()
		
		


def addPub(name, address, area, county, thisyear, fromapp):
	p = Pub.objects.get_or_create(name=name, address=address, area=area, county=county, thisyear=thisyear, fromapp=fromapp)

if __name__ == '__main__':
	print 'Populating Pub Database...'
	populate()
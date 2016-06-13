import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DadPubList.settings')

import django
django.setup()

from publist.models import Pub

def populate():
	filename = "publist.txt"

	with open(filename, 'r') as f:
		for line in f:
			words = line.split(',')
			last = words[-1]

			if len(words) == 6:
				words[1] = words[1] + ", " + words[2] + ", " + words[3]
				del words[2]
				del words[3]
			elif len(words) == 5:
				words[1] = words[1] + ", " + words[2]
				del words[2]

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

		
def addPub(name, address, area, county, thisyear, fromapp):
	p = Pub.objects.get_or_create(name=name, address=address, area=area, county=county, thisyear=thisyear, fromapp=fromapp)


if __name__ == '__main__':
	print 'Populating Pub Database...'
	populate()
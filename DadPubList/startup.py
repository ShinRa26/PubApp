import os
import webbrowser

def server():
	os.system('sudo python manage.py runserver')
	
def browser():
	url = "localhost:8000/publist/"
	c = webbrowser.get('firefox')
	c.open(url)

def main():
	browser()
	server()

main()
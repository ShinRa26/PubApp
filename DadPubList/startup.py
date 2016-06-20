import os
import webbrowser
from threading import Thread


def server():
	os.system('python manage.py runserver')
	
def browser():
	url = "localhost:8000/publist/"
	c = webbrowser.get('chrome')
	c.open(url)

def main():
	startServer = Thread(target=server)
	startBrowser = Thread(target=browser)

	startBrowser.start()
	startServer.start()


main()

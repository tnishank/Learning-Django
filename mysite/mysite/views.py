from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("Hello world")

def my_home_page(request):
    return HttpResponse("My home page")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html',{'current_date' : now})

def hours_ahead(request, offset):
	try:
		offset = int (offset)
	except ValueError:
		raise http404()

	dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
	html = "<html><body> In %s hour(s), it will be %s</body><html>" %(offset, dt)

	return HttpResponse(html)
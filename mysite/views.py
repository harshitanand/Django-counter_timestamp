from django.http import HttpResponse
import datetime

def hello(request):
	return HttpResponse("hello World")

def time(request):
	now = datetime.datetime.now()
	html = "<html><body>The current TIME and DATE is %s</body></html>" % (now)
	return HttpResponse(html)

def times_ahead(request, offset):
	try:
		offset = int (offset)
	except VALUEERROR:
		raise Http404()
	prev = datetime.datetime.now()
	now = prev + datetime.timedelta(hours=offset)
	html = "<html><body>The current DATETIME is %s and after %s hours DATETIME will be %s</body></html>" % (prev, offset, now)
        return HttpResponse(html)
	

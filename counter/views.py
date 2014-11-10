from django.shortcuts import render
from django.http import HttpResponse
from counter.models import counter
import datetime

# Create your views here.

def main_page(request):

	p = counter.objects.all()[0]
	p.hit_count = p.hit_count + 1
	p.time_count = datetime.datetime.now()
	p.save()

	content = '''
		<html>
			<head>
			<title> Connecting my_site </title>
			</head>

			<body>
			<h2> Conneted to my site </h2>
			We will use this for hit countsit
			<ul>
				<li><h3>The total number of hitcounts is %s </h3></li>
				<li><h3>Recent time stamp is %s</h3></li>
			</ul>
			</body>
		</html>''' % (p.hit_count, p.time_count)

	return HttpResponse(content)


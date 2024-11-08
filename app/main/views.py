from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def halodunia(request):
	html = '<h1>Halo Dunia!</h1>'
	return HttpResponse(html)
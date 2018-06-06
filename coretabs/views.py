from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi there, this is our new home page.")

def hello(request, name):
	return HttpResponse("<!DOCTYPE html><html lang=\"eng-US\"><head><title>Hello web App</title></head><body bgcolor =\"#ABFF9A\"><header><h2>Hello {} !!</h2></header></body></html>".format(name))
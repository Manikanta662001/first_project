from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hai(request):
    return HttpResponse('<center><h1>This is a Hai function</h1></center>')
def hello(request):
    return HttpResponse('<marquee><h1>This is a hello function</h1></marquee>')
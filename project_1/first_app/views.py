from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return HttpResponse("Home page")
def courses(request):
    return HttpResponse("Course page.")

def about(request):
    return HttpResponse("About page.")





from django.http import HttpResponse
from django.shortcuts import render

def shop(request):
    return HttpResponse("Minion shop ")

def category(request):
    return HttpResponse("Category:")
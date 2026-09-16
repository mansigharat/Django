#all the logical part are written in this file
#there are two types of view , class based and function based
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    print("Test 1 pass")
    return HttpResponse("<h1>Hey I'm Django Server.</h1>")


def success(request):
    print("Test 2 pass")
    return HttpResponse("<h1> This page created by Manasi </h1>")
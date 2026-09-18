#all the logical part are written in this file
#there are two types of view , class based and function based
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    peoples = [
            {'name' : "Sayali",'age':25},  
            {'name' : "Dhanshree",'age':22},  
            {'name' : "Manasi",'age':20},  
            {'name' : "Parth",'age':12},  
        ]
    for people in peoples:
        print(people)

    text="""    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Consequuntur ad harum ea tempore libero minus suscipit placeat optio, pariatur quo, debitis eum accusamus! Saepe asperiores eos neque natus nulla necessitatibus?
    Eligendi iure dolorum, velit tenetur, debitis ullam labore non iste numquam quod molestiae assumenda aperiam mollitia quaerat quam ipsum doloremque atque dicta odio cupiditate. Aperiam hic iure nihil asperiores facilis."""

    print("Test 1 pass")
    return render(request, 'home/index.html', context = {'peoples' : peoples, "text":text})
        

def success(request):
    print("Test 2 pass")
    return HttpResponse("<h1> This page created by Manasi </h1>")

def about(request):
    context = {'page' : 'About'}
    print("Test 3 pass")
    return render(request,'home/about.html',context)

def contact(request):
    context = {'page':'Contact'}
    print("Test 4 pass")
    return render(request,'home/contact.html',context)

from django.shortcuts import render
from .models import *
from django.shortcuts import redirect

# Create your views here.
def receipe(request):
    if request.method == "POST":
        data = request.POST

        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        Recipe.objects.create(
            receipe_image = receipe_image,
            receipe_name = receipe_name,
            receipe_description = receipe_description,
        )

        return redirect('/receipes/')

    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))

    context = {'receipes' : queryset}
    return render(request, 'receipe.html',context)

def update_receipe(request,id):
    queryset = Recipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')  

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/receipe/')
        

    context = {'receipes' : queryset}
    return render(request, 'update_receipe.html',context)


def delete_receipe(request,id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipe/')
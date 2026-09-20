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

        return redirect('/receipe/')

    queryset = Recipe.objects.all()
    context = {'receipes' : queryset}
    return render(request, 'receipe.html',context)

def delete_receipe(request,id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipe/')
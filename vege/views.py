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
        # print(receipe_name)
        # print(receipe_description)
        # print(receipe_image)
        # print("Test Pass ✅️")

    return render(request, 'receipe.html')
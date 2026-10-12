from django.shortcuts import render
from report.models import Student
from django.core.paginator import Paginator

objects = ["john", "paul", "george", "ringo"]
p = Paginator(objects, 2)  # 2 items per page
page1 = p.page(1)
page2 = p.page(2)
print(page1.object_list)  # ['john', 'paul']
print(page2.object_list)  # ['george', 'ringo']

def get_students(request):
    queryset = Student.objects.all()
    return render(request, 'students.html', {'queryset': queryset})
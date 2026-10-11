from django.shortcuts import render
from report.models import Student

def get_students(request):
    queryset = Student.objects.all()
    return render(request, 'students.html', {'queryset': queryset})
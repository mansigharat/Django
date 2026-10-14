from django.shortcuts import render
from report.models import *
from django.core.paginator import Paginator
from django.db.models import Q


def get_students(request):
    queryset = Student.objects.all()

    paginator = Paginator(queryset, 10)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'students.html', {'page_obj': page_obj})


def get_students(request):
    queryset = Student.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search)
        )

    paginator = Paginator(queryset, 10)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)


    return render(request, 'students.html', {'page_obj': page_obj})

def see_marks(request, student_id):
    queryset = SubjectMarks.objects.all(student__student_id__student_id = student_id)
    return render(request, 'see_marks.html', {'queryset':queryset})


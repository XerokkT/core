from django.shortcuts import render
from .models import Course

# Create your views here.
def course_list(request):
    courses = Course.objects.all()

    return render(request, "A/course_list.html", {"courses":courses})

def course_list(request):
    query = request.GET.get('q', '')
    
    if query:
        courses = Course.objects.filter(code__icontains=query)
    else:
        courses = Course.objects.all()

    return render(request, "A/course_list.html", {"courses": courses, "query": query})
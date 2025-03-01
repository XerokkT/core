from django.shortcuts import render, get_object_or_404, redirect
from .models import Course

# Create your views here.
def course_list(request):
    courses = Course.objects.all()

    return render(request, "A/course_list.html", {"courses":courses})

def course_search(request):
    query = request.GET.get('q', '')
    
    if query:
        courses = Course.objects.filter(code__icontains=query)
    else:
        courses = Course.objects.all()

    return render(request, "A/course_search.html", {"courses": courses, "query": query})

def course_search_name(request):
    query = request.GET.get('q', '')
    
    if query:
        courses = Course.objects.filter(name__icontains=query)
    else:
        courses = Course.objects.all()
        
    return render(request, "A/course_search_name.html", {"courses": courses, "query": query})

def course_edit(request, code):
    course = get_object_or_404(Course, code=code)
    
    if request.method == 'POST':
        new_code = request.POST.get('code')
        new_name = request.POST.get('name')
        
        course.code = new_code
        course.name = new_name
        course.save()
        
        return redirect('course_edit', code=course.code)
    
    return render(request, 'A/course_edit.html', {'course': course})

def course_delete(request):
    message = ""
    if request.method == "POST":
        code = request.POST.get('code')
        try:
            course = Course.objects.get(code=code)
            course.delete()
            message = f"ลบรายวิชา {code} เรียบร้อยแล้ว"
        except Course.DoesNotExist:
            message = f"ไม่พบรายวิชาที่มีรหัส {code}"
    
    return render(request, "A/course_delete.html", {"message": message})

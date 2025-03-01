from django.urls import path
from .views import course_list

urlpatterns = [
    path('courses/', course_list, name='course_list'),

    path('courses_search/', course_list, name='courses_search'),
]

from django.urls import path
from .views import course_list, course_search

urlpatterns = [
    path('courses/', course_list, name='course_list'),

    path('courses_search/', course_search, name='courses_search'),
]

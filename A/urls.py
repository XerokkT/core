from django.urls import path
from .views import course_list, course_search, course_search_name, course_edit, course_delete

urlpatterns = [
    path('courses/', course_list, name='course_list'),

    path('courses_search/', course_search, name='courses_search'),

    path('courses_search_name/', course_search_name, name='course_search_name'),

    path('courses/edit/<str:code>/', course_edit, name='course_edit'),

    path('courses/delete/', course_delete, name='course_delete'),
]

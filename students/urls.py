from django.urls import path
from .views import all_students, single_student_view

urlpatterns = [
    path('', all_students ,name='all'),  
    path('<int:id>/', single_student_view, name='single-student') 
]
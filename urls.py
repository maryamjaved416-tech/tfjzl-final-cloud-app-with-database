from django.urls import path
from . import views

app_name = 'coursequiz'

urlpatterns = [
    # baaki paths...
    
    # 1. submit path
    path('<int:course_id>/submit/', views.submit, name='submit'),
    
    # 2. show_exam_result path  
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result'),
]

from django.urls import path
from . import views

app_name = 'coursequiz'

urlpatterns = [
    # tumhare baaki paths yahan...
    
    path('submit/<int:course_id>/', views.submit, name='submit'),
    path('result/<int:course_id>/<int:submission_id>/', views.show_exam_result, name='show_exam_result'),
]

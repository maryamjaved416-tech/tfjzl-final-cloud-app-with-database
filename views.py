from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Course, Question, Choice, Submission, Enrollment

def submit(request, course_id):
    # 1. Course aur Enrollment retrieve karna
    course = get_object_or_404(Course, pk=course_id)
    enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
    
    # 2. Submission object banana
    submission = Submission.objects.create(enrollment=enrollment)

    # 3. Selected choices ko associate karna
    for key, value in request.POST.items():
        if key.startswith('choice'):
            choice_id = int(value)
            choice = Choice.objects.get(pk=choice_id)
            submission.choices.add(choice)
    
    submission.save()
    
    # 4. Result page pe redirect karna
    return HttpResponseRedirect(reverse('coursequiz:show_exam_result', args=(course_id, submission.id)))

def show_exam_result(request, course_id, submission_id):
    # 1. Course aur Submission retrieve karna
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    # 2. Score calculate karna using is_get_score() method
    total_score = submission.is_get_score()
    
    # 3. Possible score calculate karna
    possible_score = 0
    for question in course.question_set.all():
        possible_score += question.grade
    
    # 4. Context template ko bhejna
    context = {
        'course': course,
        'submission': submission,
        'total_score': total_score,
        'possible_score': possible_score,
    }
    
    return render(request, 'coursequiz/exam_result_bootstrap.html', context)

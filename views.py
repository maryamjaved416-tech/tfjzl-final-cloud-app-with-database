from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from.models import Course, Question, Choice, Submission, Enrollment
from django.utils.timezone import now

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # 1. Course aur Enrollment lena
    # 2. Submission object banana
    # 3. Selected choices ko associate karna
    # Filhal basic logic
    submission = Submission.objects.create(course=course, enrollment_id=1) # enrollment_id change karna

    selected_ids = []
    for key in request.POST:
        if key.startswith('choice'):
            selected_ids.append(int(request.POST[key]))

    submission.choices.set(selected_ids)
    submission.save()

    return HttpResponse(f"Submitted for course {course_id}")

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)

    # Score calculate karna
    total_score = submission.is_get_score()
    possible_score = sum([q.grade for q in course.question_set.all()])

    context = {
        'course': course,
        'submission': submission,
        'total_score': total_score,
        'possible_score': possible_score,
    }
    return render(request, 'coursequiz/exam_result_bootstrap.html', context)

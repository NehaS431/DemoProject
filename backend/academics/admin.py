from django.contrib import admin
from .models import Course, Test , Question ,StudentCourse ,TestAppeared ,SelectedAnswers
# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=['id','course_name','creator_name']

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display=['id','test_name','test_duration','course_associated']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=['id','question_name','answer','option_a','option_b','option_c','option_d']

@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    list_display=['id','student_id','course_id']


@admin.register(TestAppeared)
class TestAppearedAdmin(admin.ModelAdmin):
    list_display=['id','student','test','start_time','end_time','score']


@admin.register(SelectedAnswers)
class SelectedAnswersAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'test', 'question', 'selected_answer']
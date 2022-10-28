from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework.response import Response

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    creator_name=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name


class Test(models.Model):
    test_name=models.CharField(max_length=256,default='',unique=True)
    test_duration=models.DurationField(blank=False,default=timezone.now)
    course_associated=models.ForeignKey(Course, on_delete=models.CASCADE,default='')

    def __str__(self):
        return self.test_name

class Question(models.Model):
    question_name=models.CharField(max_length=256,default='')
    answer=models.CharField(max_length=256,default='')
    option_a=models.CharField(max_length=256,default='')
    option_b=models.CharField(max_length=256,default='')
    option_c=models.CharField(max_length=256,default='')
    option_d=models.CharField(max_length=256,default='')
    test_associated=models.ForeignKey(Test,on_delete=models.CASCADE,default='')

    def __str__(self):
        return self.question_name

class StudentCourse(models.Model):
    student_id=models.ForeignKey(User, on_delete=models.CASCADE)
    course_id=models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student_id)
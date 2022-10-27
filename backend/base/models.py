from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=200)
    creater_name=models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = "Course"

    def __str__(self):
        return "Course - {0}".format(self.id)
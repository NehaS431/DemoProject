from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken 

from .models import Course , Test , Question , StudentCourse, TestAppeared ,SelectedAnswers

class CourseSerializers(serializers.Serializer):

    course_name=serializers.CharField(required=True,max_length=256)
    creator_name=serializers.CharField(required=True,max_length=256)
    #creator name will be the username of the creator 
    class Meta:
        model=Course
        fields=('course_name','creator_name')
    
    def create(self,validated_data):
        course_detail=Course.objects.create(
                course_name=validated_data['course_name'],
                creator_name=User.objects.get(username=validated_data['creator_name'])
            )
        course_detail.save()
        return course_detail

    def update(self,instance,validated_data):
        instance.course_name=validated_data.get('course_name', instance.course_name)
        instance.creator_name=User.objects.get(username=validated_data['creator_name'])
        instance.save()
        return instance

    

    
   
class TestSerializers(serializers.Serializer):

    test_name=serializers.CharField(required=True,max_length=256)
    test_duration=serializers.DurationField(required=True)
    #duration is send in seconds and djnago update it to day and hour format
    course_associated=serializers.CharField(required=True)

    class Meta:
        model=Test
        fields=('test_name','test_duration','course_associated')

    def create(self,validated_data):
        test_detail=Test.objects.create(
                test_name=validated_data['test_name'],
                test_duration=validated_data['test_duration'],
                course_associated=Course.objects.get(course_name=validated_data['course_associated'])
            )
        test_detail.save()
        return test_detail

    
    def update(self,instance,validated_data):
        instance.test_name=validated_data.get('test_name', instance.test_name)
        instance.test_duration=validated_data.get('test_duration', instance.test_duration)
        instance.course_associated=Course.objects.get(course_name=validated_data['course_associated'])
        instance.save()
        return instance
    
class QuestionSerializers(serializers.Serializer):


    question_name=serializers.CharField(required=True,max_length=256)
    answer=serializers.CharField(required=True,max_length=256)
    option_a=serializers.CharField(required=True,max_length=256)
    option_b=serializers.CharField(required=True,max_length=256)
    option_c=serializers.CharField(required=True,max_length=256)
    option_d=serializers.CharField(required=True,max_length=256)
    test_associated=serializers.CharField(required=True,max_length=256)

    class Meta:
        model=Question
        fields=('question_name','answer','option_a','option_b','option_c','option_d','test_associated')


  
    def create(self,validated_data):
        question_detail=Question.objects.create(
                question_name=validated_data['question_name'],
                answer=validated_data['answer'],
                option_a=validated_data['option_a'],
                option_b=validated_data['option_b'],
                option_c=validated_data['option_c'],
                option_d=validated_data['option_d'],
                test_associated=Test.objects.get(test_name=validated_data['test_associated'])
            )
        question_detail.save()
        return question_detail

    def update(self,instance,validated_data):
        instance.question_name=validated_data.get('question_name', instance.question_name)
        instance.answer=validated_data.get('answer', instance.answer)
        instance.option_a=validated_data.get('option_a', instance.option_a)
        instance.option_b=validated_data.get('option_b', instance.option_b)
        instance.option_c=validated_data.get('option_c', instance.option_c)
        instance.option_d=validated_data.get('option_d', instance.option_d)
        instance.test_associated=Test.objects.get(test_name=validated_data['test_associated'])
        instance.save()
        return instance


class StudentCourseSerializer(serializers.Serializer):
    student_id=serializers.CharField(required=True,max_length=256)
    course_id=serializers.CharField(required=True,max_length=256)
    
    class Meta:
        model=StudentCourse
        fields=('student_id','course_id')


    def create(self,validated_data):
        #logic
        #student id will have student username (username is a unique name)
        #course id will have the course name (coursename is a unique name)

        studentcourse_detail=StudentCourse.objects.create(
                student_id=User.objects.get(username=validated_data['student_id']),
                course_id=Course.objects.get(course_name=validated_data['course_id'])
            )

        studentcourse_detail.save()
        
        return studentcourse_detail
    


class TestAppearedSerializer(serializers.Serializer):
    student=serializers.CharField(required=True,max_length=256)
    test=serializers.CharField(required=True,max_length=256)
    start_time=serializers.TimeField()
    end_time=serializers.TimeField()
    score=serializers.IntegerField(required=True)
    class Meta:
        model=TestAppeared
        fields=('student','test','score')

    def create(self,validated_data):
        test_appeared_details=TestAppeared.objects.create(
            student=User.objects.get(username=validated_data['student']),
            test=Test.objects.get(test_name=validated_data['test']),
            start_time=validated_data['start_time'],
            end_time=validated_data['end_time'],
            score=validated_data['score']
        )
        test_appeared_details.save()
        return test_appeared_details

    def update(self,instance,validated_data):
        instance.score=validated_data.get('score',instance.score)
        instance.end_time=validated_data.get('end_time',instance.end_time)
        instance.save()
        return instance

class SelectedAnswersSerializer(serializers.Serializer):
    student=serializers.CharField(required=True,max_length=256)
    test=serializers.CharField(required=True,max_length=256)
    question=serializers.CharField(required=True)
    selected_answer = serializers.CharField(required=True,max_length=256)

    class Meta:
        model=SelectedAnswers
        fields=('student','test','question','selected_answer')

    def create(self,validated_data):
        selected_answer_details=SelectedAnswers.objects.create(
            student=User.objects.get(username=validated_data['student']),
            test=Test.objects.get(test_name=validated_data['test']),
            question=Question.objects.get(question_name=validated_data['question']),
            selected_answer=validated_data['selected_answer']
        )

        selected_answer_details.save()
        return selected_answer_details




    



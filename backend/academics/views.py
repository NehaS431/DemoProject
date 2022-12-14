from functools import partial
from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken 
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import (CourseSerializers , TestSerializers ,
QuestionSerializers ,StudentCourseSerializer ,TestAppearedSerializer , 
SelectedAnswersSerializer)
from .models import Course ,Test ,Question , StudentCourse ,TestAppeared , SelectedAnswers
# Create your views here.

def CheckStaff(self,request):
        token=AccessToken(request.headers.get('Bearer'))
        user=User.objects.get(pk=token.payload.get("user_id"))
        if user.groups.filter(name='staff').exists():
            return True
        return False

def GetUser(self,request):
    token=AccessToken(request.headers.get('Bearer'))
    user=User.objects.get(pk=token.payload.get("user_id"))
    return user

class CourseAssociate(APIView):

    authentication_classes = [JWTAuthentication]

    def GetCourse(self,pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def post(self,request):
        check=CheckStaff(self,request)
        if check:
            data=request.data
            serializer_class = CourseSerializers(data=data)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data, status=201)
            return Response(serializer_class.errors, status=400)
        else:
            return Response("Access Denied",status=400)

    def put(self,request,pk):
        check=CheckStaff(self,request)
        if check:
            course=self.GetCourse(pk)
            serializer = CourseSerializers(course, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Access Denied",status=400)

    def get(self, request, format=None):
        course = Course.objects.all()
        serializer_class = CourseSerializers(course, many=True)
        return Response(serializer_class.data)

    def delete(self, request, pk, format=None):
        check=CheckStaff(self,request)
        if check:
            course = self.GetCourse(pk)
            course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("Access Denied",status=400)
        

class TestAssociate(APIView):

    authentication_classes = [JWTAuthentication]


    def GetTest(self,pk):
        try:
            return Test.objects.get(pk=pk)
        except Test.DoesNotExist:
            raise Http404

    def post(self,request):
        check=CheckStaff(self,request)
        if check:
            data=request.data
            serializer_class = TestSerializers(data=data)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data, status=201)
            return Response(serializer_class.errors, status=400)
        else:
            return Response("Access Denied",status=400)

    def get(self, request, format=None):
        test = Test.objects.all()
        serializer_class = TestSerializers(test, many=True)
        return Response(serializer_class.data)
        
    def delete(self, request, pk, format=None):
        check=CheckStaff(self,request)
        
        if check:
            test = self.GetTest(pk)
            test.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("Access Denied",status=400)

    def put(self,request,pk):
        check=CheckStaff(self,request)
        # print(check)
        if check:
            test=self.GetTest(pk)
            # print("test")
            #id is 2 for the current test

            serializer = TestSerializers(test, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Access Denied",status=400)


class QuestionAssociate(APIView):
    authentication_classes = [JWTAuthentication]

    def GetQuestion(self,pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def post(self,request):
        check=CheckStaff(self,request)
        if check:
            data=request.data
            serializer_class = QuestionSerializers(data=data)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data, status=201)
            return Response(serializer_class.errors, status=400)
        else:
            return Response("Access Denied",status=400)

    def get(self, request, format=None):
        question = Question.objects.all()
        serializer_class = QuestionSerializers(question, many=True)
        return Response(serializer_class.data)

    def delete(self, request, pk, format=None):
        check=CheckStaff(self,request)
        
        if check:
            question = self.GetQuestion(pk)
            question.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("Access Denied",status=400)

    def put(self,request,pk):
        check=CheckStaff(self,request)
        if check:
            question=self.GetQuestion(pk)
            serializer = QuestionSerializers(question, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Access Denied",status=400)


class StudentCourseAssociate(APIView):
    def GetCourseID(self,pk):
        try:
            return StudentCourse.objects.get(pk=pk)
        except StudentCourse.DoesNotExist:
            raise Http404

    def post(self,request):
        data=request.data
        serializer_class = StudentCourseSerializer(data=data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=201)
        return Response(serializer_class.errors, status=400)

    def get(self,request):
        # pass
        #get username through getuser function and 
        #return course details related to user
        user=GetUser(self,request)
        # print(user,"USER IS HERE")
        #get the user name id 
        user_Data=User.objects.get(username=user)
        # print("User data: ",user_Data.id)
        user_list=StudentCourse.objects.filter(student_id=user_Data.id)
        serializer_data=StudentCourseSerializer(user_list, many=True).data
        return Response(serializer_data)

    def delete(self,request,pk):
        #pk here refers to the course id
        required_user=StudentCourse.objects.get(pk=pk)
        required_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
       
        
class TestAppearedAssociate(APIView):

    def GetTestAppeared(self,pk):
        try:
            return TestAppeared.objects.get(pk=pk)
        except TestAppeared.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        test_appeared = TestAppeared.objects.all()
        serializer_class = TestAppearedSerializer(test_appeared, many=True)
        return Response(serializer_class.data)

    def post(self,request):
        data=request.data
        serializer_class = TestAppearedSerializer(data=data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=201)
        return Response(serializer_class.errors, status=400)
    #the put method will be called when we submit the test
    def   put(self,request,pk):
        test_appeared=self.GetTestAppeared(pk)
        serializer = TestAppearedSerializer(test_appeared, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class SelectedAnswersAssociate(APIView):
    def get(self, request, format=None):
        selected_answer_details = SelectedAnswers.objects.all()
        serializer_class = SelectedAnswersSerializer(selected_answer_details, many=True)
        return Response(serializer_class.data)

    def post(self,request):
        data=request.data
        serializer_class = SelectedAnswersSerializer(data=data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=201)
        return Response(serializer_class.errors, status=400)



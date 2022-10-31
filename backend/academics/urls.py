from django.urls import path
from . import views
from .views import (CourseAssociate , TestAssociate ,TestAppearedAssociate,
QuestionAssociate,StudentCourseAssociate , SelectedAnswersAssociate)


urlpatterns=[
    path('createcourse/',CourseAssociate.as_view(),name='CourseAssociate'),
    path('updatecourse/<int:pk>/',CourseAssociate.as_view(),name='CourseAssociate'),
    path('viewcourses/',CourseAssociate.as_view(),name='CourseAssociate'),
    path('deletecourse/<int:pk>/',CourseAssociate.as_view(),name='CourseAssociate'),
    path('createtest/',TestAssociate.as_view(),name='TestAssociate'),
    path('viewtest/',TestAssociate.as_view(),name='TestAssociate'),
    path('deletetest/<int:pk>/',TestAssociate.as_view(),name='TestAssociate'),
    path('updatetest/<int:pk>/',TestAssociate.as_view(),name='TestAssociate'),
    path('createquestion/',QuestionAssociate.as_view(),name='QuestionAssociate'),
    path('viewquestion/',QuestionAssociate.as_view(),name='QuestionAssociate'),
    path('deletequestion/<int:pk>/',QuestionAssociate.as_view(),name='QuestionAssociate'),
    path('updatequestion/<int:pk>/',QuestionAssociate.as_view(),name='QuestionAssociate'),
    path('createstudentassociatedcourse/',StudentCourseAssociate.as_view(),name='StudentCourseAssociate'),
    path('viewstudentassociatedcourse/',StudentCourseAssociate.as_view(),name='StudentCourseAssociate'),
    path('deletestudentassociatedcourse/<int:pk>/',StudentCourseAssociate.as_view(),name='StudentCourseAssociate'),
    path('create-testappeared/',TestAppearedAssociate.as_view(),name='TestAppearedAssociate'),
    path('view-testappeared/',TestAppearedAssociate.as_view(),name='TestAppearedAssociate'),
    path('submit-testappeared/<int:pk>/',TestAppearedAssociate.as_view(),name='TestAppearedAssociate'),
    path('create-selectedans/',SelectedAnswersAssociate.as_view(),name='SelectedAnswersAssociate'),
    path('views-selectedans/',SelectedAnswersAssociate.as_view(),name='SelectedAnswersAssociate'),
]
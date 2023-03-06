from django.urls import path
from course import views

urlpatterns = [
    path('create', views.CreateCourseView.as_view()),
    path('readbySem', views.GetCourseByProgramView.as_view()),
]


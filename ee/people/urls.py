from django.urls import path
from people import views

urlpatterns = [
    path('create', views.PeopleView.as_view()),
    path('read', views.GetPeopleView.as_view())
]

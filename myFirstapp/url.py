
from django.contrib import admin
from django.urls import path
from  myFirstapp import views
urlpatterns = [
    path('',views.index ),
    path('politics/',views.politics ,name="politics"),
]

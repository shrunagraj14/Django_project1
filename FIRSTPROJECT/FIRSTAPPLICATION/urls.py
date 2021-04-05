from django.urls import path
from FIRSTAPPLICATION import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('about', views.about),
]

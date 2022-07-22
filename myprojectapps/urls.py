"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views
from . import views1
from . import views2

urlpatterns = [

    path('', views.index, name="bookindex"),
    path('books/', views.books),
    path('all/', views.all),
    path('filterbybookname/', views.filterbybookname, name='filterbybookname'),
    path('filterbyprice/', views.filterbyprice, name="filterbyprice"),
    path('simplebook/', views.simplebook, name="simplebook"),
    path('search/', views.searchbooks, name='search'),
    path('aggregates/', views.aggregates, name="aggregate"),
    path('head/', views.header, name="head"),
    path('bookapp/', views.bookapp, name="bookapp"),
    path('quiz/', views.quiz, name="quiz"),
    path('htmlquestion/', views.htmlquestion, name="htmlquestion"),
    path('session/', views.session),
    path('result/', views.result),
    path("login/", views.login, name="login"),
    path("home/", views.home),
    path("logout/", views.logout),
    path("datastore/", views.datastore),
    path("simpledesign/", views.simpledesign),
    path("simpledesign_d/", views.simpledesign_d),
    path("saveform/", views.savedata),
    path("delete/", views.delete),
    path("weather/", views1.weather),
    # path("time/", views1.time),

]

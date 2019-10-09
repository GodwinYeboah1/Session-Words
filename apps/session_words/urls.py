from django.conf.urls import url,include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^session_words$', views.home),
    url(r'^add$', views.new),
    url(r'^clear$', views.clear),
]

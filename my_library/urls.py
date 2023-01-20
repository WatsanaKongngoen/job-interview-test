import imp
from django.conf.urls import url
from django.contrib import admin
from todo_list import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^my_index/', views.index),
]

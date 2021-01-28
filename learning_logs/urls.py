""" Defines URL patterns fot learning_logs. """
from django.urls import path
from . import views


app_name = 'learning_logs'
urlpatterns = [
    # The Home page.
    path('', views.index, name='index'),
]

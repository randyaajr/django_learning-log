""" Defines URL patterns fot learning_logs. """
from django.urls import path
from . import views


app_name = 'learning_logs'
urlpatterns = [
    # The Home page.
    path('', views.index, name='index'),
    # This is the page which shows the topics
    path('topics/', views.topics, name='topics'),
    # Detailed page for a single topic.
    path('topics/<int:topic_id>/', views.topics, name='topics'),
]

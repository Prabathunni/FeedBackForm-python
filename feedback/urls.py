from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('feedback', views.submit_feedback, name='submit_feedback')
]

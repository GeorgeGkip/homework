from . import views
from django.urls import path

urlpatterns = [
    path('', views.subjects_view, name='subjects'),
]

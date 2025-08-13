from django.shortcuts import render
from .models import Subject

def subjects_view(request):
  sub_list = Subject.objects.all()
  
  return render(request, 'subjects/subjects.html', {'sub_list':sub_list})
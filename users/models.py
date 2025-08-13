from django.db import models
from django.contrib.auth.models import AbstractUser
from subjects.models import Subject

class CustomUser(AbstractUser):

  bio = models.TextField(max_length=500, blank=True, null=True)
  
  def get_role(self):
    if hasattr(self, 'teacher'):
      return 'Teacher'
    elif hasattr(self, 'student'):
      return 'Student'
    return 'Unknown'
  
  
  def __str__(self):
    return self.first_name + ' ' + self.last_name
  

class Teacher(CustomUser):
  
  subjects_teaching = models.ManyToManyField(Subject, related_name='subjects_teaching', blank=True)
  
  class Meta:
    verbose_name = 'Teacher'
    verbose_name_plural = 'Teachers'
    
  def __str__(self):
    return self.first_name + ' ' + self.last_name
  
class Student(CustomUser):
  
  subjects_taught = models.ManyToManyField(Subject, related_name='subjects_taught', blank=True)
  
  class Meta:
    verbose_name = 'Student'
    verbose_name_plural = "students"
  
  def __str__(self):
    return self.first_name + ' ' + self.last_name
  

class TeacherStudentRelation(models.Model):
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='student_relationships')
  student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='teacher_relationships')
  
  def __str__(self):
    return f'{self.teacher.first_name} teaches {self.student.first_name}' 
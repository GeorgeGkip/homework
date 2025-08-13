from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Teacher, Student


class UserTypeForm(forms.Form):
    USER_TYPE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, widget=forms.RadioSelect)


class CustomUserCreationForm(UserCreationForm):
  
  bio = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'required':False}))
  
  class Meta:
    model = CustomUser
    fields = ('username', 'first_name', 'last_name', 'email', 'bio')
  
  def __init__(self, *args, **kwargs):
    super(CustomUserCreationForm, self).__init__(*args, **kwargs)
    
    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['first_name'].widget.attrs['class'] = 'form-control'
    self.fields['last_name'].widget.attrs['class'] = 'form-control'
    self.fields['email'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['class'] = 'form-control'  
    
class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = CustomUser
    fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'bio')

 
    
    
class TeacherRegisterForm(CustomUserCreationForm):
  model = Teacher
  fields = CustomUserCreationForm.Meta.fields + ('subjects_teaching',)
  

class StudentRegisterForm(CustomUserCreationForm):
  model = Student
  fields = CustomUserCreationForm.Meta.fields + ('subjects_taught',)
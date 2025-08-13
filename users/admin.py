from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Teacher, Student
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Define inlines for the child models
class TeacherInline(admin.StackedInline):
    model = Teacher
    can_delete = False  # Prevent deleting the role without deleting the user
    verbose_name_plural = 'Teacher Info'
    # Optional: specify fields if you don't want all of them
    # fields = ['subjects_teaching']

class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'Student Info'
    # Optional: specify fields
    # fields = ['subjects_taught']

# Customize the CustomUserAdmin
class CustomUserAdmin(UserAdmin):
    # Use the forms you created for the admin interface
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = get_user_model()
    
    # Add 'bio' to the list display
    list_display = UserAdmin.list_display + ('bio',)

    # Override the fieldsets for both the change and add forms to include 'bio'
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('bio',)}),
    )

    # Inlines for the user roles
    inlines = [TeacherInline, StudentInline]

    def get_inlines(self, request, obj=None):
        if obj and hasattr(obj, 'teacher'):
            return [TeacherInline]
        if obj and hasattr(obj, 'student'):
            return [StudentInline]
        return self.inlines


admin.site.register(get_user_model(), CustomUserAdmin)
from django import forms
from django.contrib.auth.models import User
from .models import Employee

class EmployeeForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ExtraInfoEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('employee_status',)


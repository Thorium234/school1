from django import forms
from .models import Book,Student

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        exclude=['created',]

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        exclude=['created',]
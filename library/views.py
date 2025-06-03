from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import Book,Student
from .forms import BookForm,StudentForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate
from django.contrib.auth.models import User


@login_required
def Book_list(response):
    book=Book.objects.all()
    return render(response,'books/book_list.html',{'book':book})

def Book_create(response):
    form=BookForm(response.POST or None)
    if response.method =='POST':
        form=BookForm(response.POST or None)
        if form.is_valid():
            form.save()
            return redirect('Book_list')
    else:
        form=BookForm(response.POST or None)    
    return render(response,'books/book_form.html',{'form':form})

def Book_edit(response,pk):
    book=get_object_or_404(Book,pk=pk)
    form=BookForm(response.POST or None ,instance=book)
    if response.method =='POST':
        form=BookForm(response.POST or None,instance=book)
        if form.is_valid():
            form.save()
            return redirect('Book_list')
    else:
        form=BookForm(response.POST or None, instance=book)
    return render(response,'books/book_form.html',{'form':form})

def Book_delete(response,pk):
    book=get_object_or_404(Book,pk=pk)
    form=BookForm(response.POST or None ,instance=book)
    if response.method =='POST':
        book.delete()
        return redirect('Book_list')
    return render(response,'books/book_delete_cornfirm.html',{'book':book})


#students views

@login_required
def student_list(response):
    student=Student.objects.all()
    return render(response,'students/student_list.html',{'student':student})

def student_create(response):
    form=StudentForm(response.POST or None)
    if response.method =='POST':
        form=StudentForm(response.POST or None)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form=StudentForm(response.POST or None)    
    return render(response,'students/student_form.html',{'form':form})

def student_edit(response,pk):
    student=get_object_or_404(Student,pk=pk)
    form=StudentForm(response.POST or None ,instance=student)
    if response.method =='POST':
        form=StudentForm(response.POST or None,instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form=StudentForm(response.POST or None, instance=student)
    return render(response,'students/student_form.html',{'form':form})

def student_delete(response,pk):
    student=get_object_or_404(Student,pk=pk)
    form=StudentForm(response.POST or None ,instance=student)
    if response.method =='POST':
        student.delete()
        return redirect('student_list')
    return render(response,'students/student_delete_cornfirm.html',{'student':student})

@login_required
def profile_user(request):
    if User.is_authenticated:
        return render(request,'registration/profile.html')
    else:
        return HttpResponse(request,'you must be logged in')


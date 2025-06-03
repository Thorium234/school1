from django.urls import path
from . import views

urlpatterns = [
    path('profile_user/',views.profile_user,name="profile_user"),
    path('Book_list/',views.Book_list,name="Book_list"),
    path('create/',views.Book_create,name="Book_create"),
    path('edit<int:pk>/',views.Book_edit,name="Book_edit"),
    path('delete<int:pk>/',views.Book_delete,name="Book_delete"),
    #urls for students
    path('student_list/',views.student_list,name="student_list"),
    path('student_create/',views.student_create,name="student_create"),
    path('student_edit<int:pk>/',views.student_edit,name="student_edit"),
    path('student_delete<int:pk>/',views.student_delete,name="student_delete"),
]
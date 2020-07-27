from django.conf.urls import url
from django.urls import include, path

from .api.schoolapi import SchoolList
from .api.studentapi import StudentAPI
from .views.exam import logout_request, user_home, user_login
from .views.student import (StudentHome, student_home, student_welcome,
                            user_signup)
from .views.teacher import DetailView, StudentDetails, TeacherHome

urlpatterns = [
    path('', user_home, name='home'),
    path('singup', user_signup, name='signup'),
    path('signin', user_login, name='login'),
    path('student', StudentHome.as_view(), name='student'),
    path('teacher', TeacherHome.as_view(), name='teacher'),
    path('logut', logout_request, name='studentlogout'),
    path('accounts/login/', user_login, name='accountlogin'),
    url(r'^(?P<pk>[-\w]+)/$', StudentDetails.as_view(), name='student'),
    url(r'^details/(?P<student_id>\d{1,18})/$',StudentDetails.as_view(), name='details'),
    path('welcome', student_welcome, name='welcome'),
    path('api/listschool/', SchoolList.as_view(), name="liststudent"),
    path('api/listschool/<int:pk>', SchoolList.as_view(), name="liststudent"),
    path('api/liststudent/', StudentAPI.as_view(), name="liststudent"),  
    path('api/liststudent/<int:pk>', StudentAPI.as_view(), name="liststudent"),



]

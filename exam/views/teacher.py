import json
import smtplib
import uuid
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
from django.contrib import messages
from django.contrib.auth import authenticate as auth_login
from django.contrib.auth import login as login_default
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, TemplateView

from exam.forms import StudentsList
from exam.models import Student

# Create your views here.

@method_decorator([login_required], name='dispatch')
def teacher_home(request):
    context_object_name = 'students'
    return render(request, 'teachers/home.html', {})


@method_decorator([login_required], name='dispatch')
class TeacherHome(ListView):
    context_object_name = 'students'
    model = Student
    paginate_by = 10
    template_name = 'teachers/home.html'
    print("...TeacherHome.......")

    def get_context_data(self, **kwargs):
        context = super(TeacherHome, self).get_context_data(**kwargs)
        print("...TeacherHome.......", context)
        return context



@method_decorator([login_required], name='dispatch')
class StudentDetails(DetailView):
    context_object_name = 'students_details'
    model = Student
    template_name = 'teachers/details.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test'] = 'Test Context passing'
        return context

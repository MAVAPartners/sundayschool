import uuid

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
from django.views.generic import ListView, TemplateView

from exam.forms import UserLogin, UserSingupForm, UserStudentFrom
from exam.models import Student
from exam.views.exam import sendinblue_emailSend

EMAIL_HOST_USER = 'mava.monitor@gmail.com'
EMAIL_HOST_PASSWORD = 'Mavabc@1234'


# Create your views here.

def user_signup(request):

    registered = False
    print('....user_signup........', request.method)
    if request.POST:
        user_form = UserSingupForm(data=request.POST)
        studer_form = UserStudentFrom(data=request.POST)

        if user_form.is_valid() and studer_form.is_valid():

            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.username = uuid.uuid4().hex[:6].upper()
            user.is_student = True
            user.save()


            student = studer_form.save(commit=False)
            student.user = user
            student.accademicYear = 2020
            student.status = 0
            student.save()

            registered = True
            htmlMessage = ("<html><head></head><body><p>Hello, %s</p>Thank you for registering for the November 2020 catechism examination. <br> Your application will be approved after the screening process. <br> Your user name is %s. Please note down this number. Please use the registration number as your username to log into to the examination portal. <br><br> Regards, <br> Centralized Exam Panel Director  <br> ------------------------------------------------------- <br>Powered by Team MAVA</p></body></html>" %(user.first_name, user.username ))
            #messages.success(request, 'Successfully registredered for November exam, Sending email for updates. Username is : '+user.username)
            data = { "sender":{  
                            "name":"Mava Partners",
                            "email":"mava.partnersin@gmail.com"},
                            "to":[  
                            {  
                                "email":"mava.partnersin@gmail.com",
                                "name":"Mava Partners"
                            },
                            {  
                                "email":user.email,
                                "name":user.first_name
                            }
                            ],
                            "subject":"Malankara Syrian Orthodox Sunday School Association of North America",
                            "htmlContent":htmlMessage
            }
            sendinblue_emailSend(data)
            urlWelcome = '/welcome?username='+user.username
            return HttpResponseRedirect(urlWelcome)
        else:
            print("Form validate..failed.....")
            print(user_form.errors, studer_form.errors)
    else:
        user_form = UserSingupForm()
        studer_form = UserStudentFrom()

    return render(request, 'registration/signup_form.html', {"user_form" : user_form, "studer_form" : studer_form, "registered" :registered })


def student_home(request):        
    return render(request, 'students/home.html', {})

def student_welcome(request):
    username = request.GET.get('username')
    print(username)
    return render(request, 'registration/welcome.html', {"username":username})


@method_decorator([login_required], name='dispatch')
class StudentHome(ListView):
    context_object_name = 'students'
    model = Student
    template_name = 'students/home.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test'] = 'Test Context passing'
        return context

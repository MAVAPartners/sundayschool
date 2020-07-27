import requests
from django.contrib import messages
from django.contrib.auth import authenticate as auth_login
from django.contrib.auth import login as login_default
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from exam.forms import UserLogin

EMAIL_HOST_USER = 'mava.monitor@gmail.com'
EMAIL_HOST_PASSWORD = 'Mavabc@1234'

def user_home(request):
    return render(request, 'home.html', {})


def user_login(request):
    print('.....user login....first.....', request.method)
    if request.POST:
        user_form = AuthenticationForm(data=request.POST)
        print('.....user login....second.....', user_form.is_valid())
        username = request.POST['username']
        password = request.POST['password']
        print(password,'.....user login....second.....', username)
        if user_form.is_valid():
            authUser = auth_login(
                request, username=username, password=password)
            print(username, '.....user login....444.....', authUser)
            if authUser is not None:
                userData = login_default(
                    request, authUser)
                print(request.user.is_staff, '.....user login....5555.....', request.user.is_student)
                if request.user.is_superuser:
                    messages.success(
                        request, 'You are now successfully loged in')
                    return HttpResponseRedirect('/admin/')
                elif request.user.is_staff and (request.user.is_student is False) :
                    messages.success(
                        request, 'You are now successfully loged in')
                    return HttpResponseRedirect('/teacher')
                elif request.user.is_student:
                    messages.success(
                        request, 'You are now successfully loged in')
                    url = reverse('student', kwargs={'pk': request.user.student.id})
                    return HttpResponseRedirect(url)
                else:
                    logout(request)
                    messages.error(
                        request, 'Please request Admin to approve this user authentication')
                    user_form = UserLogin()
            else:
                messages.error(request, 'Invalid username / password')
                user_form = UserLogin()
        else:
            messages.error(request, 'Invalid username / password')
            user_form = UserLogin()


        print('.......user login..........')
    else:
        user_form = UserLogin()
    return render(request, 'registration/login.html', {"user_form" : user_form})


def logout_request(request):
    logout(request)
    messages.success(request, 'You are now successfully logged out')
    return HttpResponseRedirect('/signin')

def sendinblue_emailSend(data):
    apiUrl = 'https://api.sendinblue.com/v3/smtp/email'
    header = {'accept': 'application/json', 'api-key': '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',
              'content-type': 'application/json'}
    '''data = { "sender":{  
      "name":"Rajesh M P",
      "email":"rajeshpillai23@gmail.com"},
      "to":[  
      {  
         "email":"mava.partnersin@gmail.com",
         "name":"Mava Partners"
      }
      ],
      "subject":"Hello world",
      "htmlContent":"<html><head></head><body><p>Hello,</p>This is my first transactional email sent from Sendinblue.</p></body></html>"
    }'''

    response = requests.post(apiUrl, json=data, headers=header)
    data = response.content.decode('utf-8')
    print('..sendinblue_emailSend..response....success....', data)

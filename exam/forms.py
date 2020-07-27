from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.validators import RegexValidator

from exam.models import School, Student, User

#from django.contrib.auth.models import User


CHOICES=[('Male','Male'),
         ('Female','Female')]

class UserLogin(AuthenticationForm):
    username = forms.CharField(required=True, help_text='Required. Username')
    username.widget.attrs.update({'class': 'form-control', 'placeholder': 'User Name', 'style': 'border-color:#8a8e94'})
    password = forms.CharField(widget = forms.PasswordInput())
    password.widget.attrs.update({'class': 'form-control', 'placeholder': 'Password', 'style': 'border-color:#8a8e94'})

    class Meta():
        model = User
        fields = ("username", "password")

    def clean(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
       return self.cleaned_data

class UserSingupForm(forms.ModelForm):
    email = forms.CharField(required=True)
    email.widget.attrs.update({'class': 'form-control', 'placeholder': 'Email', 'style': 'border-color:#8a8e94'})
    password = forms.CharField(widget = forms.PasswordInput())
    password.widget.attrs.update({'class': 'form-control', 'placeholder': 'Password', 'style': 'border-color:#8a8e94'})
    first_name = forms.CharField(required=True)
    first_name.widget.attrs.update({'class': 'form-control', 'placeholder': 'First Name', 'style': 'border-color:#8a8e94'})
    last_name = forms.CharField(required=True)
    last_name.widget.attrs.update({'class': 'form-control', 'placeholder': 'Last Name', 'style': 'border-color:#8a8e94'})
    
    class Meta():
        model = User
        fields = ("email", "password", "first_name", "last_name")



class UserStudentFrom(forms.ModelForm):

    #school = forms.ModelMultipleChoiceField(queryset=School.objects.all())
    school = forms.ModelChoiceField(queryset=School.objects.all())
    #school = forms.ChoiceField(choices=School.objects.filter().values("name"))
    school.widget.attrs.update({'class': 'form-control', 'placeholder': 'Sunday School Name', 'style': 'border-color:#8a8e94'})
    gender = forms.ChoiceField(choices=CHOICES,)
    gender.widget.attrs.update({'class': 'form-control', 'style': 'border-color:#8a8e94'})
    age = forms.IntegerField(required=True,)
    age.widget.attrs.update({'class': 'form-control', 'placeholder': 'Age', 'style': 'border-color:#8a8e94'})
    address = forms.CharField(required=True, label='Address 1')
    address.widget.attrs.update({'class': 'form-control', 'placeholder': 'Address 1', 'style': 'border-color:#8a8e94'})
    address2 = forms.CharField(required=True, label='Address 2')
    address2.widget.attrs.update({'class': 'form-control', 'label' : 'Address 1' ,'placeholder': 'Address 2', 'style': 'border-color:#8a8e94'})

    city = forms.CharField(required=True)
    city.widget.attrs.update({'class': 'form-control', 'placeholder': 'City', 'style': 'border-color:#8a8e94', 'id' : 'city'})
    state = forms.CharField(required=True)
    state.widget.attrs.update({'class': 'form-control', 'placeholder': 'State', 'style': 'border-color:#8a8e94', 'id' : 'state'})
    zipcode = forms.IntegerField(required=True, label='ZIP')
    zipcode.widget.attrs.update({'class': 'form-control', 'placeholder': 'ZIP', 'style': 'border-color:#8a8e94', 'id' : 'zipcode'})
    phoneno = forms.CharField(required=True, label='Phone')
    phoneno.widget.attrs.update({'class': 'form-control', 'placeholder': 'Phone', 'style': 'border-color:#8a8e94','data-mask': '(999) 999-9999'})

    '''def clean(self):
        cleaned_data = super(UserStudentFrom, self).clean()
        phone = cleaned_data.get('state')
        print(",....clean......", phone)

    def clean_state(self):
        phone = self.cleaned_data['state']
        print(",....clean_homePhone......", phone)
        if len(phone) >= 5:
            raise forms.ValidationError('Too many characters ...')
        return phone'''

    class Meta():
        model = Student
        fields = ("gender", "age", "school",
              "address", "address2","city", "state", "zipcode", "phoneno")

class StudentsList(forms.ModelForm):

    id = forms.NumberInput()
    username = forms.CharField(max_length=255)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    name = forms.CharField(max_length=255)

    class Meta:
        model = Student
        fields = ('id', 'username', 'first_name', 'last_name','name')

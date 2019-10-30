# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# #from phonenumber_field.formfields import PhoneNumberField
# from django.contrib.auth.models import User
#
#
# class UserCreationForm(forms.Form):
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)
#     address = forms.CharField(
#         max_length=2000,
#         widget=forms.Textarea(),
#     )
#     email = models.EmailField(max_length=50, primary_key=True)
#     phonenumber = forms.IntegerField(required=False)
#
# class Meta:
#     model = User
#     fields = ('first_name', 'last_name', 'address', 'email', 'phonenumber' )
#
#
# class SignUpForm(UserCreationForm):
#
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#     phone = forms.CharField(max_length=30)
#     address = forms.CharField(
#         max_length=2000,
#         widget=forms.Textarea(),
#     )
#
#
#     #class Meta:
#         #model = User
#         #fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )


from django import forms
from .models import *
from django.contrib.auth.models import Group, User


class LoginForm(forms.Form):
    """
    Form to log in a current user
    """
    username = forms.CharField(max_length=50, label='Username',
                               widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class RegisterForm(forms.Form):
    """
    Form to register a new user
    """
    username = forms.CharField(max_length=50, label='Username',
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=50, label='first name',
                                 widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=50, label='first name',
                                widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email = forms.CharField(max_length=50, label='Email',
                            widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone = forms. CharField(max_length=50, label='phone',
                             widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    DESIGNATION_CHOICES = [
        ('super_admin', 'super admin'),
        ('senior_system_admin', 'senior system admin'),
        ('system_admin', 'system admin'),
    ]
    designation = forms.CharField(label='Designation', widget=forms.Select(choices=DESIGNATION_CHOICES))


class TaskAddForm(forms.ModelForm):
    """
    Form to add new ticket
    """
    class Meta:
        model = Task
        fields = '__all__'
        labels = {
            "assigned_to": "Assigned to",
            "start_date": "start date",
            "end_date": "End date",
            "subject": "Subject",
            "message": "Message",
            "priority": "Priority"

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].queryset = User.objects.filter(groups__name='system_admin')


# Form to edit the details of the current user
class EditForm(forms.ModelForm):
    username = forms.CharField(max_length=50, label='Username',
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=50, label='first name',
                                 widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=50, label='first name',
                                widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email = forms.CharField(max_length=50, label='Email',
                            widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(max_length=50, label='phone',
                            widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))

    DESIGNATION_CHOICES = [
        ('super_admin', 'super admin'),
        ('senior_system_admin', 'senior system admin'),
        ('system_admin', 'system admin'),
    ]
    designation = forms.CharField(label='Designation',
                                  widget=forms.Select(choices=DESIGNATION_CHOICES))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'phone')
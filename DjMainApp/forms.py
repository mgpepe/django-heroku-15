from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import re

class ResourceForm(forms.Form):
    link=forms.CharField(required=True, min_length=6)

class RegistrationForm(forms.Form):
    email = forms.EmailField(required=True)
    name = forms.CharField(min_length=3, max_length=50, required=True,)
    # last_name = forms.CharField(min_length=3, max_length=20, required=True,)
    password = forms.CharField(min_length=3, widget=forms.PasswordInput())
#    repeat_pass = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
#        repeat_pass = cleaned_data.get("repeat_pass")

#        if password != repeat_pass:
#            raise forms.ValidationError("The passwords do not match")

        count= User.objects.filter(email=cleaned_data.get("email")).count()
        if count!=0:
            raise  forms.ValidationError("There is already a user with this email")

        return cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        #user email for username => Email Backend

        try:
            user1=User.objects.get(email=cleaned_data.get("email"))
            if not user1.is_active:
                raise forms.ValidationError("Account not activated")
        except:
            pass

        user = authenticate(username=cleaned_data.get("email"), password=cleaned_data.get('password'))
        if not user:
            raise forms.ValidationError("Wrong credentialsz")
        return cleaned_data


class ForgotPassForm(forms.Form):
    email=forms.EmailField(required=True)

    def clean(self):
        cleaned_data = super(ForgotPassForm, self).clean()
        if not User.objects.filter(email=cleaned_data.get("email")).exists():
            raise forms.ValidationError("There is no user with this email in our DB.")
        return cleaned_data

class ChangePassForm(forms.Form):
    new_pass = forms.CharField(widget=forms.PasswordInput())
    new_pass2 = forms.CharField(widget=forms.PasswordInput())

    def clean(self):

        cleaned_data = super(ChangePassForm, self).clean()

        if len(cleaned_data.get("new_pass"))<3 or len(cleaned_data.get("new_pass2"))<3:
            raise forms.ValidationError("Passwords need to be at least 3 characters long")

        if cleaned_data.get("new_pass") != cleaned_data.get("new_pass2"):
            raise forms.ValidationError("Passwords don't match.");
        return cleaned_data

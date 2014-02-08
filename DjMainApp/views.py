from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from DjMainApp.forms import RegistrationForm, LoginForm, ForgotPassForm, ChangePassForm, SetNewPassForm
from DjMainApp.models import UserProfile
from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.mail import EmailMessage
import pdb
from django.core.urlresolvers import reverse
import random
from django.db.utils import IntegrityError
from django.http import HttpResponse
import simplejson
from datetime import datetime

# Create your views here.
def splash(request):
	if request.user.is_authenticated():
		return redirect(reverse("home"))
	data=dict()
	return render_to_response("DjMainApp/splash.html",data, context_instance=RequestContext(request))

@login_required
def home(request):

	data=dict()

	data['user']=request.user
	return render_to_response("DjMainApp/home.html",data, context_instance=RequestContext(request))


def register(request):
#    if request.user.is_authenticated == True:
#        return redirect(reverse("home"))
	form = RegistrationForm(request.POST or None)
	if form.is_valid():
		try:
			name = form.cleaned_data["name"]
			name_array = name.partition(" ");
			first_name = name_array[0]
			last_name = name_array[2]
			usrname = get_unique_username(first_name)
			email = form.cleaned_data["email"]
			passw = form.cleaned_data["password"]
			new_user = User.objects.create_user(
				username=usrname,
				email=email,
				first_name=first_name,
				last_name=last_name,
				password=passw)
			new_user.is_active = True
			new_user.save()
			user = authenticate(username=email, password=passw)
			login(request, user)

			return redirect(reverse('home'))
		except IntegrityError:
			return render_to_response("DjMainApp/error.html")
	data =dict()
	data["form"]=form
	return render_to_response("DjMainApp/registration.html", data, context_instance=RequestContext(request))

def login_view(request):
#    if request.user.is_authenticated == True:
#        return redirect(reverse("home"))
	form = LoginForm(request.POST or None)
	redirect_to = request.REQUEST.get(REDIRECT_FIELD_NAME, '')

	if form.is_valid():
		passw=form.cleaned_data.get("password")
		emailw = form.cleaned_data.get("email")
		user = authenticate(username=emailw, password=passw)
		login(request, user)
		if redirect_to:
			return redirect(redirect_to)
		else:
			return redirect(reverse("splash"))

	data = dict()
	data["form"]=form
	return render_to_response("DjMainApp/login.html", data,context_instance=RequestContext(request));

def logout_user(request):
	logout(request)
	return redirect(reverse("splash"))
	# return render_to_response("auth/logout.html",None, context_instance=RequestContext(request))

def forgot_pass(request):
	form = ForgotPassForm(request.POST or None)
	data= dict()
	data["new_pass_given"]=False
	data["form"]=form
	data['html_style']='dark'
	if request.method == "POST" and form.is_valid():
		user = get_object_or_404(User, email=form.cleaned_data["email"])
		new_pass=get_random_string(6)
		user.set_password(new_pass)
		user.save()
		msg=EmailMessage(from_email=u"DjangoHeroku <no-reply@djangoheroku.com>", to=[user.email], subject=u"New Password", body=u"Your new password is {0}".format(new_pass))
		msg.send()
		data["new_pass_given"]=True
		data["success"]=True
		data["email"]=form.cleaned_data["email"]
	return render_to_response("DjMainApp/forgot_pass.html", data, context_instance=RequestContext(request))

@login_required
def change_pass(request):
	form = ChangePassForm(request.POST or None)
	data= dict()
	data["form"]=form
	if request.method == "POST" and form.is_valid():
		request.user.set_password(form.cleaned_data["new_pass"])
		request.user.save()
		data["success"]=True
	return render_to_response("DjMainApp/changepass.html", data, context_instance=RequestContext(request))

def get_unique_username(first_name):
	# the [0] is used to access variables of parent function
	uname = [first_name.replace(" ", "").lower()]
	res = [User.objects.filter(username=uname[0])]
	first_run = [True]
	def stuff():
		if first_run[0]:
			first_run[0] = False
		else:
			uname[0]+=str(random.randint(1,9))
		res[0] = User.objects.filter(username=uname[0])
	while(res[0]):
		stuff()
	return uname[0];


def set_new_pass(request, code=None):
	data={}
	if request.method == "POST":
		form = SetNewPassForm(request.POST)
		if form.is_valid():
			xcode = form.cleaned_data['pass_reset_code']
			try:
				up = UserProfile.objects.get(pass_reset_code=xcode)
				u = User.objects.get(pk= up.user.id)
				u.set_password(form.cleaned_data['password'])
				u.save()
				usr = authenticate(username=u.email, password=form.cleaned_data['password'])
				login(request, usr)
				return redirect(reverse('home'))
			except UserProfile.DoesNotExist:
				messages.add_message(request, messages.INFO, 'Wrong Code.')
				pass
		else:
			messages.add_message(request, messages.INFO, 'Not Valid.')
	else:
		if code is not None:
			form = SetNewPassForm(initial={'pass_reset_code':code})
		else:
			form = SetNewPassForm(None)
	data['form']=form
	return render_to_response("DjMainApp/set_new_pass.html", data, context_instance=RequestContext(request))





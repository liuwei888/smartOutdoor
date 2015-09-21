from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms 
from models import Merchant
from models import Equipment
from django.template.loader import get_template

class LoginForm(forms.Form):
	username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control input-lg'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input-lg'}))

class RegistForm(forms.Form):
	username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control input-lg'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input-lg'}))
	email = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control input-lg'}))

def regist(req):
	if req.method == 'POST':
		rf = RegistForm(req.POST)
		if rf.is_valid():
			username = rf.cleaned_data['username']
			password = rf.cleaned_data['password']
			email = rf.cleaned_data['email']
			Merchant.objects.create(merchant_login_name=username, merchant_password=password, merchant_email=email)
			response = HttpResponseRedirect('/outdoor/login')
			return response
	else:
		rf = RegistForm()
	return render_to_response('regist.html', {'rf':rf},
context_instance=RequestContext(req))

def login(req):
	if req.method == 'POST':
		lf = LoginForm(req.POST)
		if lf.is_valid():
			username = lf.cleaned_data['username']
			password = lf.cleaned_data['password']
			user = Merchant.objects.filter(merchant_login_name__exact = username, merchant_password__exact = password)
			if user:
				response = HttpResponseRedirect('/outdoor/index/')
				response.set_cookie('username', username, 3600) 
				return response
			else:
				return HttpResponseRedirect('/outdoor/login/')
	else:
		lf = LoginForm()
	return render_to_response('login.html', 
{'lf':lf}, context_instance=RequestContext(req))

def index(req):
	username = req.COOKIES.get('username', '')
	#result = Merchant.objects.filter(merchant_login_name=username)
	result = Equipment.objects.all().filter(equipment_owner=username)
	#result = Merchant.objects.all()
	return render_to_response('index.html', {'result':result})

def logout(req):
	response = HttpResponseRedirect('/outdoor/login/')
	response.delete_cookie('username')
	return response

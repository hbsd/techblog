from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile


def login_user(request):
	if request.user.is_authenticated:
		return redirect('tech_index')

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		try:
			user = User.objects.get(username=username)
		except:
			messages.error(request, 'Username does not exist')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('tech_index')
		else:
			messages.error(request, 'Username OR password is incorrect')
	return render(request, 'writers/login_register.html')


def logout_user(request):
	logout(request)
	messages.error(request, 'User was logged out!')
	return redirect('login')

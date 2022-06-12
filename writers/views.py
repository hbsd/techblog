from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm


def login_user(request):
	page = 'login'
	
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


def register_user(request):
	page = 'register'
	form = CustomUserCreationForm()

	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.username = user.username.lower()
			user.save()

			messages.success(request, 'User account was created!')
			login(request, user)
			return redirect('tech_index')
		else:
			messages.success(request, 'An error has occured during registeration')

	context = {'page': page, 'form': form}
	return render(request, 'writers/login_register.html', context)

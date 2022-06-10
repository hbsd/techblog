from django.shortcuts import render, redirect
from .models import Post
from writers.models import Profile
from .forms import PostForm


def tech_author(request, pk):
	profile = Profile.objects.get(id=pk)
	context = {'profile': profile}
	return render(request, 'blog/tech-author.html', context)


def tech_category_01(request):
	return render(request, 'blog/tech-category-01.html')


def tech_category_02(request):
	return render(request, 'blog/tech-category-02.html')


def tech_category_03(request):
	return render(request, 'blog/tech-category-03.html')


def tech_contact(request):
	return render(request, 'blog/tech-contact.html')


# Home page
def tech_index(request):
	posts = Post.objects.all()
	profiles = Profile.objects.all()
	context = {'posts': posts, 'profiles': profiles}
	return render(request, 'blog/tech-index.html', context)


# Posts page
def tech_single(request, pk):
	post_id = Post.objects.get(id=pk)
	tags = post_id.tags.all()
	profiles = Profile.objects.all()
	context = {'post': post_id, 'tags': tags, 'profiles': profiles}
	return render(request, 'blog/tech-single.html', context)


# CRUD operations
def create_post(request):
	form = PostForm()

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('tech_index')
	
	context = {'form': form}
	return render(request, 'blog/create-post.html', context)


def update_post(request, pk):
	post = Post.objects.get(id=pk)
	form = PostForm(instance=post)

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			form.save()
			return redirect('tech_index')

	context = {'form': form}
	return render(request, 'blog/create-post.html', context)


def delete_post(request, pk):
	post = Post.objects.get(id=pk)
	if request.method == 'POST':
		post.delete()
		return redirect('tech_index')
	context = {'object': post}
	return render(request, 'blog/delete-post.html', context)

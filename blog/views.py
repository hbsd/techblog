from django.shortcuts import render


def tech_author(request):
	return render(request, 'blog/tech-author.html')


def tech_category_01(request):
	return render(request, 'blog/tech-category-01.html')


def tech_category_02(request):
	return render(request, 'blog/tech-category-02.html')


def tech_category_03(request):
	return render(request, 'blog/tech-category-03.html')


def tech_contact(request):
	return render(request, 'blog/tech-contact.html')


def tech_index(request):
	return render(request, 'blog/tech-index.html')


def tech_single(request):
	return render(request, 'blog/tech-single.html')

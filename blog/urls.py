from django.urls import path
from . import views


urlpatterns = [
	path('tech_author/', views.tech_author, name='tech_author'),
	path('tech_category_01/', views.tech_category_01, name='tech_category_01'),
	path('tech_category_02/', views.tech_category_02, name='tech_category_02'),
	path('tech_category_03/', views.tech_category_03, name='tech_category_03'),
	path('tech_contact/', views.tech_contact, name='tech_contact'),
	path('', views.tech_index, name='tech_index'),
	path('tech_single/', views.tech_single, name='tech_single'),
]

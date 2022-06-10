from django.urls import path
from . import views


urlpatterns = [
	path('tech_author/<str:pk>/', views.tech_author, name='tech_author'),
	path('tech_category_01/', views.tech_category_01, name='tech_category_01'),
	path('tech_category_02/', views.tech_category_02, name='tech_category_02'),
	path('tech_category_03/', views.tech_category_03, name='tech_category_03'),
	path('tech_contact/', views.tech_contact, name='tech_contact'),
	path('', views.tech_index, name='tech_index'),
	path('tech_single/<str:pk>/', views.tech_single, name='tech_single'),

	path('create_post/', views.create_post, name='create_post'),
	path('update_post/<str:pk>/', views.update_post, name="update_post"),
	path('delete_post/<str:pk>/', views.delete_post, name="delete_post"),
]

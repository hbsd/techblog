from django.urls import path
from . import views


urlpatterns = [
	path('login/', views.login_user, name="login"),
	path('logout/', views.logout_user, name="logout"),
	path('register/', views.register_user, name="register"),
	path('edit-account/', views.edit_account, name="edit-account"),
]

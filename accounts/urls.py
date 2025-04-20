from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('registeratsiya/', views.registeratsiya, name='registeratsiya'),
    path('logout_user/',views.logout_user, name='logout_user'),
]

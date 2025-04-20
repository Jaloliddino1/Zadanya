from django.urls import path
from . import views


app_name =  'accounts'
urlpatterns = [
    path('login/', views.login_user, name='login_user'),
    path('registeratsiya/', views.registeratsiya, name='registeratsiya'),
    path('logout_user/',views.logout_user, name='logout_user'),
]

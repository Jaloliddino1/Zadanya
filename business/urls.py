from django.urls import path
from business import views


app_name = 'business'
urlpatterns = [
    path('list/', views.phone_list, name='phone_list'),
    path('create/', views.phone_create, name='phone_create'),
    path('update/<int:id>/', views.phone_update, name='phone_update'),
    path('delete/<int:id>/', views.phone_delete, name='phone_delete'),
    path('publish/<int:phone_id>/', views.publish_phone, name='publish_phone'),

]

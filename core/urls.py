from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home/',views.home_view,name='home_view')
    ]

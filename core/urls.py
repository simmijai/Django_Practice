from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    
    
    # Auth
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # path('',views.home,name='home'),
    path('home/',views.home_view,name='home_view'),
    
    path('', views.student_list, name='student_list'),
    # path('add/', views.add_student, name='add_student'),
    # path('edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('manage/', views.manage_student, name='add_student'),
    path('manage/<int:pk>/', views.manage_student, name='edit_student'),

    path('delete/<int:pk>/', views.delete_student, name='delete_student'),


    ]

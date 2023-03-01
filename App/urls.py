from . import views
from django.urls import path, include


urlpatterns =[
    path('logged-out/', views.logoutPage, name= 'logout'),
    path('login/', views.loginPage, name= 'login'),
    path('signup/', views.signUp, name= 'signup'),
    path('', views.home, name='home'),
    path('contact-profile/<str:pk>',views.contact_profile, name='profile'),
    path('create-contact/' , views.create, name='create'),
    path('update-contact/<str:pk>', views.update, name='update'),
    path('delete-contact/<str:pk>', views.delete, name='delete')
]


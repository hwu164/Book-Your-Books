from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('h/', views.home),
    path('login/', views.login),
    path('my_bookings/', views.my_bookings),
    path('book/', views.select_option, name='select_option'),
    path('test/', views.test),
    path('join/', views.join),
    path('verify/', views.verify),
    path('book-bin/', views.book_bin, name='book_bin'),
]
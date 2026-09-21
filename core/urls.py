from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('magazine/', views.magazine_view, name='magazine'),
    path('contact/', views.contact_view, name='contact'),
]
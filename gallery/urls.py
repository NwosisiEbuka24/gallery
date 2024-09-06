from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('view/<int:id>/', views.ViewPage, name='view'),
    path('edit/<int:id>/', views.UpdateView, name='edit'),
    path('search/', views.SearchQuery, name='search')
]

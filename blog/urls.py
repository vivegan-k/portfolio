from django.urls import path

from . import views

urlpatterns = [
    path('', views.highlights, name='highlights'),
    path('skillset/', views.skillset, name='skillset'),
    #path('<int:blog_id>/', views.detail, name='detail'),
]
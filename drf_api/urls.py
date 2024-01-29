"""
URL configuration for drf_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from imdbapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stream/',views.StreamPlatformAV.as_view(),name='stream'),
    path('watch/',views.WatchListAV.as_view(),name='watch'),
    # path('watch_d/<int:pk>',views.WatchDetailAV.as_view(),name='watch_d')
    # upper url is wrong please give / after <int:pk>/
    path('watch_d/<int:pk>/', views.WatchDetailAV.as_view(), name='watch_d'),


]

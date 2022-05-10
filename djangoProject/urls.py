"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from board import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', views.index),
    path('user/list/', views.user_list),
    path('user/add/', views.user_add),
    path('tpl/', views.tpl),
    path('news/', views.news),
    path('get-token/', views.get_csrf_token),
    path('doLogin/', views.login),
    path('testLogin/', views.login_test),
    path('user/info/', views.getInfo),
    path('test/ls', views.ls),
    # /usr/bin/time
    path('time/add/', views.addtime),
    path('time/get/', views.gettime),
    path('time/avg/', views.avgtime),
    path('time/getall/', views.getalltime),

    # size
    path('size/add/', views.addsize),
    path('size/getavg/', views.getAvgsize),
    path('size/get/', views.getsize),
    path('size/getall/', views.getallsize)

]

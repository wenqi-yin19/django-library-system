"""
URL configuration for books_comment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import RedirectView

from app01.views import *
from app01.views import user,admin

urlpatterns = [
    # path("admin/", admin.site.urls),
    # 首页
    path("home/", admin.home),
    # 注册
    path("register/", admin.register),
    # 登录
    path("login/", admin.login),
    # 退出
    path("loginout/", admin.loginout),

    # 管理员
    path("admin/list/", admin.admin_list),
    # 管理员添加描述
    path("admin/<int:nid>/brief/", admin.admin_brief),


    # 用户书评界面
    path("user/list/", user.user_list),
    # 用户列表
    path("user/", user.user),
    # 用户添加评论
    path("user/<int:nid>/comment/", user.user_comment),

    # 项目启动重定向到home
    path('', RedirectView.as_view(url='/home'))
]


# -*- coding: utf-8 -*-
# @Author : Author
# @Time   :2023/11/28 11:13
from django.shortcuts import render, redirect
from app01 import models
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from app01.models import User,Book
# 用户书评
def user_list(request):
    tableData=Book.objects.all()
    email = request.session['email']
    return render(request,'user_list.html',{"tableData":tableData,"email":email})

# 用户列表
def user(request):
    tableData=User.objects.all()
    email=request.session['email']
    return render(request,'user.html',{"tableData":tableData,"email":email})

# 用户评论
@csrf_exempt
def user_comment(request,nid):
    """用户评论"""
    if request.method == "GET":
        data_list = Book.objects.filter(id=nid).first()
        return render(request, "user_com.html", {"data_list": data_list})
    else:
        # 获取用户提交的评论
        comment = request.POST.get("comment")
        # 根据ID找到数据库中的数据并进行更新
        # Book.objects.filter(id=nid).update(title=title,其他字段=123)
        Book.objects.filter(id=nid).update(comment=comment)
        # 重定向回书列表
        return redirect("/user/list/")

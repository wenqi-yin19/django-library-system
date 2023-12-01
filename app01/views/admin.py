# -*- coding: utf-8 -*-
# @Author : Author
# @Time   :2023/11/28 11:13
from django.shortcuts import render, redirect
from app01 import models
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from app01.models import Admin,User,Book
def home(request):
    """首页"""
    return render(request,'home.html')

def login(request):
    """登录"""
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        if request.POST.get('identype') != '':
            # 普通用户登录
            if request.POST.get('identype') == 'user':
                # 过滤函数
                def filter_fn(item):
                    return request.POST.get('email') == item.email and request.POST.get('password') == item.password

                # 检查数据表user中是否存在账号
                users = User.objects.all()
                filter_user = list(filter(filter_fn, users))
                # 检测库中是否有账户
                if len(filter_user):
                    request.session['email'] = request.POST.get('email')
                    return redirect('/user/list/')
                else:
                    message = 'Invalid email or password'
                    return render(request,'404-error.html', {"message":message})
            # elif user_info.get('identype') == 'admin': # 管理员登录
            else:  # 管理员登录
                # 过滤函数
                def filter_fn(item):
                    return request.POST.get('email') == item.email and request.POST.get('password') == item.password

                # 检查数据表admin中是否存在账号
                users = Admin.objects.all()
                filter_user = list(filter(filter_fn, users))
                # 检测库中是否有账户
                if len(filter_user):
                    request.session['email'] = request.POST.get('email')  # session的用法同字典 session.get() or session['']
                    return redirect('/admin/list/')
                else:
                    message = 'Invalid email or password'
                    return render(request,'404-error.html',{"message":message} )

def loginout(request):
    request.session.clear()
    return redirect('/home')

def register(request):
    """注册"""
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        if request.POST.get('identype')!='':
            # 普通用户注册
            if request.POST.get('identype')=='user':
                if request.POST.get('password') != request.POST.get('passwordChecked'):
                    message = 'Passwords do not match. Please re-register.'
                    return render(request,'404-error.html', {"message":message})
                    # return '两次密码不一致'

                def filter_fn(item):
                    return request.POST.get('email') == item.email  # 检测email是否已存在

                users = User.objects.all()
                filter_list = list(filter(filter_fn, users))  # filter()过滤函数序列 第一个参数是函数 第二个是序列
                if len(filter_list):  # 如果长度不为0，说明在数据库里找到了，说明已存在
                    message = 'User already registered'
                    return render(request,'404-error.html', {"message":message})
                else:
                    User.objects.create(email=request.POST.get('email'), password=request.POST.get('password'))
                    return redirect('/login/')
                # 管理员注册
            else:
                if request.POST.get('password') != request.POST.get('passwordChecked'):
                    message = 'Passwords do not match. Please re-register.'
                    return render(request,'404-error.html',{"message":message} )
                    # return '两次密码不一致'

                def filter_fn(item):
                    return request.POST.get('email') == item.email  # 检测email是否已存在

                users = Admin.objects.all()
                filter_list = list(filter(filter_fn, users))  # filter()过滤函数序列 第一个参数是函数 第二个是序列
                if len(filter_list):  # 如果长度不为0，说明在数据库里找到了，说明已存在
                    message = 'User already registered'
                    return render(request,'404-error.html', {"message":message})
                else:
                    Admin.objects.create(email=request.POST.get('email'), password=request.POST.get('password'))
                    return redirect('/login/')

def admin_list(request):
    tableData=Book.objects.all()
    email = request.session['email']
    return render(request,'admin_list.html',{"tableData":tableData,"email":email})

# 管理员描述
@csrf_exempt
def admin_brief(request,nid):
    """管理员描述"""
    if request.method == "GET":
        data_list = Book.objects.filter(id=nid).first()
        return render(request, "admin_brief.html", {"data_list": data_list})
    else:
        # 获取管理员提交的描述
        brief = request.POST.get("brief")
        # 根据ID找到数据库中的数据并进行更新
        # Book.objects.filter(id=nid).update(title=title,其他字段=123)
        Book.objects.filter(id=nid).update(brief=brief)
        # 重定向回书列表
        return redirect("/admin/list/")
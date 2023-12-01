from django.db import models

# Create your models here.

class Admin(models.Model):
    """管理员"""
    email = models.CharField(verbose_name="邮箱", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

    def __str__(self):
        return self.username  # 解决前端页面显示成xx.object问题

class User(models.Model):
    """用户"""
    email = models.CharField(verbose_name="邮箱", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

    def __str__(self):
        return self.username  # 解决前端页面显示成xx.object问题

class Book(models.Model):
    """图书"""
    title = models.CharField(verbose_name="书名", max_length=32)
    author = models.CharField(verbose_name="作者", max_length=64)
    type = models.CharField(verbose_name="类型", max_length=64)
    genre = models.CharField(verbose_name="主题", max_length=64)
    brief = models.TextField(verbose_name="简介",blank=True)
    comment = models.TextField(verbose_name="评论",blank=True)

    def __str__(self):
        return self.username  # 解决前端页面显示成xx.object问题
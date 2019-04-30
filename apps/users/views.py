from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth import authenticate,login

from apps.users.models import UserProfile


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 不希望用户存在两个，get只能有一个。两个是get失败的一种原因 Q为使用并集查询
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))

            # django的后台中密码加密：所以不能password==password
            # UserProfile继承的AbstractUser中有def check_password(self, raw_password):
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def user_login(request):
    if request.method == 'POST':
        #request获取前端用户提交的用户名和密码
        user_name = request.POST.get('username', None)
        pass_word = request.POST.get('password', None)

        # 成功则返回user对象,失败返回None
        user = authenticate(user_name,pass_word)
        # 如果不是null说明验证成功
        if user is not None:
            #登录
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html',{'msg':'用户名或密码错误'})
    elif request.method == 'GET':
        return render(request, 'login.html')
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from XtqProject.settings import MEDIA_KEY_PREFIX


def mine(request):
    user_id = request.session.get('user_id')
    data = {
        "is_login":False
    }
    if user_id:
        user = User.objects.get(pk=user_id)
        data["is_login"] = True
        data["username"] = user.username
        data["last_name"] =  MEDIA_KEY_PREFIX+user.last_name.name

    return render(request, 'mine.html', data)

#  注册
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        # icon = request.FILES.get("icon")
        if not all([username]):
            message = '用户名不能为空'
            return render(request, 'register.html', locals())
        name_1 = User.objects.filter(username=username)
        if name_1:  # 用户名唯一
            message = '用户名存在'
            return render(request, 'register.html', locals())
        if not all([email]):
            message = '邮箱不能为空'
            return render(request, 'register.html', locals())
        email_1 = User.objects.filter(email=email)
        if email_1:
            message = '邮箱存在'
            return render(request, 'register.html', locals())
        if not all([password]):
            message = '密码不能为空'
            return render(request, 'register.html', locals())
        User.objects.create_user(username, email, password)
        return render(request, 'login.html')




#  登录
def login(request):
    if request.method == "GET":
        # error_message =request.session.get("error_message")
        # if error_message:
        #     del request.session["error_message"]
        return render(request, 'login.html')
    elif request.method =="POST":
        errors = {'msg':''}
        username = request.POST.get("username")
        password = request.POST.get("password")
        valid_code =request.POST.get("valid_code") #填写验证码
        queryset = User.objects.filter(username=username)
        if not queryset.exists():
            errors['msg'] = '%s 用户不存在，请先注册!' % username
        else:
            user = queryset.first()
            print(user.id,"*****3*****")
            # 验证口令
            if check_password(password, user.password):
                # 将登录后的信息存入到session中
                # request.session['login_user'] = {
                #     'id': user.id,
                #     'username': user.username,
                # }
                request.session["user_id"] = user.id
                return redirect(reverse('myapp:mine'))
            else:
                errors['msg'] = '登录口令不正确！'
    return render(request, 'login.html', locals())

def louout(request):
    request.session.flush()
    return redirect(reverse("myapp:mine"))

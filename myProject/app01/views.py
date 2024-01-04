import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import UserInfo
from .utils.token import create_token
# Create your views here.

@csrf_exempt
def login_view(request):
    data = json.loads(request.body)
    userName = data['username']
    password = data['password']
    if userName and password:
        user = UserInfo.objects.values().filter(user_name=userName, user_pwd=password)
        if user.count() >= 1:
            print(str(user))
            user = list(user)
            token = create_token(userName)
            return JsonResponse({'code': 0, 'message': '登录成功！', 'user': user, 'token': token, 'username': userName})
        else:
            return JsonResponse({'code': 1, 'message': '账号密码不匹配！'})
    else:
        return JsonResponse({'code': 1, 'message': '请重新输入用户名和密码！'})

@csrf_exempt
def register_view(request):
    data = json.loads(request.body)
    userName = data['username']
    password = data['password']
    print('request.body:' + str(request.body))
    if userName and password:
        result_Count = UserInfo.objects.filter(user_name=userName).count()
        if result_Count == 0:
            user = UserInfo(user_name=userName, user_pwd=password)
            user.save()
            return JsonResponse({'code': 0, 'message': '注册成功！'})
        else:
            return JsonResponse({'code': 1, 'message': '用户名已注册！'})
    else:
        return JsonResponse({'code': 1, 'message': '请重新输入用户名和密码！'})

# @csrf_exempt
# def population_bar_options_view(request):
#     print(json.loads(population_bar().population_bar_echarts()))
#     return JsonResponse({**{'code': 0, 'message': '成功！'},**json.loads(population_bar().population_bar_options)})
# @csrf_exempt
# def population_bar_options_view(request):
#     print(json.loads(chart_options))
#     return JsonResponse({**{'code': 0, 'message': '成功！'},**json.loads(chart_options)})



# @csrf_exempt
# def hebei_view(request):
#     return JsonResponse({'code': 0, 'message': '成功！', 'chart_options': chart_options})
# @csrf_exempt
# def henan_view(request):
#     return JsonResponse({'code': 0, 'message': '成功！', 'chart_options': chart_options})
# @csrf_exempt
# def shandong_view(request):
#     return JsonResponse({'code': 0, 'message': '成功！', 'chart_options': chart_options})
# @csrf_exempt
# def shanxi_view(request):
#     return JsonResponse({'code': 0, 'message': '成功！', 'chart_options': chart_options})

@csrf_exempt
def chgpwd_view(request):
    data = json.loads(request.body)
    userName = data['username']
    oldPassword = data['oldpassword']
    password = data['password']
    if userName and password:
        user = UserInfo.objects.get(user_name=userName, user_pwd=oldPassword)
        if user:
            print(user)
            user.user_pwd=password
            user.save()
            return JsonResponse({'code': 0, 'message': '修改密码成功，请重新登录！' })
        else:
            return JsonResponse({'code': 1, 'message': '账号与原密码不匹配，无法修改密码！'})
    else:
        return JsonResponse({'code': 1, 'message': '请重新输入用户名和密码！'})

@csrf_exempt
def destroy_view(request):
    data = json.loads(request.body)
    userName = data['username']
    password = data['password']
    if userName and password:
        user = UserInfo.objects.get(user_name=userName, user_pwd=password)
        if user:
            print(str(user))
            user.delete()
            return JsonResponse({'code': 0, 'message': '注销成功！' })
        else:
            return JsonResponse({'code': 1, 'message': '账号与密码不匹配，无法注销！'})
    else:
        return JsonResponse({'code': 1, 'message': '请重新输入用户名和密码！'})
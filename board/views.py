from django.http import JsonResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
from django.middleware.csrf import get_token


def index(request):
    return HttpResponse("welcomeeeeee")


def user_list(request):
    return render(request, "user_list.html")

def user_add(request):
    return HttpResponse("add a user")

def tpl(request):
    name = "wudi"
    roles = ["111", "222", "333"]
    man ={"name": "zhagn yi min", "age": 30, "company": "bytedance"}
    return render(request, 'tpl.html', {"n1": name, "n2": roles, "n3": man})

def news(request):
    import requests
    res = requests.get("http://neunews.neu.edu.cn/xwzh/list2.htm")
    data_list = res.json()
    print(data_list)
    return render(request, 'news.html', {"data_list": data_list})

def login(request):
    print(request.POST)
    return JsonResponse({'code': 20000, 'token': 'admin-token'})
    # return HttpResponse("test")

def get_csrf_token(request):
    token = get_token(request)
    print(token)
    return JsonResponse({'Xtoken': token, 'code': 20000})
    # return HttpResponse("test")

def login_test(request):
    if request.method == "GET":
        return render(request, "login.html")
    print(request.POST)
    return JsonResponse({'code': 20000})

def getInfo(request):
    admin_token = {
        'roles': 'admin',
        'introduction': 'I am a super administrator',
        'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
        'name': 'Super Admin'
    }
    return JsonResponse({'code': 20000, 'info': admin_token})

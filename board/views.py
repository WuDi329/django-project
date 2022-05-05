import json
from decimal import Decimal
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.utils import timezone
from django.db.models import Avg
from MyEncoder import MyEncoder
from board.models import Bintime
import re
import os


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

def ls(request):
    instruction = 'ls'
    f = os.popen(instruction)
    msg = f.readlines()
    return JsonResponse({'code': 20000, 'msg':msg})

def addtime(request):
    instruction = '/usr/bin/time -v -o time.txt'
    # preprocessing
    pname = request.GET.get('processname').replace("'", "")
    params = request.GET.get('params').replace("'", "")
    instruction = instruction + ' ' + pname + ' ' + params
    os.system(instruction)
    print(os.getcwd())
    with open('time.txt', 'r') as f:
        data = f.readlines()
    print(data)
    # print(Decimal(re.findall(r'\d+.\d+$', data[4])[0]))
    # print(Decimal(re.findall(r'\d+.\d+$', data[1])[0]))
    # print(Decimal(re.findall(r'\d+.\d+$', data[2])[0]))
    # print(int(re.findall(r'\d+', data[3])[0]))
    # print(Decimal(re.findall(r'\d+.\d+$', data[4])[0]))
    # print(int(re.findall(r'\d+$', data[9])[0]))
    create_time = timezone.now()
    # print(re.findall(r'\w+$', '/home/wudi/1234/memtier_benchmark'))
    b = Bintime(elf_name=re.findall(r'\w+$', pname)[0], run_time=create_time,
                user_time=Decimal(re.findall(r'\d+.\d+$', data[1])[0]),
                sys_time=Decimal(re.findall(r'\d+.\d+$', data[2])[0]),
                cpu_per=int(re.findall(r'\d+', data[3])[0]),
                elapse_time=Decimal(re.findall(r'\d+.\d+$', data[4])[0]),
                max_size=int(re.findall(r'\d+$', data[9])[0]),
                page_fault=int(re.findall(r'\d+$', data[11])[0]),
                mpage_fault=int(re.findall(r'\d+$', data[12])[0]))
    b.save()
    return JsonResponse({'code': 20000})

def gettime(request):
    pname = request.GET.get('processname').replace("'", "")
    elf_name = re.findall(r'\w+$', pname)[0]
    print(elf_name)
    data = Bintime.objects.filter(elf_name=elf_name)
    print(data)
    return HttpResponse(json.dumps({
        'code': 20000,
        'data': serializers.serialize("json", data)
    }))

def getalltime(request):
    data = list(Bintime.objects.values('id', 'elf_name', 'run_time', 'user_time', 'sys_time', 'cpu_per', 'elapse_time',
                                       'max_size', 'page_fault', 'mpage_fault'))
    # data = serializers.serialize("json", data)
    print(data)
    return JsonResponse({'code': 20000, 'data': data})
    #return JsonResponse({"code": 20000, "data": json.dumps(data, cls=MyEncoder, indent=4)})
    # return JsonResponse({'code': 20000, 'data': data})


def avgtime(request):
    pname = request.GET.get('processname').replace("'", "")
    elf_name = re.findall(r'\w+$', pname)[0]
    print(elf_name)
    data = Bintime.objects.filter(elf_name='memtier_benchmark').aggregate(
        Avg('user_time'), Avg('sys_time'), Avg('cpu_per'), Avg('elapse_time'),
        Avg('max_size'), Avg('page_fault'), Avg('mpage_fault'))
    print(data)
    return JsonResponse({'code': 20000, 'data': data, 'elf_name': elf_name})
import json
from decimal import Decimal
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.utils import timezone
from django.db.models import Avg
from MyEncoder import MyEncoder
from board.models import Bintime
from board.models import Elfinfo
from board.models import Perfmess
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
    create_time = timezone.now()
    b = Bintime(elf_name=re.findall(r'\w+$', pname)[0], params=params,
                run_time=create_time,
                user_time=Decimal(re.findall(r'\d+.\d+$', data[1])[0]),
                sys_time=Decimal(re.findall(r'\d+.\d+$', data[2])[0]),
                cpu_per=int(re.findall(r'\d+', data[3])[0]),
                elapse_time=Decimal(re.findall(r'\d+.\d+$', data[4])[0]),
                max_size=int(re.findall(r'\d+$', data[9])[0]),
                page_fault=int(re.findall(r'\d+$', data[11])[0]),
                mpage_fault=int(re.findall(r'\d+$', data[12])[0]))
    b.save()
    return JsonResponse({'code': 20000, 'msg': 'add successfully'})

def gettime(request):
    pname = request.GET.get('processname').replace("'", "")
    params = request.GET.get('params').replace("'", "")
    elf_name = re.findall(r'\w+$', pname)[0]
    print(elf_name)
    data = list(Bintime.objects.values('id', 'elf_name', 'run_time', 'user_time', 'sys_time', 'cpu_per', 'elapse_time',
                                       'max_size', 'page_fault', 'mpage_fault').filter(elf_name=elf_name, params=params))
    print(data)
    return JsonResponse({'code': 20000, 'data': data})

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
    params = request.GET.get('params').replace("'", "")
    elf_name = re.findall(r'\w+$', pname)[0]
    print(elf_name)
    elf_name_static = elf_name + '_static'
    print(elf_name_static)
    data = Bintime.objects.filter(elf_name=elf_name, params=params).aggregate(
        Avg('user_time'), Avg('sys_time'), Avg('cpu_per'), Avg('elapse_time'),
        Avg('max_size'), Avg('page_fault'), Avg('mpage_fault'))
    data_static = Bintime.objects.filter(elf_name=elf_name_static, params=params).aggregate(
        Avg('user_time'), Avg('sys_time'), Avg('cpu_per'), Avg('elapse_time'),
        Avg('max_size'), Avg('page_fault'), Avg('mpage_fault'))
    data = [data, data_static]
    print(data)
    return JsonResponse({'code': 20000, 'data': data, 'elf_name': elf_name, })

def addsize(request):
    instruction = 'size'
    # preprocessing
    pname = request.GET.get('processname').replace("'", "")
    elf_name = re.findall(r'\w+$', pname)[0]
    instruction = instruction + ' ' + pname + ' > size.txt '
    os.system(instruction)
    print(os.getcwd())
    with open('size.txt', 'r') as f:
        data = f.readlines()
    print(Decimal((re.findall(r'\d+', data[1]))[3]))
    s = Elfinfo(elf_name=elf_name, text_length=Decimal((re.findall(r'\d+.', data[1]))[0]),
                data_length=Decimal((re.findall(r'\d+', data[1]))[1]),
                bss_length=Decimal((re.findall(r'\d+', data[1]))[2]),
                dec_length=Decimal((re.findall(r'\d+', data[1]))[3]))
    s.save()
    return JsonResponse({'code': 20000, 'msg': 'add successfully'})

def getallsize(request):
    data = list(Elfinfo.objects.distinct().values('elf_name', 'text_length', 'data_length', 'bss_length', 'dec_length'))
    # data = serializers.serialize("json", data)
    print(data)
    return JsonResponse({'code': 20000, 'data': data})

def getAvgsize(request):
    pname = request.GET.get('processname').replace("'", "")
    elf_name = re.findall(r'\w+$', pname)[0]
    print(elf_name)
    elf_name_static = elf_name + '_static'
    print(elf_name_static)
    data = Elfinfo.objects.filter(elf_name=elf_name).values(
         'text_length', 'data_length', 'bss_length', 'dec_length').first()
    data_static = Elfinfo.objects.filter(elf_name=elf_name_static).values(
         'text_length', 'data_length', 'bss_length', 'dec_length').first()
    data = [data, data_static]
    print(data)
    return JsonResponse({'code': 20000, 'data': data, 'elf_name': elf_name, })

def getsize(request):
    pname = request.GET.get('processname').replace("'", "")
    elf_name = re.findall(r'\w+$', pname)[0]
    print(elf_name)
    data = Elfinfo.objects.filter(elf_name=elf_name).values('elf_name', 'text_length', 'data_length', 'bss_length', 'dec_length').first()
    data = [data]
    print(data)
    return JsonResponse({'code': 20000, 'data': data})

def addperf(request):
    instruction = 'perf stat -o perf.txt -e task-clock,instructions,branches,' \
                  'branch-misses,L1-dcache-loads,L1-dcache-load-misses,' \
                  'LLC-loads,LLC-load-misses,L1-icache-load-misses,' \
                  'dTLB-loads,dTLB-load-misses,iTLB-load-misses'
    # preprocessing
    pname = request.GET.get('processname').replace("'", "")
    params = request.GET.get('params').replace("'", "")
    elf_name = re.findall(r'\w+$', pname)[0]
    instruction = instruction + ' ' + pname + ' ' + params
    os.system(instruction)
    print(os.getcwd())
    with open('perf.txt', 'r') as f:
        data = f.readlines()
    # print(data)
    create_time = timezone.now()
    with open('perf-new.txt', 'w') as f:
        for line in data:
            new_line = line.replace(",", "")
            f.write(new_line)

    with open('perf-new.txt', 'r') as f:
        data = f.readlines()
    print(data)
    # print(Decimal((re.findall(r'(\d+,)\d+', data[6]))[0]))
    s = Perfmess(elf_name=elf_name, params=params, run_time=create_time,
                 cpu_utilize=Decimal((re.findall(r'\d+.\d+(?= CPUs)', data[5]))[0]),
                instructions=Decimal((re.findall(r'\d+', data[6]))[0]),
                branches=Decimal((re.findall(r'\d+', data[7]))[0]),
                branches_misses=Decimal((re.findall(r'\d+', data[8]))[0]),
                 l1_dcache=Decimal((re.findall(r'\d+', data[9]))[0]),
                l1_dcache_misses=Decimal((re.findall(r'\d+', data[10]))[0]),
                 llc_cache=Decimal((re.findall(r'\d+', data[11]))[0]),
                 llc_cache_misses=Decimal((re.findall(r'\d+', data[12]))[0]),
                 l1_icache_misses=Decimal((re.findall(r'\d+', data[13]))[0]),
                 dtlb_cache=Decimal((re.findall(r'\d+', data[14]))[0]),
                 dtlb_cache_misses=Decimal((re.findall(r'\d+', data[15]))[0]),
                 itlb_cache_misses=Decimal((re.findall(r'\d+', data[16]))[0]))
    s.save()
    return JsonResponse({'code': 20000, 'msg': 'add successfully'})

def getperf(request):
    pname = request.GET.get('processname').replace("'", "")
    params = request.GET.get('params').replace("'", "")
    elf_name = re.findall(r'\w+$', pname)[0]
    print(elf_name)

    data = list(Perfmess.objects.filter(elf_name=elf_name, params=params).values('id', 'elf_name', 'params', 'run_time',
                                                                           'instructions', 'branches', 'branches_misses',
                                                                                 'cpu_utilize',
                                                                           'l1_dcache', 'l1_dcache_misses',
                                                                           'llc_cache', 'llc_cache_misses',
                                                                           'l1_icache_misses', 'dtlb_cache',
                                                                           'dtlb_cache_misses', 'itlb_cache_misses'))
    print(data)
    return JsonResponse({'code': 20000, 'data': data})

def getallperf(request):
    data = list(Perfmess.objects.distinct().values('id', 'elf_name', 'params', 'run_time',
                                                    'instructions', 'branches', 'branches_misses',
                                                    'cpu_utilize',
                                                    'l1_dcache', 'l1_dcache_misses',
                                                    'llc_cache', 'llc_cache_misses',
                                                    'l1_icache_misses', 'dtlb_cache',
                                                    'dtlb_cache_misses', 'itlb_cache_misses'))
    print(data)
    return JsonResponse({'code': 20000, 'data': data})

def getAvgperf(request):
    pname = request.GET.get('processname').replace("'", "")
    params = request.GET.get('params').replace("'", "")
    elf_name = re.findall(r'\w+$', pname)[0]
    print(elf_name)
    elf_name_static = elf_name + '_static'
    print(elf_name_static)

    data = Perfmess.objects.filter(elf_name=elf_name, params=params).aggregate(
         Avg('instructions'), Avg('branches'), Avg('branches_misses'),
         Avg('l1_dcache'),
         Avg('l1_dcache_misses'), Avg('llc_cache'), Avg('llc_cache_misses'),
         Avg('l1_icache_misses'), Avg('dtlb_cache'), Avg('dtlb_cache_misses'), Avg('itlb_cache_misses'))
    data_static = Perfmess.objects.filter(elf_name=elf_name_static, params=params).aggregate(
         Avg('instructions'), Avg('branches'), Avg('branches_misses'), Avg('l1_dcache'),
         Avg('l1_dcache_misses'), Avg('llc_cache'), Avg('llc_cache_misses'),
         Avg('l1_icache_misses'), Avg('dtlb_cache'), Avg('dtlb_cache_misses'),
         Avg('itlb_cache_misses'))
    data = [data, data_static]
    print(data)
    return JsonResponse({'code': 20000, 'data': data, 'elf_name': elf_name})
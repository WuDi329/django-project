from django.http import JsonResponse
from another.models import Straceinfo
import os
import re

from django.shortcuts import render, HttpResponse


def addstrace(request):
    if os.path.exists('./strace.txt'):
        os.remove('./strace.txt')
    pname = request.GET.get('processname').replace("'", "")
    params = request.GET.get('params').replace("'", "")
    elf_name = re.findall(r'\w+$', pname)[0]

    instruction = 'strace -c -v -o ./strace.txt ' + pname + ' ' + params + '  >/dev/null 2>&1  &  '
    instruction2 = '/home/wudi/Desktop/htstress/htstress  -n 10000 -c 100 -t 8 localhost:7000 >/dev/null 2>&1'
    os.system(instruction)
    os.system('sleep 0.5s')
    os.system(instruction2)
    os.system('sleep 2s')
    with open('strace.txt', 'r') as f:
        data = f.readlines()
    print(data)
    if len(data) == 0:
        return JsonResponse({'code': 20000, 'msg': 'some errors'})
    print(re.findall(r' \d+ ', data[2])[0])
    e = Straceinfo.objects.create(
        elf_name=elf_name,
        params='7000',
        msg=[
            {'name': re.findall(r'[a-zA-Z]+', data[2])[0], 'per_time': re.findall(r' \d+ ', data[2])[0],
             'call_times': re.findall(r' \d+ ', data[2])[1], 'percent': re.findall(r'\d+.\d+', data[2])[0]},
            {'name': re.findall(r'[a-zA-Z]+', data[3])[0], 'per_time': re.findall(r' \d+ ', data[3])[0],
             'call_times': re.findall(r' \d+ ', data[3])[1], 'percent': re.findall(r'\d+.\d+', data[3])[0]},
            {'name': re.findall(r'[a-zA-Z]+', data[4])[0], 'per_time': re.findall(r' \d+ ', data[4])[0],
             'call_times': re.findall(r' \d+ ', data[4])[1], 'percent': re.findall(r'\d+.\d+', data[4])[0]},
            {'name': re.findall(r'[a-zA-Z]+', data[5])[0], 'per_time': re.findall(r' \d+ ', data[5])[0],
             'call_times': re.findall(r' \d+ ', data[5])[1], 'percent': re.findall(r'\d+.\d+', data[5])[0]},
            {'name': re.findall(r'[a-zA-Z]+', data[6])[0], 'per_time': re.findall(r' \d+ ', data[6])[0],
             'call_times': re.findall(r' \d+ ', data[6])[1], 'percent': re.findall(r'\d+.\d+', data[6])[0]},
        ]
    )
    e.save(using='strace')
    return JsonResponse({'code': 20000, 'msg': 'add successfully'})

def getstrace(request):
    pname = request.GET.get('processname').replace("'", "")
    params = request.GET.get('params').replace("'", "")
    elf_name = re.findall(r'\w+$', pname)[0]
    print(elf_name)
    data = list(Straceinfo.objects.filter(elf_name=elf_name, params=params).values())
    print(data)
    return JsonResponse({'code': 20000, 'data': data})

def getavgstrace(request):
    pname = request.GET.get('processname').replace("'", "")
    params = request.GET.get('params').replace("'", "")
    elf_name = re.findall(r'\w+$', pname)[0]
    print(elf_name)
    elf_name_static = elf_name + '_static'
    print(elf_name_static)
    data = Straceinfo.objects.filter(elf_name=elf_name, params=params).values().last()
    data_static = Straceinfo.objects.filter(elf_name=elf_name_static, params=params).values().last()
    data= [data, data_static]
    print(data)
    return JsonResponse({'code': 20000, 'data': data, 'elf_name': elf_name,})


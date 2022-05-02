from django.shortcuts import render, HttpResponse

# Create your views here.

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
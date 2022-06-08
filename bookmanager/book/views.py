from django.shortcuts import render

# Create your views here.
"""
shitu
suowei de shitu jiushi python hanshu
shitu hanshu you liangge yaoqiu 
    1.shitu hanshu de diyige canshu jiushi jieshou qingqiu
"""
from django.http import HttpRequest
from django.http import HttpResponse


# women qiwang yonghu shuru http://127.0.0.1:8000/index/
def index(request):

    return HttpResponse('ok')

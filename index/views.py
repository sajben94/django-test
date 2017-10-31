from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    my_dict = {'insert_me':'Now I am comming from index/hello hahaha'}
    return render(request, 'index/hello.html',context=my_dict)
# Create your views here.

def help(request):
    my_dict = {'help_me':'This is help page!'}
    return render(request,'index/help.html',context=my_dict)

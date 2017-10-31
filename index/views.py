from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    my_dict = {'insert_me':'Now I am comming from index/hello'}
    return render(request, 'hello.html',context=my_dict)
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from index.models import Topic,Webpage,AccessRecord,Users

def hello(request):
    webpage = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpage}
    my_dict = {'insert_me':'Now I am comming from index/hello hahaha'}
    return render(request, 'index/hello.html',context=date_dict)
# Create your views here.

def help(request):
    my_dict = {'help_me':'This is help page!'}
    return render(request,'index/help.html',context=my_dict)

def users(request):
    users_list = Users.objects.order_by('first_name')
    user_dict = {'users_list':users_list}
    return render(request,'index/users.html',context=user_dict)

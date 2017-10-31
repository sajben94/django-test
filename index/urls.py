from django.conf.urls import url
from index import views

urlpatterns = [
    url(r'^$',views.hello,name="hello"),
    url(r'^help/',views.help,name="help")
]

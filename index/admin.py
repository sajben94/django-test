from django.contrib import admin
from index.models import AccessRecord,Topic,Webpage,Users

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Users)
# Register your models here.

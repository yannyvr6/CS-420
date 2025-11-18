from django.contrib import admin
from .models import WebUser, AddressType, Address, PhoneType, Phone, UserInfo, Page
       
# Register your models here.
admin.site.register(WebUser)
admin.site.register(AddressType)
admin.site.register(Address)
admin.site.register(PhoneType)
admin.site.register(Phone)
admin.site.register(UserInfo)
admin.site.register(Page)
from django.db import models

# Create your models here.
from django.db import models

class WebUser(models.Model):
    web_user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'web_users'

class AddressType(models.Model):
    address_type_id = models.AutoField(primary_key=True)
    address_type = models.CharField(max_length=255)

    class Meta:
        db_table = 'address_types'

class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    web_user = models.ForeignKey(WebUser, on_delete=models.CASCADE)
    address_type = models.ForeignKey(AddressType, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)

    class Meta:
        db_table = 'addresses'

class PhoneType(models.Model):
    phone_type_id = models.AutoField(primary_key=True)
    phone_type = models.CharField(max_length=255)

    class Meta:
        db_table = 'phone_types'

class Phone(models.Model):
    phone_id = models.AutoField(primary_key=True)
    web_user = models.ForeignKey(WebUser, on_delete=models.CASCADE)
    phone_type = models.ForeignKey(PhoneType, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)

    class Meta:
        db_table = 'phones'

class UserInfo(models.Model):
    user_info_id = models.AutoField(primary_key=True)
    web_user = models.ForeignKey(WebUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture_url = models.URLField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'user_infos'

class Page(models.Model):
    page_id = models.AutoField(primary_key=True)
    page_name = models.CharField(max_length=255)
    page_content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'pages'
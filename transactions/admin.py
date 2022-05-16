from django.contrib import admin
from .models import Company, Transaction
# Register your models here.
admin.site.register(Transaction)
admin.site.register(Company)
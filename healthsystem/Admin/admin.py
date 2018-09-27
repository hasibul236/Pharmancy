from django.contrib import admin
from .models import *

class CustomerAdmin(admin.ModelAdmin):
	list_display = ('name','guardian','doctor_refer','mobile','age','created_at')

class SupplierAdmin(admin.ModelAdmin):
	list_display = ('name','mobile','email','company','medicine_name')

class MedicineAdmin(admin.ModelAdmin):
	list_display = ('name','cost','quantity','company')

class DoctorAdmin(admin.ModelAdmin):
	list_display = ('name','designation','consultant','mobile','email','address')


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Supplier,SupplierAdmin)
admin.site.register(Medicine,MedicineAdmin)
admin.site.register(Doctor,DoctorAdmin)
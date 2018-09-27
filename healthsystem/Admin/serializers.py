from rest_framework import serializers
from Admin.models import * 
import collections

class CustomerSerializer(serializers.ModelSerializer):
		class Meta:
			model = Customer
			fields = ('name','guardian','doctor_refer','email','mobile','age','address','created_at')

class SupplierSerializer(serializers.ModelSerializer):
		class Meta:
			model = Supplier
			fields = ('name','mobile','email','company','company_address','supply_date','supplier_address','medicine_name')

class MedicineSerializer(serializers.ModelSerializer):
		class Meta:
			model = Medicine
			fields = ('name','cost','quantity','company','supply_date','expiry_date')

class DoctorSerializer(serializers.ModelSerializer):
		class Meta:
			model = Doctor
			fields = ('name','designation','consultant','mobile','email','address')
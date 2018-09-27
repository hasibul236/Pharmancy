from django.shortcuts import render
from Admin.models import *
from django.http import HttpResponse,Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from Admin.serializers import *
from rest_framework import status

class CustomerViewSet(APIView):
	def get(self,request,format=None):
		customers = Customer.objects.all()
		serializer= CustomerSerializer(customers,many=True)
		return Response(serializer.data)


class SupplierViewSet(APIView):
	def get(self,request,format=None):
		suppliers = Supplier.objects.all()
		serializer= SupplierSerializer(suppliers,many=True)
		return Response(serializer.data)


class MedicineViewSet(APIView):
	def get(self,request,format=None):
		Medicines = Medicine.objects.all()
		serializer= MedicineSerializer(Medicines,many=True)
		return Response(serializer.data)

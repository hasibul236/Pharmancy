from django.db import models

class Customer(models.Model):
	name = models.CharField(max_length=512)
	guardian =models.CharField(max_length=512)
	doctor_refer=models.CharField(max_length=512,null=True,blank=True)
	email = models.CharField(max_length=512,null=True,blank=True)
	mobile =models.BigIntegerField()
	age =models.IntegerField()
	address = models.TextField()
	created_at =models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	doctor_refer.verbose_name='Doctor Reffer'

class Medicine(models.Model):
	MEDICINETYPE=(('Tablet','Tablet'),('Syrup','Syrup'),('Injection','Injection'),('Shampoo','Shampoo'),('Capsule','Capsule'),('Not Define','Not Define'))
	name = models.CharField(max_length=512)
	cost = models.DecimalField(max_digits=8, decimal_places=2)
	quantity = models.IntegerField()
	type=models.CharField(choices=MEDICINETYPE,max_length=25,default='Not Define')
	generic=models.CharField(max_length=512,null=True,blank=True)
	batch_no=models.CharField(max_length=512,null=True,blank=True)
	company = models.CharField(max_length=512)
	supply_date =models.DateField()
	expiry_date =models.DateField(blank=True,null=True)
	modified_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	supply_date.verbose_name='Supply Date'
	expiry_date.verbose_name='Expiry Date'
	batch_no.verbose_name='Batch No'


class Supplier(models.Model):
	name =models.CharField(max_length=512)
	mobile =models.BigIntegerField()
	email = models.CharField(max_length=512,null=True,blank=True)
	company =models.CharField(max_length=512)
	company_address=models.TextField(blank=True,null=True)
	supply_date =models.DateField()
	supplier_address= models.TextField(null=True,blank=True)
	medicine_name=models.ForeignKey(Medicine,related_name='suppliers',on_delete= models.CASCADE)
	created_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	company_address.verbose_name='Company Address'
	supply_date.verbose_name='Supply Date'
	supplier_address.verbose_name='Supplier Address'
	medicine_name.verbose_name='Medicine Name'

class Doctor(models.Model):
	DOCTORTYPES= (('Aesthetic and Reconstructive Surgery','Aesthetic and Reconstructive Surgery'),('Cardiology','Cardiology'),('Nephrology','Nephrology'),('Urology','Urology'),('ENT','ENT'),('Internal Medicine','Internal Medicine'),('Cardiac Surgery','Cardiac Surgery'),('Bariatric Surgery','Bariatric Surgery'),('Orthopaedics','Orthopaedics'),('Neurology','Neurology'),('Neurosurgery','Neurosurgery'),('Surgical Gastroenterology','Surgical Gastroenterology'),('Liver Transplantation','Liver Transplantation'),('Infectious Disease','Infectious Disease'),('Pain Management','Pain Management'),('Breast Surgery','Breast Surgery'),('Dental Surgery','Dental Surgery'),('Dermatology','Dermatology'),('Diabetology','Diabetology'),('Dietary','Dietary'),('Endocrinology','Endocrinology'),('Gastroenterology','Gastroenterology'),('General Surgery','General Surgery'),('Geriatric Medicine','Geriatric Medicine'),('Haematology','Haematology'),('Hepatology','Hepatology'),('Interventional Radiology','Interventional Radiology'),('Podiatry','Podiatry'),('Psychiatry','Psychiatry'),('Pulmonology','Pulmonology'),('Rheumatology','Rheumatology'),('Vascular Surgery','Vascular Surgery'),('Medical Oncology','Medical Oncology'),('Pediatric Immunology','Pediatric Immunology'),('Ophthalmology','Ophthalmology'),('Pediatric Endocrinology','Pediatric Endocrinology'),('Psychology','Psychology'),('Obstetrics and Gynaecology','Obstetrics and Gynaecology'),('Cardiology Electrophysiology ','Cardiology Electrophysiology '),('Surgical Oncology ','Surgical Oncology '),('Robotic Surgery','Robotic Surgery'))
	name = models.CharField(max_length=512)
	picture = models.FileField(upload_to='doctor_images',blank=True,null=True)
	designation = models.CharField(max_length=512)
	consultant = models.CharField(choices=DOCTORTYPES,max_length=100)
	mobile = models.BigIntegerField()
	email = models.CharField(max_length=512,blank=True,null=True)
	address = models.TextField()





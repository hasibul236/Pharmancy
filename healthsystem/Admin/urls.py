from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^customer/$',views.CustomerViewSet.as_view(),name='customer'),
	url(r'^supplier/$',views.SupplierViewSet.as_view(),name='supplier'),
	url(r'^medicine/$',views.MedicineViewSet.as_view(),name='medicine'),
]
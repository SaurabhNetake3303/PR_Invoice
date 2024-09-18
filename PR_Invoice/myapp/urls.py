from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.Payment_recommendation, name="Payment_recommendation"),
    # path('beneficiary_create', views.beneficiary_create, name='beneficiary_create'),
    path('get_beneficiary_details', views.get_beneficiary_details, name='get_beneficiary_details'),

    path('select_beneficiary', views.select_beneficiary, name='select_beneficiary'),
    path('pr_request_data', views.pr_request_data, name='pr_request_data'),
]

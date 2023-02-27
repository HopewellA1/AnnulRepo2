from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('addFederation', views.addFederation, name="addFederation"),
    path('updateFederation', views.updateFederation, name="updateFederation"),
    path('AnsDistricts/<int:numDone>', views.AnsDistricts, name="AnsDistricts"),
    path('updateDistrict/<int:districtId>', views.updateDistrict, name="updateDistrict"),
    path('FederationDetails/<int:federationId>',views.FederationDetails, name="FederationDetails"),
    path('ViewFederations', views.ViewFederations, name="ViewFederations")
    
   
   
]
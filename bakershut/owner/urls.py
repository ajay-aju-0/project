from accounts.views import loadHome
from django.urls import path
from .views import *

urlpatterns = [
   path('home/',ownerHome,name='owner_home'),
   path('addstaff/',addStaff,name='owner_addstaff'),
   path('managestaff/',staffList,name='owner_managestaff'),
   path('staffupdate/<id>',updateStaff,name='owner_updatestaff'),
   path('staffactivation/',changeStaffStatus,name='owner_staffstatus'),
   path('addproduct/',addProduct,name='owner_addproduct'),
   path('manageproduct/',productList,name='owner_manageproduct'),
   path('updateproduct/<id>',updateProduct,name='owner_updateproduct'),
   path('deactivateproduct/',changeProductStatus,name='owner_productstatus'),
   path('manageshop/',shopList,name='owner_manageshop'),
   path('deactivateshop/',changeShopStatus,name='owner_shopchangestatus'),
   path('managecustomer/',custList,name='owner_managecustomer'),
   path('deactivatecustomer/',changeCustStatus,name='owner_custchangestatus'),
   path('changepassword/',changePassword,name='owner_changepassword'),
   path('updateprofile/',updateProfile,name='owner_updateprofile'),
]

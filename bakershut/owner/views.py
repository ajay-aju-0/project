import json
from owner.models import Products, StaffDetails
from accounts.models import ShopDetails, UserLogin
from django.http.response import HttpResponse,JsonResponse
from owner.forms import ProductsForm, StaffForm
from accounts.forms import *
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

# ---------------- Home Page -------------------------------

@login_required()
def ownerHome(request):
    return render(request,'home.html')

# ----------------- Staff managing views ----------------------

@login_required()
def addStaff(request):
    context = {'form1':UserForm(initial={'usertype':'staff'}),'form2':StaffForm()}
    if request.method == 'GET':
        return render(request,'addstaff.html',context)
    elif request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = StaffForm(request.POST)
        pwd = request.POST['password']
        if form1.is_valid() and form2.is_valid():
            obj1 = form1.save(commit=False)
            obj2 = form2.save(commit=False)
            obj2.login = obj1
            obj1.set_password(pwd)
            obj1.save()
            obj2.save()
            return redirect('owner_managestaff')
        else:
            return render(request,'addstaff.html',{'form1':form1,'form2':form2})
    else:
        return render(request,'addstaff.html',context)

@login_required()
def staffList(request):
    list = StaffDetails.objects.all()
    context = {'staff':list}
    return render(request,'stafflist.html',context)

@login_required()
def changeStaffStatus(request):
    # list = UserLogin.objects.get(pk=id)
    # if list.is_active == 0:
    #     list.is_active = 1
    # else:
    #     list.is_active = 0
    # list.save()
    # return redirect('owner_managestaff')
    if request.method == 'POST' and request.is_ajax:
        id = request.POST.get('id')
        list = UserLogin.objects.get(pk=id)
        if list.is_active == 0:
            list.is_active = 1
        else:
            list.is_active = 0
        list.save()
        return JsonResponse({'success':1,'active':list.is_active})

@login_required()
def updateStaff(request, id):
    staff = StaffDetails.objects.get(pk=id)
    if request.method == 'GET':
        context = {}
        context['form'] = StaffForm(instance=staff)
        return render(request, 'updatestaff.html', context)
    elif request.method == 'POST':
        form = StaffForm(request.POST,instance=staff)
        if form.is_valid():
            form.save()
            return redirect('owner_managestaff')
        else:
            context = {}
            context['form'] = StaffForm(instance=staff)
            return render(request, 'updateseller.html', context)
    else:
        return redirect('owner_managestaff')


# ---------------------- Product managing views --------------------

@login_required()
def addProduct(request):
    context = {'form':ProductsForm()}
    if request.method == 'GET':
        return render(request,'addproduct.html',context)
    elif request.method == 'POST':
        form = ProductsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('owner_manageproduct')
        else:
            return render(request,'addproduct.html',{'form':form})
    else:
         return render(request,'addproduct.html',context)

@login_required()
def productList(request):
    list = Products.objects.all()
    context = {'product':list}
    return render(request,'productlist.html',context)

@login_required()
def changeProductStatus(request):
    # list = Products.objects.get(pk=id)
    # if list.status == 0 :
    #     list.status = 1
    # else:
    #     list.status = 0
    # list.save()
    # return redirect('owner_manageproduct')
    if request.method == 'POST' and request.is_ajax:
        id = request.POST.get('id')
        # print(id)
        list = Products.objects.get(pk=id)
        if list.status == 0:
            list.status = 1
        else:
            list.status = 0
        list.save()
        return JsonResponse({'success':1,'status':list.status})

@login_required()
def updateProduct(request, id):
    prod = Products.objects.get(pk=id)
    if request.method == 'GET':
        context = {}
        context['form'] = ProductsForm(instance=prod)
        return render(request, 'updateproduct.html', context)
    elif request.method == 'POST':
        form = ProductsForm(request.POST,instance=prod)
        if form.is_valid():
            form.save()
            return redirect('owner_manageproduct')
        else:
            context = {}
            context['form'] = ProductsForm(instance=prod)
            return render(request, 'updateproduct.html', context)
    else:
        return redirect('owner_manageproduct')

# -------------------------- Customer activation and deactivation -------------------

@login_required()
def changeCustStatus(request):
    # list = UserLogin.objects.get(pk=id)
    # if list.is_active == 0:
    #     list.is_active = 1
    # else:
    #     list.is_active = 0
    # list.save()
    # return redirect('owner_managecustomer')
    if request.method == 'POST' and request.is_ajax:
        id = request.POST.get('id')
        list = UserLogin.objects.get(pk=id)
        if list.is_active == 0:
            list.is_active = 1
        else:
            list.is_active = 0
        list.save()
        return JsonResponse({'success':1,'active':list.is_active})

# --------------------------- Shop activation and deactivation -----------------------

@login_required()
def changeShopStatus(request):
    # list = UserLogin.objects.get(pk=id)
    # if list.is_active == 0:
    #     list.is_active = 1
    # else:
    #     list.is_active = 0
    # list.save()
    # return redirect('owner_manageshop')
    if request.method == 'POST' and request.is_ajax:
        id = request.POST.get('id')
        # print(id)
        list = UserLogin.objects.get(pk=id)
        if list.is_active == 0:
            list.is_active = 1
        else:
            list.is_active = 0
        list.save()
        return JsonResponse({'success':1,'active':list.is_active})

# --------------------------- Shop List View ------------------------------

@login_required()
def shopList(request):
    list = ShopDetails.objects.all()
    context = {'shop':list}
    return render(request,'shoplist.html',context)

# --------------------------- Customer List View ---------------------------

@login_required()
def custList(request):
    list = UserLogin.objects.all()
    context = {'cust':list}
    return render(request,'customerlist.html',context)

# --------------------------- Change password view -------------------------

@login_required()
def changePassword(request):
    if request.method == 'GET':
        return render(request,'changepassword.html')
    if request.method == 'POST':
        new = request.POST['new']
        renew = request.POST['renew']
        if new==renew:
            request.user.set_password(new)
            request.user.save()
        else:
            messages.error(request,'passwords not matching,please re enter')
            return render(request,'changepassword.html')
        return redirect('login')

# ----------------------------- Update Profile View -------------------------

@login_required()
def updateProfile(request):
    context = {}
    context['form'] = UpdateForm(instance=request.user)
    if request.method == 'GET':
        return render(request,'updateprofile.html',context)
    elif request.method == 'POST':
        form = UpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"profile updated successfully")
            return redirect('owner_updateprofile')
        else:
            messages.error(request,"error while submitting")
            return render(request,'updateprofile.html',context)
    else:
        return redirect('owner_home')
    

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from user_auth.views import login_required
from django.core import serializers
from django.db.models import Q
# Create your views here.


@login_required
def main(request):
    try:
        current_user = request.session['user_id']
        query = ''
        try:
            query = request.GET['query']
        except Exception as e:
            print("No Serach Query\t:\t", e)
        if query:
            units_details_comment = unit_comment_details.objects.filter(Q(vehicle_no__icontains=query)).order_by('-id')
        else:
            units_details_comment = unit_comment_details.objects.all().order_by('-id')
        paginator = Paginator(units_details_comment, 10)
        page = request.GET.get('page')
        try:
            units_details_comment = paginator.page(page)
        except PageNotAnInteger:
            units_details_comment = paginator.page(1)
        except EmptyPage:
            units_details_comment = paginator.page(paginator.num_pages)
        context = {
            'units_details_comment': units_details_comment,
            'user_id': current_user,
            'query': query,
        }
        return render(request, 'dashboard/unit_address_comments.html', context)
    except Exception as e:
        messages.error(request, "There is an critical issue")
        print("exception \t:\t", e)

    return render(request, 'dashboard/main.html')


# CRUD for Unit Name

def delete_unitname(request):
    if request.method == "GET":
        data_id = request.GET['data-id']
        try:
            unit_details.objects.filter(id=data_id).delete()
        except Exception as e:
            print('unit Name  ',e)
        messages.success(request, "Unit Name Deleted Successfully")
        return JsonResponse(True, safe=False)
    return HttpResponse("test")


def update_unitname(request):
    if request.method == "GET":
        data_id = request.GET['data-id']
        unit_name = request.GET['unit_name']
        unit_details.objects.filter(id=data_id).update(unit_name=unit_name)
        messages.success(request, "Unit Name Updated Successfully")
        return JsonResponse(True, safe=False)
    return HttpResponse("test")


def create_unitname(request):
    try:
        current_user = request.session['user_id']
        if request.method == "POST":
            unit_name = request.POST['unit_name']
            new_record = unit_details.objects.create(user_id=current_user, unit_name=unit_name)
            new_record.save()
            messages.success(request, "Unit Name Created Successfully")

    except Exception as e:
        print("exception\t:\t", e)
        messages.error(request, "Failed ! To created New Unit")
    return redirect("/dashboard/list-unitname/")


def list_unitname(request):
    try:
        current_user = request.session['user_id']
        print(current_user)
        query = ''
        try:
            query = request.GET['query']
        except Exception as e:
            print("No Serach Query\t:\t", e)
        if query:
            units_details = unit_details.objects.filter(Q(unit_name__icontains=query)).order_by('-id')
        else:
            units_details = unit_details.objects.all().order_by('-id')
        paginator = Paginator(units_details, 10)
        page = request.GET.get('page')
        try:
            units_details = paginator.page(page)
        except PageNotAnInteger:
            units_details = paginator.page(1)
        except EmptyPage:
            units_details = paginator.page(paginator.num_pages)
        context = {
            'units_details': units_details,
            'user_id': current_user,
            'query':query,
        }
        return render(request, 'dashboard/unit_details.html', context)
    except Exception as e:
        messages.error(request, "There is an critical issue")
        print("exception \t:\t", e)

    return render(request, 'dashboard/main.html')



# CRUD for Unit Name with Address
def get_unit_names(request):
    response  = unit_details.objects.all().order_by('-id')
    data = serializers.serialize('json', list(response), fields=('id', 'unit_name'))
    return JsonResponse(data, safe=False,)

def delete_unitname_address(request):
    if request.method == "GET":
        data_id = request.GET['data-id']
        try:
            unit_address_details.objects.filter(id=data_id).delete()
        except Exception as e:
            print('unit Name Address  ',e)
        messages.success(request, "Data Deleted Successfully")
        return JsonResponse(True, safe=False)
    return HttpResponse("test")


def update_unitname_address(request):
    if request.method == "GET":
        data_id = request.GET['data-id']
        unit_address = request.GET['unit_address']
        unit_name = request.GET['unit_name']
        phone_no = request.GET['unit_person_no']
        unit_person_name = request.GET['person_name']
        unit_status = request.GET['status']
        unit_address_details.objects.filter(id=data_id).update(unit_details_id = unit_name, unit_address=unit_address, rank_message_sender=unit_person_name,
                                                             phone_number= phone_no, status=unit_status)
        messages.success(request, "Data Updated Successfully")
        return JsonResponse(True, safe=False)
    return HttpResponse("test")


def create_unitname_address(request):
    try:
        current_user = request.session['user_id']
        if request.method == "POST":
            unit_details_id = request.POST['unit_name']
            unit_address = request.POST['unit_address']
            phone_no = request.POST['unit_person_no']
            unit_person_name = request.POST['person_name']
            unit_status = request.POST['status']

            unit_name_value = unit_details.objects.get(id=unit_details_id)
            new_record = unit_address_details.objects.create(user_id=current_user, unit_details_id = unit_name_value, unit_address=unit_address, rank_message_sender=unit_person_name,
                                                             phone_number= phone_no, status=unit_status)
            new_record.save()
            messages.success(request, "Address Created Successfully")

    except Exception as e:
        print("exception\t:\t", e)
        messages.error(request, "Failed ! To created New Unit")
    return redirect("/dashboard/list-unitname-address/")


def list_unitname_address(request):
    try:
        current_user = request.session['user_id']
        query = ''
        try:
            query = request.GET['query']
        except Exception as e:
            print("No Serach Query\t:\t", e)
        if query:
            units_details_address = unit_address_details.objects.filter(Q(unit_address__icontains=query)).order_by('-id')
        else:
            units_details_address = unit_address_details.objects.all().order_by('-id')
        paginator = Paginator(units_details_address, 10)
        page = request.GET.get('page')
        try:
            units_details_address = paginator.page(page)
        except PageNotAnInteger:
            units_details_address = paginator.page(1)
        except EmptyPage:
            units_details_address = paginator.page(paginator.num_pages)
        context = {
            'units_details_address': units_details_address,
            'user_id': current_user,
            'query':query,
        }
        return render(request, 'dashboard/unit_address.html', context)
    except Exception as e:
        messages.error(request, "There is an critical issue")
        print("exception \t:\t", e)

    return render(request, 'dashboard/main.html')


def delete_unitname_address_comment(request):
    if request.method == "GET":
        data_id = request.GET['data-id']
        try:
            unit_comment_details.objects.filter(id=data_id).delete()
        except Exception as e:
            print('unit  Comment  ',e)
        messages.success(request, "Data Deleted Successfully")
        return JsonResponse(True, safe=False)
    return HttpResponse("test")


def update_unitname_address_comment(request):
    if request.method == "GET":
        data_id = request.GET['data-id']
        unit_name = request.GET['unit_name']
        vehicle_no = request.GET['vehicle_no']
        unit_problem = request.GET['unit_problem']
        driver_name = request.GET['driver_name']
        make_type = request.GET['make_type']
        remark = request.GET['remark']
        unit_comment_details.objects.filter(id=data_id).update(unit_address_details_id = unit_name, problem=unit_problem, remarks=remark, car_type=make_type ,vehicle_no=vehicle_no,
                                                             driver_name=driver_name)
        messages.success(request, "Data Updated Successfully")
        return JsonResponse(True, safe=False)
    return HttpResponse("test")


def create_unitname_address_comment(request):
    try:
        current_user = request.session['user_id']
        if request.method == "POST":
            unit_details_id = request.POST['unit_name']
            vehicle_no = request.POST['vehicle_no']
            unit_problem = request.POST['unit_problem']
            driver_name = request.POST['driver_name']
            vehicle_type_make = request.POST['vehicle_type_make']
            unit_remarks = request.POST['unit_remarks']

            unit_name_value = unit_details.objects.get(id=unit_details_id)
            new_record = unit_comment_details.objects.create(user_id=current_user, unit_address_details_id = unit_name_value, problem=unit_problem, remarks=unit_remarks, car_type=vehicle_type_make, vehicle_no=vehicle_no,
                                                             driver_name=driver_name)
            new_record.save()
            messages.success(request, "Comment Created Successfully")

            # // used for sms
            numbers = []
            message = 'Car No: '+ vehicle_no + '. Model : '+ vehicle_type_make + '. Driver Name : '+ driver_name + '. Problem : '+unit_problem
            unit_name_value = unit_address_details.objects.filter(unit_details_id=unit_details_id).filter(status= True)
            print(unit_name_value)
            for i in unit_name_value:
                numbers.append(int(i.phone_number))
            print(numbers)
            print(message)

            messages.success(request, "Masseges Send Successfully")

    except Exception as e:
        print("exception\t:\t", e)
        messages.error(request, "Failed ! To created New Unit")
    return redirect("/dashboard/list-unitname-address-comment/")


def list_unitname_address_comment(request):
    try:
        current_user = request.session['user_id']
        query = ''
        try:
            query = request.GET['query']
        except Exception as e:
            print("No Serach Query\t:\t", e)
        if query:
            units_details_comment = unit_comment_details.objects.filter(Q(vehicle_no__icontains=query)).order_by('-id')
        else:
            units_details_comment = unit_comment_details.objects.all().order_by('-id')
        paginator = Paginator(units_details_comment, 10)
        page = request.GET.get('page')
        try:
            units_details_comment = paginator.page(page)
        except PageNotAnInteger:
            units_details_comment = paginator.page(1)
        except EmptyPage:
            units_details_comment = paginator.page(paginator.num_pages)
        context = {
            'units_details_comment': units_details_comment,
            'user_id': current_user,
            'query':query,
        }
        return render(request, 'dashboard/unit_address_comments.html', context)
    except Exception as e:
        messages.error(request, "There is an critical issue")
        print("exception \t:\t", e)

    return render(request, 'dashboard/main.html')
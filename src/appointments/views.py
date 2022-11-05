from django.shortcuts import render
from .models import *
import datetime
from django.contrib.auth.decorators import login_required


@login_required
def add_appointment(request):
    return render(request, 'appointments/add_appointment.html', context={})


@login_required
def submit_appointment(request):
    obj = Appointment()
    obj.title = request.GET.get('title')
    obj.client = request.GET.get('client')
    obj.time = request.GET.get('time')
    obj.save()
    context = {
        "appointments": Appointment.objects.all()
    }
    return render(request, 'appointments/list_appointment.html', context=context)


@login_required
def list_appointment(request):
    context = {
        "appointments": Appointment.objects.all()
    }
    return render(request, 'appointments/list_appointment.html', context=context)


@login_required
def delete_appointment(request, id):
    obj = Appointment.objects.get(id=id)
    obj.delete()
    context = {
        "appointments": Appointment.objects.all()
    }
    return render(request, 'appointments/list_appointment.html', context=context)


@login_required
def edit_appointment(request, id):
    obj = Appointment.objects.get(id=id)
    context = {
        "title": obj.title,
        "client": obj.client,
        "time": obj.time,
        "id": obj.id
    }
    return render(request, 'appointments/edit_appointment.html', context=context)


@login_required
def update_appointment(request, id):
    obj = Appointment(id=id)
    obj.title = request.GET.get('title')
    obj.client = request.GET.get('client')
    obj.time = request.GET.get('time')
    updated_at = datetime.datetime.now()
    obj.created_at = updated_at
    obj.save()
    context = {
        "appointments": Appointment.objects.all()
    }
    return render(request, 'appointments/list_appointment.html', context=context)

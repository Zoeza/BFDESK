from django.http import Http404
from django.shortcuts import render, redirect
from .models import Client
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q


@login_required
def add_client(request):
    return render(request, "clients/add-client.html", {})


@login_required
def submit_client(request):
    client = Client()
    client.name = request.GET.get('name')
    client.email = request.GET.get('email')
    client.birthday = request.GET.get('birthday')
    client.lawyer = request.GET.get('lawyer')
    client.address = request.GET.get('address')
    client.save()

    context = {
        "clients": Client.objects.all()
    }

    return render(request, "clients/clients-list.html", context=context)


@login_required
def manage_client(request):
    context = {
        'clients': Client.objects.all(),
    }
    return render(request, "clients/clients-list.html", context)


@login_required
def edit_client(request, id):
    obj = Client.objects.get(id=id)
    context = {
        "name": obj.name,
        "email": obj.email,
        "birthday": obj.birthday,
        "lawyer": obj.lawyer,
        "address": obj.address,
        "id": obj.id
    }
    return render(request, "clients/edit-client.html", context)


@login_required
def delete_client(request, id):
    obj = Client.objects.get(id=id)
    obj.delete()
    context = {
        "clients": Client.objects.all()
    }
    return render(request, "clients/clients-list.html", context)


@login_required
def update_client(request, id):
    obj = Client(id=id)
    obj.name = request.GET.get('name')
    obj.email = request.GET.get('email')
    obj.birthday = request.GET.get('birthday')
    obj.lawyer = request.GET.get('lawyer')
    obj.address = request.GET.get('address')
    obj.save()
    context = {
        "clients": Client.objects.all()
    }
    return render(request, "clients/clients-list.html", context)


@login_required
def search_client(request):
    results = []
    if request.method == "GET":

        query = request.GET.get('search')

        if query:
            results = Client.objects.filter(
                Q(name__icontains=query) | Q(email__icontains=query) | Q(birthday__icontains=query) | Q(
                    address__icontains=query) | Q(lawyer__icontains=query))

    return render(request, 'clients/clients-search.html', {'query': query, 'results': results})

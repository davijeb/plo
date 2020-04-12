from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

import django_tables2 as tables

from .models import User

class SimpleTable(tables.Table):
    class Meta:
        model = User


def test(request):
	return HttpResponse("Hello...")

def detail(request, user_id): 
	user = get_object_or_404(User, pk=user_id)
	return render(request, 'ploadmin/detail.html', {'user': user})

def results(request):
    table = SimpleTable(
        User.objects.all(), attrs={"class": "paleblue"}, template_name="django_tables2/table.html"
    )
    return render(request, "ploadmin/results.html", {"table": table})

def modify(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	email = request.POST['email']
	print('Email is', email)
	user.email = email
	user.save()

	return HttpResponseRedirect(reverse('ploadmin:index'))


def index(request):
	latest_user = User.objects.order_by('id')[:5]
	return render(request, 'ploadmin/index.html', {'latest_user': latest_user})
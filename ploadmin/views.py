from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import User

def test(request):
	print('hello')
	return HttpResponse("Hello...")

def detail(request, user_id): 
	user = get_object_or_404(User, pk=user_id)
	return render(request, 'ploadmin/detail.html', {'user': user})

def results(request, user_id):
	return HttpResponse("You are looking at the results for question {}".format(user_id))

def vote(request, user_id):
	return HttpResponse("You are voting on question {}".format(user_id))

def index(request):
	print('***********')
	latest_user = User.objects.order_by('id')[:5]
	return render(request, 'ploadmin/index.html', {'latest_user': latest_user})
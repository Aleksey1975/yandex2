from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def index(r):
    return HttpResponse('Yandex2')

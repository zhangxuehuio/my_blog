# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hello Django")


def detail(request, id):
    return HttpResponse("You're looking at my_args %s." % id)
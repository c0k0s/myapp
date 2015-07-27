from django.shortcuts import render, redirect
from waybill.models import *
import ast
import urllib2
import json
import datetime
import string
import random
import Image
import csv
from django.http import HttpResponse
from pymongo import MongoClient


def views(request):
	cityData = City.objects.all()
	return render(request, 'views.html',locals())


def scan(request):
	if request.method =="POST":
		name = request.POST.get('name')
		code = request.POST.get('code')		
		try:			
			cityObj = City(name = name, code = code)
			cityObj.save()
			msg = 'SUCCESS'
		except:
			pass
			msg = 'FAIL'
	return render(request, 'scan.html',locals())
		
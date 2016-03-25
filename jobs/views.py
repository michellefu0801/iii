# -*- coding: utf-8 -*-
import json
import csv
# from __future__ import unicode_literals
from django.utils import timezone
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render_to_response, render
from jobs.models import Job
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core import serializers
import os

def JobList(request):
    jobs = Job.objects.filter(cluster = 2)
    return render_to_response('JobList.html',locals())
	
def job_recommend(request):
    jobs = Job.objects.filter(skill__contains = 'java' )
    return render_to_response('job_recommend.html',locals())
	
def TaiwanMap_test2(request):
    return render(request,'TaiwanMap_test2.html',locals())

#def load_json(request):	 
    # dir = os.path.dirname(__file__)                               
    # f = open(dir+'\static\\twCounty2010.geo_1.json', 'r')
    # data = json.loads(f.read().decode('utf-8'))
    # f.close
    # return JsonResponse(data, safe=False)
	
# def load_csv(request):
    # dir= os.path.dirname(__file__)                               
    # f=open(dir+'\\static\\201512_new.csv', 'r')
    # data = csv.loads(f.read().decode('utf-8'))
    # f.close
    # return CsvResponse(data, safe=False)    

# Create your views here.

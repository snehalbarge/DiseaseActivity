from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.conf.urls import url, include
import xml.etree.ElementTree as ET
import requests
import json

@api_view(['GET','POST'])
def get_result(request, disease, no_of_days):
    disease = disease.replace(' ','+')
    url = "https://clinicaltrials.gov/ct2/results/rss.xml?rcv_d={}&lup_d=&sel_rss=new14&cond={}&count=10000"
    url = url.format(no_of_days, disease)
    response_xml_as_string = requests.get(url).text
    responseXml = ET.fromstring(response_xml_as_string)
    items = responseXml.find('channel').findall('item')
    result_string = "{} modifications for disease {} in last {} days".format(len(items), disease.replace('+', ' '), no_of_days)
    result = {'result': result_string}
    return HttpResponse(str(result))


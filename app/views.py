import os

from django.http import JsonResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt

import json
# Create your views here.
from app.utils.utils import getWsd, formatResult, getMessage


def index(request):
    return render(request,'index.html')

@csrf_exempt
def searchWsd(request):
    security=json.loads(str(request.body, encoding = "utf-8"))['security']
    data=getWsd(security)
    result=formatResult(data)
    message=getMessage(data.ErrorCode)
    return JsonResponse({"errorcode":data.ErrorCode,"message":message,"security":security,"result":result})

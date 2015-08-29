# -*- coding:utf-8 -*-

import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from apps.teste.utils import soma

@csrf_exempt
def view_soma(request):

    valor1 = request.POST.get("valor1")
    valor2 = request.POST.get("valor2")

    resultado = soma(int(valor1), int(valor2))

    return HttpResponse(json.dumps({"resultado": resultado}), content_type='application/json')

from django.shortcuts import render

from django.http import JsonResponse # addition

# Create your views here.

#  addition code
def getRoutes(request):
    return JsonResponse('Our API', safe=False)
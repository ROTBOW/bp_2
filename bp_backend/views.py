from django.shortcuts import render
from django.http.response import JsonResponse

def ping(req) -> JsonResponse:
    return JsonResponse({'res': 'GOOD'})
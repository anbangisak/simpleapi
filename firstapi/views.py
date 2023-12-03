from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def dashboard(request):
    return HttpResponse("Hello world!")

def api_one(request):
    resp_content = {
        "status": "active"
    }
    return JsonResponse(resp_content, status=200)

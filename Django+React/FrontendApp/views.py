from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index(request):
    return render(request,'frontend/index.html')


def second_index(request):

    return JsonResponse([{"id":1,"name":"chetan"},{"id":2,"name":"john"}],safe=False)
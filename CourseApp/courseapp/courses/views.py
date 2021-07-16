from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. (nơi nhập các request của phía người dùng)


def index(request):
    return render(request, template_name='index.html', context={
        'name': 'Uyen Nguyen'
    })

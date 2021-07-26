from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import View


# Create your views here. (nơi nhập các request của phía người dùng)


def index(request):
    return render(request, template_name='index.html', context={
        'name': 'Uyen Nguyen'
    })


def welcome(request, year):
    return HttpResponse("HELLO " + str(year))


def welcome2(request, year):
    return HttpResponse("HELLO " + str(year))


class TestView(View):
    def get(self, request):
        return HttpResponse("TESTING")

    def post(self, request):
        pass
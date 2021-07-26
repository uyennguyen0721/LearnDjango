from django.contrib import admin
from django.urls import path, re_path
from . import views     #'.' là gọi thư mục hiện tại
#from .admin import admin_site

#đây là url riêng của app, sau khi tìm ở urls trong course nếu không thấy thì đến đây để tìm

urlpatterns = [
    path('', views.index, name="index"), #thêm thuộc tính name để sau này phân giải các đường dẫn, giống như dùng url_for trong Flask
    path('welcome/<int:year>', views.welcome, name="welcome"),
    path('test/', views.TestView.as_view()),
    re_path(r'^welcome2/(?P<year>[0-9]{1,2})/$', views.welcome2, name="welcome2"),
    #path('admin/', admin_site.urls)
]
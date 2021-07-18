from django.contrib import admin
from django.urls import path
from . import views     #'.' là gọi thư mục hiện tại
from .admin import admin_site

#đây là url riêng của app, sau khi tìm ở urls trong course nếu không thấy thì đến đây để tìm

urlpatterns = [
    path('', views.index, name="index"), #thêm thuộc tính name để sau này phân giải các đường dẫn, giống như dùng url_for trong Flask
    path('admin/', admin_site.urls)

]
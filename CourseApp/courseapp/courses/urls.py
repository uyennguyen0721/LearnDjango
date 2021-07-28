from django.contrib import admin
from django.urls import path, re_path, include
from . import views     #'.' là gọi thư mục hiện tại
#from .admin import admin_site
from rest_framework.routers import DefaultRouter

#đây là url riêng của app, sau khi tìm ở urls trong course nếu không thấy thì đến đây để tìm

#3
router = DefaultRouter()
router.register('courses', views.CourseViewSet)
router.register('lessons', views.LessonViewSet)

urlpatterns = [
    path('', include(router.urls)), #4 ---> Tạo ra 2 endpoint tương ứng với 5 API là:
    # /courses/ - GET   ---> lấy danh sách
    # /courses/ - POST  ---> thêm một khóa học mới
    # /courses/{course_id}/ - GET   ---> xem chi tiết một khóa học
    # /courses/{course_id}/ - PUT   ---> cập nhật
    # /courses/{course_id}/ - DELETE    ---> xóa


    #path('', views.index, name="index"), #thêm thuộc tính name để sau này phân giải các đường dẫn, giống như dùng url_for trong Flask
    #path('welcome/<int:year>', views.welcome, name="welcome"),
    #path('test/', views.TestView.as_view()),
    #re_path(r'^welcome2/(?P<year>[0-9]{1,2})/$', views.welcome2, name="welcome2"),
    #path('admin/', admin_site.urls)
]
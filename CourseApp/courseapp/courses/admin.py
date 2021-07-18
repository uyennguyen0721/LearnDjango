from django.contrib import admin
from .models import Category, Course, Lesson, Tag

# Register your models here. (Nơi cấu hình những thông tin của trang admin)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
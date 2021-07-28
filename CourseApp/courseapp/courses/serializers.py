#trước khi tạo ra file này cần chạy lệnh sau: pip install djangorestframework

#chuyên dữ liệu phức tạp từ querysets để chuyển thành các dạng dữ liệu đơn giản, ví dụ như JSON để gửi ra bên ngoài
#có hai loại serializers là serializers liên kết với models và serializers không liên kết với models

#ở đây là demo serializers liên kết với models

from rest_framework.serializers import ModelSerializer
from .models import Course, Lesson, Tag


class CourseSerializer(ModelSerializer):    #1
    class Meta:
        model = Course
        #chỉ định các trường để serialize ra, parse thành JSON để gửi ra bên ngoài cho client gọi API
        fields = ["id", "subject", "image", "created_date", "category"]


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class LessonSerializer(ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Lesson
        fields = ["id", "subject", "content", "created_date", "course", "image", "tags"]

#trước khi tạo ra file này cần chạy lệnh sau: pip install djangorestframework

#chuyên dữ liệu phức tạp từ querysets để chuyển thành các dạng dữ liệu đơn giản, ví dụ như JSON để gửi ra bên ngoài
#có hai loại serializers là serializers liên kết với models và serializers không liên kết với models

#ở đây là demo serializers liên kết với models

from rest_framework.serializers import ModelSerializer
from .models import Course, Lesson, Tag, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "username", "password", "avatar"]
        extra_kwargs = {
            'password': {'write_only': 'true'}  # password chỉ dùng để ghi và để đọc, không dùng để view
        }

    # khi create sẽ gọi phương thức này chứ không gọi phương thức create của API nữa
    def create(self, validated_data):
        user = User(**validated_data) #dùng **validated_data không cần phải ghi 2 lệnh dưới, nó sẽ tự động lấy dữ liệu lên và chỉ set lạ password, mọi thông tin còn lại giữ nguyên
        # user.first_name = validated_data('first_name')
        # user.last_name = validated_data('last_name')
        user.set_password(validated_data('password'))
        user.save()
        return user



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

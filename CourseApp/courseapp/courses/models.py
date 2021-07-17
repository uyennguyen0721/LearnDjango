from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here. (Nơi tạo ra các lớp để ánh xạ đến tạo cơ sở dữ liệu theo mô hình code first)


class User(AbstractUser):
    avatar = models.ImageField(upload_to='upload/%Y/%m')


class Category(models.Model):   #courses_category
    name = models.CharField(max_length=100, null=False, unique=True)


class Course(models.Model):
    subject = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)  #auto_now_add=True: khi tạo một Course, tự động nó sẽ lấy thời điểm hiện tại lúc thêm vô để gán vô biến này mà không cần bạn quan tâm, tự động django sẽ lo
    updated_date = models.DateTimeField(auto_now=True)  #auto_now=True: nếu mỗi lần có cập nhật liên quan đến Course thì biến này sẽ được cập nhật lại, lấy thời điểm hiện tại mà mình cập nhật
    active = models.BooleanField(default=True)  #nếu khóa học đó còn thì True, không còn thì False, giống như lms của trường, các HK đã học xong ko phải đã xóa hẳn đi mà nó vẫn được lưu trữ, khi xóa thì chỉ cần tắt (False) đi, để dữ liệu quá khứ và tương lai của mình vẫn còn ổn
    category = models.ForeignKey(Category, on_delete=models.SET_NULL(), null=True)
    #on_delete=models.CASCADE(): khi xóa Category, toàn bộ Course của Category sẽ xóa theo (mối quan hệ Composition
    #on_delete=models.SET_NULL(): khi xóa Category, thì trường category này sẽ lấy giá trị null, do đó ta cần để null=True
from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here. (Nơi tạo ra các lớp để ánh xạ đến tạo cơ sở dữ liệu theo mô hình code first)


class User(AbstractUser):
    avatar = models.ImageField(upload_to='upload/%Y/%m')


class Category(models.Model):   #courses_category
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name


class ItemBase(models.Model):
    class Meta:
        abstract = True #Khi tạo bảng trong CSDL thì các lớp kế thừa lớp này sẽ được tạo thành các bảng có chứa các thuộc tính của lớp kế thừa, còn lớp kế thừa sẽ không tạo thành bảng

    subject = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='courses/%Y/%m', default=None)
    created_date = models.DateTimeField(auto_now_add=True)  # auto_now_add=True: khi tạo một Course, tự động nó sẽ lấy thời điểm hiện tại lúc thêm vô để gán vô biến này mà không cần bạn quan tâm, tự động django sẽ lo
    updated_date = models.DateTimeField(auto_now=True)  # auto_now=True: nếu mỗi lần có cập nhật liên quan đến Course thì biến này sẽ được cập nhật lại, lấy thời điểm hiện tại mà mình cập nhật
    active = models.BooleanField(default=True)  # nếu khóa học đó còn thì True, không còn thì False, giống như lms của trường, các HK đã học xong ko phải đã xóa hẳn đi mà nó vẫn được lưu trữ, khi xóa thì chỉ cần tắt (False) đi, để dữ liệu quá khứ và tương lai của mình vẫn còn ổn

    def __str__(self):
        return self.subject


class Course(ItemBase):
    class Meta:
        unique_together = ('subject', 'category')   #Tên (subject) của khóa học (Course) trong cùng một danh mục (Category) không được trùng nhau
        ordering = ["-id"]
        #sắp xếp tăng dần theo ID, nếu sắp xếp giảm thì thay "id" bằng "-id"
        #có thể sắp xếp theo nhiều thuộc tính, ví dụ sắp xếp theo chủ đề và ngày tạo: ordering = ["subject", "created_date"]
        #ordering này có thể ghi đè lại trong quá trình làm

    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)    #Many to one
    #on_delete=models.CASCADE: khi xóa Category, toàn bộ Course của Category sẽ xóa theo (mối quan hệ Composition
    #on_delete=models.SET_NULL: khi xóa Category, thì trường category này sẽ lấy giá trị null, do đó ta cần để null=True


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Lesson(ItemBase):
    class Meta:
        unique_together = ('subject', 'course') #Trong cùng một khóa học (Course) không được trùng tên (subject) bài học (Lesson)

    content = RichTextField()
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)
    #on_delete=models.SET_DEFAULT: Khi Course của Lesson bị xóa đi, các bạn muốn cho Lesson này thuộc vào cái Course mặc định
    #on_delete=models.PROTECT: Cấm --> Khi những Course có những Lesson thì không được xóa những Course đó
    tags = models.ManyToManyField(Tag, related_name="lessons", blank=True, null=True)   #blank=True: được phép rỗng     #Many to many
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import View
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

from .models import Course, Lesson, User
from .serializers import CourseSerializer, LessonSerializer, UserSerializer


# Create your views here. (nơi nhập các request của phía người dùng)

#generics.ListAPIView: API lấy danh sách tất cả các User
#generics.CreateAPIView: tạo ra API Create ---> POST
#generics.RetrieveAPIView: API lấy thông tin của user hiện tại ra, user phải được chứng thực mới làm được việc nà ---> GET
#Với 3 cái này nó sẽ hiện thực sẵn cho mình 3 API: API lấy danh sách các User, API Create, API lấy thông tin 1 user
class UserViewSet(viewsets.ViewSet, generics.UpdateAPIView, generics.CreateAPIView, generics.RetrieveAPIView): #ViewSet không hiện thực sẵn nên ta có thể kết hợp với generics để tạo ra API
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser]

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonSerializer

    @swagger_auto_schema(
        operation_description='API này dùng để ẩn một bài viết từ phía Client',
        responses={
            status.HTTP_200_OK: LessonSerializer()
        }
    )

    # ẩn lesson (active = false)
    @action(methods=['post'], detail=True,
            url_path='hide-lesson')  # ngoài năm API có sẵn, mặc định sẽ cũng cung cấp 1 API nữa: /lesson/{pk}/hide-lesson (nếu ko có url_path thì mặc định sẽ lấy tên là hide_lesson)
    def hide_lesson(self, request, pk):
        try:
            l = Lesson.objects.get(pk=pk)
            l.active = False
            l.save()
        except Lesson.DoesNotExits:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(data=LessonSerializer(l, context={'request': request}).data, status=status.HTTP_200_OK)
        # context={'request': request}: nếu thêm biến này vô thì khi active = false thì trường image sẽ hiển thị đầy đủ đường dẫn


class CourseViewSet(viewsets.ModelViewSet): #2
    #đưa ra câu truy vấn
    queryset = Course.objects.filter(active=True)   # lấy những khóa học có thuộc tính active = True
    #dùng serializer để parse có dữ liệu từ queryset ra bên ngoài
    serializer_class = CourseSerializer
    #tất cả API của CourseViewSet bắt buộc phải ở trạng thái của 1 user đã đăng nhập mới dduocj truy vấn
    #permission_classes = [permissions.IsAuthenticated]
    swagger_schema = None  # không cho hiển thị bộ swagger cho Course

    # phương thức ghi dè permissions
    # def get_permissions(self):
    #     if self.action == 'list': #nếu hành động này người dùng có đăng nhập hay không đều cho xem
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]  #tất cả các thao tác còn lại trong đây bắt buộc phải đăng nhập mới truy cập được

    #chỉ hai câu lệnh trên nó đã tạo ra cho chúng ta 5 API:
    # List (GET) ----> Xem danh sách khóa học
    # Create (POST) ----> Thêm một khóa học
    # detail ----> Xem chi tiết một khóa học
    # ... (PUT) ----> Cập nhật một khóa học
    # ... (DELETE) ----> Xóa một khóa học



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
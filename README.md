# LearnDjango

Cần nhấn Ctrl + C để tắt server, nếu không khi chạy lại sẽ báo cùng port

Các câu lệnh trong Terminal:
- Cài django: pip install django
- Tạo project: django-admin startproject <project_name>
- Đi đến một thư mục bất kì: cd <folder_name>/
- Chạy project: python manage.py runserver
- Tạo app: django-admin startapp <app_name>
- Cài đặt Mysql driver: pip install mysqlclient
- Chuyển models xuống CSDL hay mỗi lần update models: đầu tiên phải khai báo app trong setting ở INSTALLED_APPS,
sau đó thực hiện lần lượt các lệnh sau:
	+ Lệnh makemigrations cho django biết có sự thay đổi trong models.py và ta muốn lưu các thây đổi số trong migration (tạo migration):   python manage.py makemigrations <app_name>
	+ Lệnh migrate thực thi migration để áp dụng những thay đổi trong models xuống lược đồ cơ sở dữ liệu (tác động xuống CSDL):	python manage.py migrate
- Có thể sử dụng lệnh sqlmigrate để xem SQL sẽ được tạo ra từ một migration để thực thi trong CSDL:
	python manage.py sqlmigrate <app_name> <mã ở đầu tên file migration> 
- Cài thư viên Pillow:	python install pillow
- Tạo ra một superuser đầu tiên: python manager.py createsuperuser
- Truy xuất dữ liệu (thường được sử dụng trong debug) trong terminal trước hết phải dùng lệnh: python manager.py shell
sau đó dùng các câu lệnh truy xuất để truy xuất dữ liệu

Một số tương tác dữ liệu trên python shell trong django:

(venv) C:\Users\uyenn\PycharmProjects\LearnDjango\CourseApp\courseapp>python manage.py shell
Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from courses.models import *
>>> c = Category(name="Lập trình Java")
>>> c.save()
>>> Category.objects.create(name="Lập trình hiện đại")
<Category: Category object (2)>
>>> Category.objects.get_or_create(name="Thiết kế Web")
(<Category: Category object (3)>, True)
>>> c = Category.objects.get(pk=1)
>>> c
<Category: Category object (1)>
>>> c.__dict__
{'_state': <django.db.models.base.ModelState object at 0x000002C9AFA633D0>, 'id': 1, 'name': 'Lập trình Java'}
>>> Course.objects.create(subject="Core Java", description="Nhập môn", category=c)
<Course: Course object (1)>
>>> Category.objects.filter(name__contains="Java")
<QuerySet [<Category: Category object (1)>]>
>>> Category.objects.filter(name__startswith="Java")
<QuerySet []>
>>> Category.objects.filter(name__endswith="Java")
<QuerySet [<Category: Category object (1)>]>
>>> c = Category.objects.filter(name__contains="Java")
>>> print(c.query)
SELECT `courses_category`.`id`, `courses_category`.`name` FROM `courses_category` WHERE `courses_category`.`name` LIKE BINARY %Java%
>>> c = Category.objects.filter(name__startswith="Java")
>>> print(c.query)
SELECT `courses_category`.`id`, `courses_category`.`name` FROM `courses_category` WHERE `courses_category`.`name` LIKE BINARY Java%
>>> Course.objects.all()
<QuerySet [<Course: Course object (1)>]>
>>> q = Course.objects.filter(category__name__contains="Java")
>>> print(q.query)
SELECT `courses_course`.`id`, `courses_course`.`subject`, `courses_course`.`description`, `courses_course`.`created_date`, `courses_course`.`updated_date`, `courses_c
ourse`.`active`, `courses_course`.`category_id` FROM `courses_course` INNER JOIN `courses_category` ON (`courses_course`.`category_id` = `courses_category`.`id`) WHER
E `courses_category`.`name` LIKE BINARY %Java%
>>> q
<QuerySet [<Course: Course object (1)>]>
>>> q = Course.objects.filter(category__name__icontains="java")
>>> print(q.query)
SELECT `courses_course`.`id`, `courses_course`.`subject`, `courses_course`.`description`, `courses_course`.`created_date`, `courses_course`.`updated_date`, `courses_c
ourse`.`active`, `courses_course`.`category_id` FROM `courses_course` INNER JOIN `courses_category` ON (`courses_course`.`category_id` = `courses_category`.`id`) WHER
E `courses_category`.`name` LIKE %java%
>>> q
<QuerySet [<Course: Course object (1)>]>
>>>







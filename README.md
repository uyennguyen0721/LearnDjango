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



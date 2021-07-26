from django.contrib import admin
from django.contrib.auth.models import Permission
from django import forms
from django.db.models import Count
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.html import mark_safe
from .models import Category, Course, Lesson, Tag, User
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonTagInline(admin.TabularInline):
    model = Lesson.tags.through


class LessonAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('/static/css/main.css',)
        }

    form = LessonForm
    list_display = ["id", "subject", "created_date", "course"]
    search_fields = ["subject", "created_date", "course__subject"]
    list_filter = ["subject", "course__subject"]
    readonly_fields = ["avatar"]
    inlines = (LessonTagInline, )

    def avatar(self, lesson):
        return mark_safe("<img src='/static/{img_url}' alt='{alt}' width='120px'/>".format(img_url=lesson.image.name, alt=lesson.subject))


#Many to one
class LessonInline(admin.StackedInline):    #StackedInline: tạo các form nằm chồng lên nhau
    model = Lesson                          #InlineModelAdmin: dạng inline chuẩn
    pk_name = 'course'                      #TabularInline: dạng bảng


class CourseAdmin(admin.ModelAdmin):
    inlines = (LessonInline, )


class CourseAppAdminSite(admin.AdminSite):
    site_header = 'HỆ THỐNG QUẢN LÝ KHÓA HỌC'

    def get_urls(self):
        return [
            path('course-stats/', self.course_stats)
        ] + super().get_urls()

    def course_stats(self, request):
        course_count = Course.objects.count()
        stats = Course.objects.annotate(lesson_count=Count('lessons')).values("id", "subject", "lesson_count")  #lessons: là related_name của biến course trong models
        return TemplateResponse(request, 'admin/course-stats.html', {
            'course_count': course_count,
            'stats': stats
        })


#admin_site = CourseAppAdminSite('mycourse')


# Register your models here. (Nơi cấu hình những thông tin của trang admin)
admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(User)
admin.site.register(Permission)
#admin_site.register(Category)
#admin_site.register(Course, CourseAdmin)
#admin_site.register(Lesson, LessonAdmin)
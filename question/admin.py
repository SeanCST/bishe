from django.contrib import admin

from .models import Question, Teacher, Student, ExerciseHistory

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('nid', 'title', 'subject', 'chapter', 'difficulty_degree', 'pub_time',)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('username',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_number', 'name', 'school', 'major', 'attendance_year')

class ExerciseHistoryAdmin(admin.ModelAdmin):
    list_display = ('student_number', 'question_numbers', 'score', 'subject', 'submit_time')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(ExerciseHistory, ExerciseHistoryAdmin)
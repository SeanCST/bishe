from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.teacher_login, name='teacher_login'),
    url(r'^index/$', views.teacher_login, name='index'),
    url(r'^teacher_login/$', views.teacher_login, name = 'teacher_login'),

    url(r'^teacher_regist/$', views.teacher_regist, name = 'teacher_regist'),
    url(r'^teacher_logout/$', views.teacher_logout, name = 'teacher_logout'),

    url(r'^student_regist/$', views.student_regist, name='student_regist'),
    url(r'^student_login/$', views.student_login, name='student_login'),
    url(r'^get_student_profile/$', views.get_student_profile, name='get_student_profile'),
    url(r'^update_student_profile/$', views.update_student_profile, name='update_student_profile'),

    url(r'^save_exercise_history/$', views.save_exercise_history, name='save_exercise_history'),
    url(r'^get_exercise_history/$', views.get_exercise_history, name='get_exercise_history'),

    url(r'^upload_questions/$', views.upload_questions),
    url(r'^submit_excel_action/$', views.submit_excel_action, name='submit_excel_action'),
    url(r'^get_questions_json/$', views.get_questions_json, name='get_questions_json'),

    url(r'^get_questions_json_by_q_nums/$', views.get_questions_json_by_q_nums, name='get_questions_json_by_q_nums'),
]

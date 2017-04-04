from django.db import models

# from django.contrib.postgres.fields import JSONField

# Create your models here.
class Question(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.TextField(u'题目' ,default='TITLE')
    options = models.TextField(u'选项' ,default='OPTIONS')
    answer = models.CharField(u'答案', max_length=32, default='A')
    subject_number = models.IntegerField(u'课程号', default=0)
    subject = models.CharField(u'课程名称', max_length=32, default='SUBJECT')
    chapter_number = models.IntegerField(u'章节号', default=0)
    chapter = models.CharField(u'章节名', max_length=32, default='CHAPTER')
    difficulty_degree = models.IntegerField(u'难度系数', default=5)
    pub_time = models.DateTimeField(u'收录时间', auto_now=True)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    username = models.CharField(u'账号', max_length=50)
    password = models.CharField(u'密码', max_length=50)

    def __str__(self):
        return self.username


class Student(models.Model):
    student_number = models.CharField(u'学号', max_length=50)
    password = models.CharField(u'密码' ,max_length=50)
    name = models.CharField(u'姓名' ,max_length=50)
    school = models.CharField(u'学校', max_length=50, null=True, default='华侨大学')
    major = models.CharField(u'专业' ,max_length=50, null=True, default='计算机')
    attendance_year = models.CharField(max_length=50, null=True, default='2013')

    def __str__(self):
        return self.student_number


class ExerciseHistory(models.Model):
    student_number = models.CharField(u'学号',max_length=50)
    question_numbers = models.CharField(u'题目序号',max_length=50)
    submit_options = models.CharField(u'提交选项',max_length=50)
    score = models.CharField(u'分数',max_length=20)
    subject = models.CharField(u'科目', max_length=20, null=True)
    submit_time = models.DateTimeField(u'提交时间',auto_now=True)

    def __str__(self):
        return self.student_number
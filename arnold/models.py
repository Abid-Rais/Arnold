from django.db import models


class Student(models.Model):
    studentID = models.IntegerField(primary_key=True)
    nNumber = models.CharField(max_length=10)
    netID = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    major = models.CharField(max_length=30)


class Course(models.Model):
    courseID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=35)
    department = models.CharField(max_length=35)
    courseCode = models.CharField(max_length=10)


class Section(models.Model):
    sectionID = models.IntegerField(primary_key=True)
    instructor = models.CharField(max_length=35)
    instructionMode = models.CharField(max_length=30)
    daysHeld = models.CharField(max_length=25)
    timeHeld = models.TimeField()
    duration = models.IntegerField()
    courseID = models.ForeignKey('Course', on_delete=models.CASCADE)


class AcademicProgressReport(models.Model):
    acadProgReport = models.IntegerField(primary_key=True)
    gpa = models.DecimalField()
    gradSemester = models.CharField(max_length=10)
    studentID = models.ForeignKey('Student', on_delete=models.CASCADE)

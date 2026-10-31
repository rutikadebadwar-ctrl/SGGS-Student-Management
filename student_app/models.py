from django.db import models

class Student(models.Model):
    regno = models.CharField(max_length=20, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.regno} - {self.name}"

class Marks(models.Model):
    regno = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.regno.regno} - {self.subject}"

class Hostel(models.Model):
    regno = models.ForeignKey(Student, on_delete=models.CASCADE)
    hostel_name = models.CharField(max_length=100)
    room_no = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.regno.regno} - {self.hostel_name}"

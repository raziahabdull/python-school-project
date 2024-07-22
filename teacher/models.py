from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    nationality = models.CharField(max_length=15)
    department = models.CharField(max_length=30)
    email = models.EmailField()
    course = models.CharField(max_length=50)
    teacher_id = models.PositiveSmallIntegerField()
    bank_account_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=5)

    def _str_(self):
       return f"{self.first_name}{self.last_name}"
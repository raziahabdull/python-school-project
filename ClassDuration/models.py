from django.db import models

class ClassDuration(models.Model):

    class_name = models.CharField(max_length=40)
    class_id = models.PositiveSmallIntegerField()
    course_descirption = models.CharField()
    trainner = models.PositiveSmallIntegerField()
    start_time= models.TimeField()
    day_of_the_week = models.DateField()
    end_time = models.TimeField()
    date = models.String()
    breaks= models.PositiveSmallIntegerField()

    def _str_(self):
        return f"{self.class_name}{self.class_id}"
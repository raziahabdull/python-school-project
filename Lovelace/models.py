from django.db import models

# Create your models here.

class Lovelace(models.Model):
    lovelace_name = models.CharField(max_length=10)
    lovelace_id = models.CharField(max_length=5)
    lovelace_descirption = models.TextField()
    lovelace_hours = models.PositiveSmallIntegerField(max_length=5)
    lovelace_trainer_name = models.CharField(max_length=10)
    lovelace_capacity = models.PositiveSmallIntegerField()
    room_number = models.PositiveSmallIntegerField(max_length=5)
    meeting_time = models.PositiveSmallIntegerField()
    grade_level = models.PositiveSmallIntegerField()

    def _str_(self):
        return f"{self.lovelace_id}{self.lovelace_name}" 
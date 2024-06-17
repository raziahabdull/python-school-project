from django.db import models

 class course(models.Model):
    course_name = models.charField(max_length=40)
    course_id = models.charField(max_length=20)
    course_descirption = models.TextField()
    class_hours = models.PositiveSmallIntegerField()
    prerequisites = models.charField(max_length=80)
    assessment_requirements = models.DateField()
    school_term = models.PositiveSmallIntegerField()
    course_capacity = models.PositiveSmallIntegerField()
    grade_level = models.PositiveSmallIntegerField()

    def _str_(self):
        return f"{self.course_id}{self.course_name}"
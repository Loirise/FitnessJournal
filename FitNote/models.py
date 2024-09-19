from django.db import models
import datetime

class Workout(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    date = models.DateField(null=False, blank=False, default=datetime.date.today)

    def __str__(self):
        return self.title
    

class Exercise(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name
    

class Note(models.Model):
    workout_id = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise_id = models.ForeignKey(Exercise, null=True, on_delete=models.SET_NULL)
    sets = models.PositiveIntegerField(null=False, blank=False)
    reps = models.PositiveIntegerField(null=False, blank=False)
    weight = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.exercise_id} - {self.sets} sets x {self.reps} reps"
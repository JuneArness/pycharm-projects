from django.db import models
from tkinter import *
import tkinter as tk

TYPE_CHOICES = {
    ('SQL', 'SQL'),
    ('Python', 'Python'),
    ('C#','C#'),
    ('Javascript', 'Javascript'),
}

TYPE_NUMBER = {
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
}

TYPE_LENGTH = {
    (6, 6),
    (1, 1),
    (2, 2),
}

"""I am attempting to call on this odject and have it looped so that the fields
 allow the user to delete and add the selections to the DB"""

class djangoClasses(models.Model):
    Title = models.CharField(max_length=60, default="", choices=TYPE_CHOICES)
    Course_Number = models.IntegerField(choices=TYPE_NUMBER)
    Instructor_Name = models.CharField(max_length=60, default="")
    Duration = models.FloatField(default=0, choices=TYPE_LENGTH)

    objects = models.Manager()

    def __str__(self):
        return self.Title



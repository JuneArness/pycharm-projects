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

"""I am attempting to call on this object and have it looped so that the fields
 allow the user to delete and add the selections to the DB"""


class djangoClasses(models.Model):
    Title = models.CharField(max_length=60, default="", choices=TYPE_CHOICES)
    Course_Number = models.IntegerField(choices=TYPE_NUMBER)
    Instructor_Name = models.CharField(max_length=60, default="")
    Duration = models.FloatField(default=0, choices=TYPE_LENGTH)



TYPE_HOUSING = {
    ('On Campus', 'On Campus'),
    ('Off Campus', 'Off Campus'),
}
TYPE_ROOMATE ={

    ('Yes', 'Yes'),
    ('NO', 'NO'),
}


class Housing(models.Model):
    Title = models.CharField(max_length=60, default="", choices= TYPE_HOUSING)
    Roommates = models.CharField(max_length=60, default="", choices= TYPE_ROOMATE)

obj1 = djangoClasses(Title='SQL', Course_Number=1, Instructor_Name="Dr Arness", Duration=6)
obj1.save()

obj2 = djangoClasses(Title='Python', Course_Number=2, Instructor_Name="Professor Parks", Duration=2)
obj2.save()

obj3 = djangoClasses(Title='C#', Course_Number=4, Instructor_Name="Mrs. McCoy", Duration=1)
obj3.save

objects = models.Manager()

def __str__(self):
    return self.Title



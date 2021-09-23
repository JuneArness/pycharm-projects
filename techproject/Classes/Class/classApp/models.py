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

"""These are the choices and object # 2"""

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

"""These are the choices and object # 3"""


TYPE_MAIN = {
    ('Chicken', 'Chicken'),
    ('Beef', 'Beef'),
    ('Pork','Pork'),
    ('Vegetarian', 'Vegetarian'),
}

TYPE_DRINKS = {
    ('Water', 'Water'),
    ('Milk', 'Milk'),
    ('Juice', 'Juice'),
    ('Soda', 'Soda'),
}

TYPE_SIDES = {
    ('Salad', 'Salad'),
    ('Mac and Cheese', 'Mac and Cheese'),
    ('Vegetable', 'Vegetable'),
}

class Meal(models.Model):
    Main = models.CharField(max_length=60, default="", choices=TYPE_MAIN)
    Drinks = models.CharField(max_length=60, default="", choices=TYPE_DRINKS)
    Sides = models.CharField(max_length=60, default="", choices=TYPE_SIDES)

    objects = models.Manager()

    def __str__(self):
        return self.Title



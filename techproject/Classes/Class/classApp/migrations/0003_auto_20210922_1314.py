# Generated by Django 2.0.7 on 2021-09-22 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0002_auto_20210922_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoclasses',
            name='Course_Number',
            field=models.IntegerField(choices=[('001', 1), ('003', 3), ('002', 2), ('004', 4)]),
        ),
    ]

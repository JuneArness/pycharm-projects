# Generated by Django 2.0.7 on 2021-09-22 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0005_auto_20210922_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoclasses',
            name='Course_Number',
            field=models.IntegerField(choices=[(4, 4), (1, 1), (3, 3), (2, 2)]),
        ),
        migrations.AlterField(
            model_name='djangoclasses',
            name='Duration',
            field=models.FloatField(choices=[(6, 6), (1, 1), (2, 2)], default=0),
        ),
        migrations.AlterField(
            model_name='djangoclasses',
            name='Title',
            field=models.CharField(choices=[('Python', 'Python'), ('SQL', 'SQL'), ('C#', 'C#'), ('Javascript', 'Javascript')], default='', max_length=60),
        ),
    ]

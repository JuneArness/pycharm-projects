# Generated by Django 2.0.7 on 2021-09-23 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0008_auto_20210922_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoclasses',
            name='Title',
            field=models.CharField(choices=[('Python', 'Python'), ('SQL', 'SQL'), ('C#', 'C#'), ('Javascript', 'Javascript')], default='', max_length=60),
        ),
    ]
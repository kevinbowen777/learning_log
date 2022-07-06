# Generated by Django 4.0.6 on 2022-07-06 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, verbose_name='Bio'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Name of User'),
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-27 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_about_me'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_me',
            name='bout_me',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='About_me'),
        ),
    ]

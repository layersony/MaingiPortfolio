# Generated by Django 3.1.4 on 2021-01-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20210106_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvupload',
            name='file_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='File Name'),
        ),
    ]
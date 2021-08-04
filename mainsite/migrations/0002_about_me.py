# Generated by Django 3.1.4 on 2020-12-26 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='about_me',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bout_me', models.TextField(blank=True, max_length=500, null=True, verbose_name='About_me Text')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'About_me',
                'verbose_name_plural': 'About_me',
                'managed': True,
            },
        ),
    ]

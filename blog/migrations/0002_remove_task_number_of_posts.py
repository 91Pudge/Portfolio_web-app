# Generated by Django 3.2.9 on 2021-11-16 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='number_of_posts',
        ),
    ]

# Generated by Django 3.2 on 2021-06-03 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0008_remove_subtopic_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='topic',
        ),
    ]

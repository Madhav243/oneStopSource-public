# Generated by Django 3.2 on 2021-05-24 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0006_subscriptions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Requests',
            new_name='Request',
        ),
        migrations.RenameModel(
            old_name='Subscriptions',
            new_name='Subscription',
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-13 02:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserMdel',
            new_name='UserModel',
        ),
    ]

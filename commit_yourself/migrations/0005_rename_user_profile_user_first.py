# Generated by Django 3.2.8 on 2021-11-24 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commit_yourself', '0004_rename_username_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='user_first',
        ),
    ]

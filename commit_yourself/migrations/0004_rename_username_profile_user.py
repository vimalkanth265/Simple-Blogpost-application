# Generated by Django 3.2.8 on 2021-11-24 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commit_yourself', '0003_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='user',
        ),
    ]

# Generated by Django 4.2 on 2023-04-17 17:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('User_website', '0003_alter_user_posts_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_Posts',
            new_name='User_Post',
        ),
    ]
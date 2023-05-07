# Generated by Django 4.2 on 2023-04-19 14:28

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User_website', '0005_user_post_slug_alter_user_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_post',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from=('title', 'user'), unique=True),
        ),
    ]
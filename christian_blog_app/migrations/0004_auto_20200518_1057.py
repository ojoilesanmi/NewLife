# Generated by Django 3.0.5 on 2020-05-18 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('christian_blog_app', '0003_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

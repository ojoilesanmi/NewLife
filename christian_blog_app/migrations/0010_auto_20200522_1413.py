# Generated by Django 3.0.5 on 2020-05-22 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('christian_blog_app', '0009_auto_20200521_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='prayer',
            name='username',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

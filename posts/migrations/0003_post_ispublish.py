# Generated by Django 4.1.7 on 2023-03-17 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_content_post_created_at_post_dislike_post_like_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='isPublish',
            field=models.BooleanField(default=False, verbose_name='Yayınla'),
        ),
    ]
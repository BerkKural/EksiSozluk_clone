# Generated by Django 4.1.7 on 2023-03-17 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_dislike_alter_post_like_alter_post_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=500, null=True, verbose_name='İçerik'),
        ),
    ]

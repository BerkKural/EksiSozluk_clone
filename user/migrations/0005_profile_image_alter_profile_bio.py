# Generated by Django 4.1.7 on 2023-03-17 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_profile_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.FileField(default='profiles/defaultpp.jpg', null=True, upload_to='profiles/', verbose_name='Porfil Resmi'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='Merhaba, ben bir blog yazarıyım', max_length=500, verbose_name='Hakkımda'),
        ),
    ]

# Generated by Django 5.0.3 on 2024-06-28 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidixerapp', '0015_alter_users_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(upload_to=''),
        ),
    ]

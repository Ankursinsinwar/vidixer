# Generated by Django 5.0.3 on 2024-06-22 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vidixerapp', '0008_rename_user_users_alter_proposal_service_provider_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
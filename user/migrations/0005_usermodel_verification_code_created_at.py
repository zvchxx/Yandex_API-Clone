# Generated by Django 5.1.4 on 2024-12-11 19:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_usermodel_phone_number_usermodel_full_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='verification_code_created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

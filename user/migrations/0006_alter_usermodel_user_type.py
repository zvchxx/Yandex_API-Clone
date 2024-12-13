# Generated by Django 5.1.4 on 2024-12-13 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_usermodel_verification_code_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='user_type',
            field=models.CharField(choices=[('customer', 'Customer'), ('restaurant', 'Restaurant'), ('admin', 'Admin'), ('courrier', 'courrier'), ('branch', 'Branch')], default='customer', max_length=10),
        ),
    ]
# Generated by Django 5.0.1 on 2024-01-15 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_account_date_joined_remove_account_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(db_column='password', max_length=1000),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(db_column='phone_number', max_length=20),
        ),
    ]

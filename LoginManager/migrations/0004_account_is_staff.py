# Generated by Django 4.0.6 on 2022-09-19 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginManager', '0003_remove_account_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]

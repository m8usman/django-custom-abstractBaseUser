# Generated by Django 4.0.3 on 2022-03-25 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_user_is_email_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
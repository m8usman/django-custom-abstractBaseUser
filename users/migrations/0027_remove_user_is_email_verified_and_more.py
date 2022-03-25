# Generated by Django 4.0.3 on 2022-03-25 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_user_is_email_verified_alter_user_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_email_verified',
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='images/profiles/user-default.png', null=True, upload_to='profiles/'),
        ),
    ]
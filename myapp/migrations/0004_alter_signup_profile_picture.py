# Generated by Django 4.2.5 on 2023-11-26 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_signup_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='Profile_Picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/profile_pic'),
        ),
    ]

# Generated by Django 3.2.9 on 2022-03-24 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fathers_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
# Generated by Django 3.2.9 on 2022-04-08 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_app', '0011_alter_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]

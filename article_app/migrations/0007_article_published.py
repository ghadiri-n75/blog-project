# Generated by Django 3.2.9 on 2022-03-24 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_app', '0006_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
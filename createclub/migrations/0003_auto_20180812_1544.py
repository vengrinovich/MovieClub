# Generated by Django 2.0 on 2018-08-12 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createclub', '0002_auto_20180812_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieclub',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-16 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='slug',
            field=models.SlugField(default='code', unique=True),
            preserve_default=False,
        ),
    ]

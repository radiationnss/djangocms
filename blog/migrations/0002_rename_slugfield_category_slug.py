# Generated by Django 4.0 on 2021-12-11 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='SlugField',
            new_name='slug',
        ),
    ]

# Generated by Django 4.0 on 2022-01-23 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pageName', models.CharField(max_length=100)),
                ('pageLink', models.CharField(max_length=100)),
            ],
        ),
    ]

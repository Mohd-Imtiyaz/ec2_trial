# Generated by Django 4.1.6 on 2023-02-10 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='company_users',
        ),
    ]

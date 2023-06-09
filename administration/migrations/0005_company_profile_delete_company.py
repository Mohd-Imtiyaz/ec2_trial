# Generated by Django 4.1.6 on 2023-04-13 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('administration', '0004_theme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200, null=True)),
                ('about_comapny', models.TextField(max_length=200, null=True)),
                ('company_location', models.TextField(max_length=500, null=True)),
                ('website_url', models.URLField(blank=True, max_length=300, null=True)),
                ('founded_on', models.DateField(null=True)),
                ('company_size', models.IntegerField(null=True)),
                ('specilities', models.CharField(max_length=500, null=True)),
                ('active', models.BooleanField(default=True)),
                ('group_name', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='auth.group')),
            ],
        ),
        migrations.DeleteModel(
            name='company',
        ),
    ]

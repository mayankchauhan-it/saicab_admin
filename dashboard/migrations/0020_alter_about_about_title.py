# Generated by Django 3.2.6 on 2023-08-01 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_alter_about_about_desc1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_title',
            field=models.JSONField(null=True),
        ),
    ]
# Generated by Django 3.2.13 on 2023-07-09 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20230707_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acadeurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]

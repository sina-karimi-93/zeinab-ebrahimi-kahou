# Generated by Django 3.1 on 2020-08-25 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20200823_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Phone Number (optional)'),
        ),
    ]

# Generated by Django 3.1 on 2020-08-18 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_myexperience_desc_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='myeducation',
            name='desc_2',
            field=models.TextField(blank=True, null=True, verbose_name='Description (optional)'),
        ),
    ]

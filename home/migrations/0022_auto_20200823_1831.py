# Generated by Django 3.1 on 2020-08-23 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20200823_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='myeducation',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Education', verbose_name='Photo'),
        ),
        migrations.AddField(
            model_name='myexperience',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Experience', verbose_name='Photo'),
        ),
    ]

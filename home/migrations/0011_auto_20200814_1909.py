# Generated by Django 3.1 on 2020-08-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_contactme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactme',
            name='email',
            field=models.EmailField(max_length=25, verbose_name='Email'),
        ),
    ]

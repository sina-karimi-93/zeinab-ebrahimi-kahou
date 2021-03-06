# Generated by Django 3.1 on 2020-08-23 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20200823_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='research',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Researches', verbose_name='Photo (optional)'),
        ),
        migrations.AlterField(
            model_name='research',
            name='description',
            field=models.TextField(default='Description'),
        ),
        migrations.AlterField(
            model_name='research',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='Researches', verbose_name='Article (PDF or Word file)(optional)'),
        ),
        migrations.AlterField(
            model_name='research',
            name='link',
            field=models.CharField(blank=True, default='https://', max_length=50, null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='research',
            name='references',
            field=models.FileField(blank=True, null=True, upload_to='Researches', verbose_name='References (.txt file)(optional)'),
        ),
    ]

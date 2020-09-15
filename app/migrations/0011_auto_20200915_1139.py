# Generated by Django 3.1 on 2020-09-15 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200910_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='image',
            field=models.ImageField(blank=True, help_text='Cover image of this challenge.', upload_to='challenges/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, help_text='Cover image of this project.', upload_to='challenges/', verbose_name='Image'),
        ),
    ]

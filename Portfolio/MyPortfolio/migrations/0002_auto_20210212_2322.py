# Generated by Django 3.1.6 on 2021-02-12 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyPortfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]

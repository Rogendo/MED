# Generated by Django 2.1.7 on 2019-03-26 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medexpert', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='updates',
            name='image',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='updates',
            name='video',
            field=models.FileField(blank=True, upload_to='media'),
        ),
    ]
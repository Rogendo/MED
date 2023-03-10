# Generated by Django 2.2.1 on 2019-05-22 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medexpert', '0014_auto_20190520_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='msgs',
            name='Email',
            field=models.EmailField(default=0, max_length=40),
        ),
        migrations.AddField(
            model_name='msgs',
            name='Subject',
            field=models.TextField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='msgs',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='msgs',
            name='message',
            field=models.TextField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='msgs',
            name='name',
            field=models.CharField(default=0, max_length=25),
        ),
        migrations.AlterField(
            model_name='msgs',
            name='time_sent',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

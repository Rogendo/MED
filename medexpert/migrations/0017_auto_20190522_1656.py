# Generated by Django 2.2.1 on 2019-05-22 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medexpert', '0016_auto_20190522_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.IntegerField()),
                ('dateofbirth', models.DateField(max_length=30)),
                ('gender', models.CharField(max_length=7)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='data',
        ),
        migrations.AlterField(
            model_name='msgs',
            name='phone',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 3.0.6 on 2020-06-29 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dummy',
            name='roll',
            field=models.CharField(max_length=20, verbose_name='roll'),
        ),
    ]
# Generated by Django 2.2.7 on 2019-11-18 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appizza', '0003_auto_20191118_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='Tamano',
            field=models.ManyToManyField(to='appizza.Tamano'),
        ),
    ]
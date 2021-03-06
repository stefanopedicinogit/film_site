# Generated by Django 4.0.2 on 2022-02-25 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='film_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='seen',
            name='value',
            field=models.BooleanField(default=True),
        ),
    ]

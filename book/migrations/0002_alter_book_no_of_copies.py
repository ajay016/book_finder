# Generated by Django 4.2.1 on 2023-05-21 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='no_of_copies',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]

# Generated by Django 4.1 on 2022-09-18 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_profile_dataset_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='number_of_images',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-25 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ThesisApp', '0011_rename_image_person_parent_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='time',
            field=models.DurationField(default='00:00:00'),
        ),
    ]

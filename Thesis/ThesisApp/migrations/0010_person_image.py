# Generated by Django 4.2.2 on 2023-07-25 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ThesisApp', '0009_remove_person_date_person_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, upload_to='Images'),
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-25 15:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ThesisApp', '0006_alter_person_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='date',
        ),
        migrations.AddField(
            model_name='person',
            name='time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

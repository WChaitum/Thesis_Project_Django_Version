# Generated by Django 4.2.2 on 2023-07-05 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ThesisApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='children_key',
        ),
    ]

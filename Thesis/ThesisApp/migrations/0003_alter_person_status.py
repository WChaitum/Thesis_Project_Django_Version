# Generated by Django 4.2.2 on 2023-07-15 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ThesisApp', '0002_remove_person_children_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='status',
            field=models.CharField(max_length=100),
        ),
    ]
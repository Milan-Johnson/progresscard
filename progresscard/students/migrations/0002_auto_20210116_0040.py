# Generated by Django 3.1.4 on 2021-01-15 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marks',
            old_name='englih',
            new_name='english',
        ),
    ]
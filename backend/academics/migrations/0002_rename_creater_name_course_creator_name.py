# Generated by Django 4.1.2 on 2022-10-28 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='creater_name',
            new_name='creator_name',
        ),
    ]

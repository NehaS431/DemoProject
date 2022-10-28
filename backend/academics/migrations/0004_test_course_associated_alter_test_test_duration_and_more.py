# Generated by Django 4.1.2 on 2022-10-28 07:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0003_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='course_associated',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='academics.course'),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_duration',
            field=models.DurationField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_name',
            field=models.CharField(default='', max_length=256),
        ),
    ]

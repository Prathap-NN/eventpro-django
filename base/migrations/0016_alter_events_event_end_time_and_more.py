# Generated by Django 4.1 on 2022-08-23 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_events_event_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='event_end_time',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_start_time',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

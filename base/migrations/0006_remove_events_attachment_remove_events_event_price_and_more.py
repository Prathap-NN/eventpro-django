# Generated by Django 4.1 on 2022-08-20 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_events_created_at_alter_events_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='attachment',
        ),
        migrations.RemoveField(
            model_name='events',
            name='event_price',
        ),
        migrations.RemoveField(
            model_name='events',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='events',
            name='view_count',
        ),
    ]

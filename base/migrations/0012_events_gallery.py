# Generated by Django 4.1 on 2022-08-22 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_rename_gallery_events_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='gallery',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
    ]

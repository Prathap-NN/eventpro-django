# Generated by Django 4.1 on 2022-08-20 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_events_featured_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='featured_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

# Generated by Django 5.1 on 2024-08-12 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cis376', '0007_remove_postbox_header_remove_profile_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(default=''),
        ),
    ]

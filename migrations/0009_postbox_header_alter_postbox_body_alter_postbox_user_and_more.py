# Generated by Django 5.1 on 2024-08-12 11:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cis376', '0008_alter_post_body'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='postbox',
            name='header',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='postbox',
            name='body',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='postbox',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]

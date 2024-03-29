# Generated by Django 5.0.3 on 2024-03-26 16:14

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0002_streamplatform'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='platForm',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='watchlist_app.streamplatform'),
            preserve_default=False,
        ),
    ]

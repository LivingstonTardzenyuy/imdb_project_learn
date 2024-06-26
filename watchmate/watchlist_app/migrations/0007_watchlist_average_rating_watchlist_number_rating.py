# Generated by Django 5.0.3 on 2024-04-13 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0006_reviews_review_user_alter_reviews_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='average_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='number_rating',
            field=models.IntegerField(default=0),
        ),
    ]

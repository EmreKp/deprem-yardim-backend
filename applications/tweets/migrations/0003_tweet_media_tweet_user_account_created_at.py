# Generated by Django 4.1.6 on 2023-02-06 18:12

# Django Stuff
from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tweets", "0002_alter_tweet_hashtags"),
    ]

    operations = [
        migrations.AddField(
            model_name="tweet",
            name="media",
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name="tweet",
            name="user_account_created_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2 on 2023-05-29 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0007_remove_news_time_alter_news_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="time",
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]

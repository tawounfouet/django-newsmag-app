# Generated by Django 4.2 on 2023-05-29 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0006_news_time_alter_news_date_alter_news_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="news",
            name="time",
        ),
        migrations.AlterField(
            model_name="news",
            name="date",
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]

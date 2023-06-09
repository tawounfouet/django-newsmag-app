# Generated by Django 4.2 on 2023-05-29 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0005_alter_news_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="time",
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="news",
            name="date",
            field=models.DateTimeField(default="0000-00-00"),
        ),
        migrations.AlterField(
            model_name="news",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="./"),
        ),
    ]

# Generated by Django 4.2 on 2023-05-30 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0009_news_o_category_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="news",
            old_name="o_category_id",
            new_name="ocategory_id",
        ),
    ]

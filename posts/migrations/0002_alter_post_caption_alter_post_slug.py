# Generated by Django 5.0.3 on 2024-04-18 11:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="caption",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]

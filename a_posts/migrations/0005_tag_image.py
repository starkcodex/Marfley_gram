# Generated by Django 5.0.1 on 2024-01-25 08:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("a_posts", "0004_alter_tag_options_tag_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="image",
            field=models.FileField(blank=True, null=True, upload_to="icons/"),
        ),
    ]
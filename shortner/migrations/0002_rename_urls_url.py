# Generated by Django 4.1.4 on 2023-02-27 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shortner", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="Urls", new_name="Url",),
    ]

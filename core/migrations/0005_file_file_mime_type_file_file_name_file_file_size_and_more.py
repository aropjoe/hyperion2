# Generated by Django 4.1.7 on 2023-05-16 15:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_file_remove_data_file_data_files"),
    ]

    operations = [
        migrations.AddField(
            model_name="file",
            name="file_mime_type",
            field=models.CharField(default="Unknown", max_length=100),
        ),
        migrations.AddField(
            model_name="file",
            name="file_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="file",
            name="file_size",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="file",
            name="file",
            field=models.FileField(upload_to="files/"),
        ),
    ]
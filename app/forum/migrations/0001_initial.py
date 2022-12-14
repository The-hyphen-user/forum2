# Generated by Django 4.1.1 on 2022-09-16 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("date_posted", models.DateTimeField(auto_now_add=True)),
                ("author", models.CharField(max_length=100)),
            ],
        ),
    ]

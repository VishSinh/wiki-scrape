# Generated by Django 4.2.2 on 2023-06-29 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebScrape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=300)),
                ('title', models.CharField(max_length=250)),
                ('info', models.JSONField(null=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

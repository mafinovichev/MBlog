# Generated by Django 4.1.3 on 2023-03-06 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogservice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('postid', models.IntegerField()),
            ],
        ),
    ]

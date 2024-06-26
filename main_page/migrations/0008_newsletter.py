# Generated by Django 4.2.13 on 2024-06-19 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0007_post_featured_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=256, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['email'],
            },
        ),
    ]

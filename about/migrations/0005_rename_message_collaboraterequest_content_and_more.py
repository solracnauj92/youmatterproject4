# Generated by Django 5.0.6 on 2024-06-26 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_delete_newslettersignup_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collaboraterequest',
            old_name='message',
            new_name='content',
        ),
        migrations.AddField(
            model_name='collaboraterequest',
            name='title',
            field=models.CharField(default='New Request', max_length=200),
        ),
    ]

# Generated by Django 2.2 on 2019-05-01 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='page',
            new_name='content',
        ),
    ]
# Generated by Django 4.1.4 on 2022-12-22 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_title_thread_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='name',
            new_name='title',
        ),
    ]

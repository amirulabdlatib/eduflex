# Generated by Django 4.1.7 on 2023-06-28 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eduflexApp', '0002_alter_notes_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='updated_at',
        ),
    ]
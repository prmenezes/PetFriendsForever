# Generated by Django 5.2 on 2025-04-16 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='petfee',
            old_name='age_category',
            new_name='category',
        ),
    ]

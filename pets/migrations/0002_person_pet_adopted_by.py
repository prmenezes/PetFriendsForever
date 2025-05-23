# Generated by Django 5.2 on 2025-04-06 19:46

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.IntegerField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('interested_species', models.CharField(choices=[('DOG', 'dog'), ('CAT', 'cat'), ('BIRD', 'bird')])),
                ('first_time_owner', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='adopted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pets', to='pets.person'),
        ),
    ]

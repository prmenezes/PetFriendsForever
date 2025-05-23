# Generated by Django 5.2 on 2025-04-12 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0011_alter_pet_display_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petphotos',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='petphotos',
            name='image_width',
        ),
        migrations.AlterField(
            model_name='pet',
            name='display_pic',
            field=models.ImageField(default='pet_pics_upload/photo_coming_soon.png', max_length=200, upload_to='pet_display_pics_upload'),
        ),
        migrations.AlterField(
            model_name='petphotos',
            name='image',
            field=models.ImageField(default='pet_pics_upload/photo_coming_soon.png', upload_to='pet_pics_upload'),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-05 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rike_menu', '0002_dish_content_en_dish_content_ka_dish_title_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dishcategory',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='drinkcategory',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%y/%m/%d/'),
        ),
    ]

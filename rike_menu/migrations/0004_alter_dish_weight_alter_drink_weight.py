# Generated by Django 4.2.7 on 2023-11-20 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rike_menu', '0003_dishcategory_photo_drinkcategory_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='weight',
            field=models.IntegerField(blank=True, null=True, verbose_name='გრამირება'),
        ),
        migrations.AlterField(
            model_name='drink',
            name='weight',
            field=models.IntegerField(blank=True, null=True, verbose_name='გრამირება'),
        ),
    ]

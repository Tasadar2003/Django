# Generated by Django 4.2.7 on 2023-11-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_tags_goods_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='image',
            field=models.ImageField(blank=True, upload_to='image', verbose_name='Image'),
        ),
    ]

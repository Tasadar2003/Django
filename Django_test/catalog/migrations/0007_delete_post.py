# Generated by Django 4.2.7 on 2023-11-19 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_goods_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-14 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketapp', '0002_alter_categories_options_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]

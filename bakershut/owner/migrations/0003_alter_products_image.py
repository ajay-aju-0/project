# Generated by Django 3.2.4 on 2021-07-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0002_products_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.FileField(max_length=300, upload_to='images'),
        ),
    ]

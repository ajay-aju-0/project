# Generated by Django 3.2.4 on 2021-07-24 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0003_alter_products_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0004_orderitems_is_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.products')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
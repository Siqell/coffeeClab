# Generated by Django 4.0.3 on 2023-08-08 07:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_order_date_alter_product_price_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='order',
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 8, 7, 29, 37, 989764, tzinfo=utc)),
        ),
    ]
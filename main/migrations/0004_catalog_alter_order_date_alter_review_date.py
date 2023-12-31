# Generated by Django 4.0.3 on 2023-08-03 11:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_order_alter_review_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 3, 11, 4, 30, 529274, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 3, 11, 4, 30, 446288, tzinfo=utc)),
        ),
    ]

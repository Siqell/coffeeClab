# Generated by Django 4.0.3 on 2023-08-03 10:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_review_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username_client', models.CharField(max_length=100)),
                ('list_product', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 8, 3, 10, 35, 32, 956505, tzinfo=utc))),
            ],
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 3, 10, 35, 32, 870992, tzinfo=utc)),
        ),
    ]

# Generated by Django 4.2.4 on 2024-05-13 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lstm_prediction', '0002_remove_lstmprediction_stock_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lstmprediction',
            name='window_size',
        ),
    ]

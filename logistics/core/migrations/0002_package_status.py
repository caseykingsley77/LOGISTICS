# Generated by Django 5.0 on 2023-12-19 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='status',
            field=models.CharField(choices=[('Out on Delivery', 'Out on Delivery'), ('Cancelled Delivery', 'Cancelled Cancelled'), ('Arrived for Pickup', 'Arrived for Pickup'), ('Successfully Delivered', 'Successfully Delivered')], max_length=200, null=True),
        ),
    ]

# Generated by Django 5.1.6 on 2025-03-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='address2',
            field=models.CharField(default='new', max_length=200),
            preserve_default=False,
        ),
    ]

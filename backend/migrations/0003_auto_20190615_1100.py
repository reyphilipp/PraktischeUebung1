# Generated by Django 2.2.2 on 2019-06-15 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20190615_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='addresses', to='backend.Address'),
        ),
        migrations.AlterField(
            model_name='invoiceposition',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoicePositions', to='backend.Invoice'),
        ),
    ]

# Generated by Django 2.2.2 on 2019-06-15 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoice', to='backend.Address'),
        ),
        migrations.AlterField(
            model_name='invoiceposition',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoicePosition', to='backend.Invoice'),
        ),
    ]

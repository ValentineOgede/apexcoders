# Generated by Django 4.2.3 on 2023-07-26 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='purchase_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]

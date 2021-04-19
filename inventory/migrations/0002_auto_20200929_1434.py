# Generated by Django 3.0.5 on 2020-09-29 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='jarti',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
    ]

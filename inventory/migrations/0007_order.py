# Generated by Django 3.0.5 on 2020-10-04 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20201001_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('order_status', models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('canceled', 'Cancelled'), ('completed', 'Completed'), ('onhold', 'OnHold')], max_length=30)),
                ('notes', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.Customer')),
                ('product', models.ManyToManyField(to='inventory.Product')),
            ],
        ),
    ]
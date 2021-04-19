# Generated by Django 3.0.5 on 2020-09-30 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20200929_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('registered_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
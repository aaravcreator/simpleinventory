# Generated by Django 3.0.5 on 2020-10-10 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productcategory',
            old_name='catgory_name',
            new_name='category_name',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('canceled', 'Cancelled'), ('completed', 'Completed'), ('onhold', 'OnHold')], default='pending', max_length=30),
        ),
    ]

# Generated by Django 4.0.2 on 2022-05-06 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='photos/default.jpg', upload_to='photos/%Y/%m/%d/'),
        ),
    ]

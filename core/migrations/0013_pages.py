# Generated by Django 4.0.2 on 2022-08-08 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_order_product_order_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us', models.TextField()),
                ('shipping', models.TextField()),
                ('privacyPolicy', models.TextField()),
            ],
        ),
    ]

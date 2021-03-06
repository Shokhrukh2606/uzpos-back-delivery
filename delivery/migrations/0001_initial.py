# Generated by Django 3.2.7 on 2021-09-11 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=512, verbose_name='Client name')),
                ('phone', models.CharField(max_length=9, verbose_name='Client phone number')),
                ('from_address', models.CharField(max_length=512, verbose_name='From address')),
                ('to_address', models.CharField(max_length=512, verbose_name='To address')),
                ('landmark', models.CharField(max_length=512, verbose_name='Orientir')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Order created')),
                ('deliver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Orders',
                'db_table': 'order',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(verbose_name='Product id')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('order_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='delivery.order')),
            ],
            options={
                'verbose_name_plural': 'OrderItems',
                'db_table': 'order_items',
                'ordering': ['-pk'],
            },
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-19 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Product quantity'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-03 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.food4fuel.com/wp-content/uploads/woocommerce-placeholder-600x600.png', max_length=500),
        ),
    ]
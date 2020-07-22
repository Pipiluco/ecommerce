# Generated by Django 2.2.13 on 2020-07-22 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CarItem',
            new_name='CartItem',
        ),
        migrations.RenameField(
            model_name='cartitem',
            old_name='car_key',
            new_name='cart_key',
        ),
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart_key', 'product')},
        ),
    ]

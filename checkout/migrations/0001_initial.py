# Generated by Django 2.2.13 on 2020-07-22 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_key', models.CharField(db_index=True, max_length=40, verbose_name='Chave do carrinho')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantidade')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product', verbose_name='Produto')),
            ],
            options={
                'verbose_name_plural': 'Itens dos carrinhos',
                'verbose_name': 'Item do carrinho',
            },
        ),
    ]

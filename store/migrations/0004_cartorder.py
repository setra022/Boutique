# Generated by Django 4.2.3 on 2023-07-31 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
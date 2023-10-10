# Generated by Django 4.2.3 on 2023-10-10 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_cartorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6, null=True),
        ),
    ]
# Generated by Django 4.2.11 on 2024-05-23 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='card_id',
            new_name='cart_id',
        ),
    ]

# Generated by Django 3.2.5 on 2021-11-07 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_order_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='user_id',
        ),
    ]

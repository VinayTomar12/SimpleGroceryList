# Generated by Django 3.2.5 on 2021-07-24 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GroceryList', '0002_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyinglistitem',
            name='item_category',
        ),
        migrations.RemoveField(
            model_name='buyinglistitem',
            name='item_name',
        ),
        migrations.AddField(
            model_name='buyinglistitem',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='GroceryList.item'),
            preserve_default=False,
        ),
    ]

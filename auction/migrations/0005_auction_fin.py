# Generated by Django 4.1.1 on 2022-10-19 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auction", "0004_rename_min_amount_auction_min_bid"),
    ]

    operations = [
        migrations.AddField(
            model_name="auction",
            name="fin",
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
# Generated by Django 2.1.8 on 2019-07-16 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_market_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='summary',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
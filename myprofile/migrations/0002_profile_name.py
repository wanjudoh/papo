# Generated by Django 2.1.8 on 2019-07-21 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

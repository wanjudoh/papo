# Generated by Django 2.1.8 on 2019-08-10 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField(default='')),
                ('link', models.CharField(max_length=500)),
                ('image', models.ImageField(null=True, upload_to='msg/')),
            ],
        ),
    ]

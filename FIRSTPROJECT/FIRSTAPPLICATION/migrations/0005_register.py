# Generated by Django 2.2 on 2021-04-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FIRSTAPPLICATION', '0004_auto_20210331_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=30)),
                ('Last_name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=40)),
                ('vemail', models.EmailField(max_length=40)),
            ],
        ),
    ]

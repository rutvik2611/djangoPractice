# Generated by Django 2.2 on 2021-03-31 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FIRSTAPPLICATION', '0002_students_training'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('phone', models.IntegerField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
# Generated by Django 3.1.5 on 2021-02-06 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receivers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('targets', models.JSONField()),
                ('receiveFrequency', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'receivers',
            },
        ),
    ]

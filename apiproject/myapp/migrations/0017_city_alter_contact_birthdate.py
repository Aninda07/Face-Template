# Generated by Django 4.0.6 on 2022-07-26 09:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_alter_contact_birthdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='Birthdate',
            field=models.DateField(default=datetime.datetime(2022, 7, 26, 9, 18, 49, 622990)),
        ),
    ]

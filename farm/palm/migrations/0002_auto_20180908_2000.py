# Generated by Django 2.0.7 on 2018-09-08 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gcg',
            name='comm_error_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='gcg',
            name='node_group',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='gcg',
            name='node_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='gcg',
            name='serial_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='gcg',
            name='service_error_num',
            field=models.IntegerField(default=0),
        ),
    ]

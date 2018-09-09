# Generated by Django 2.0.7 on 2018-09-09 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palm', '0002_auto_20180908_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='anode',
            name='anode_type',
            field=models.CharField(choices=[('oc', 'Open_Close_Motor'), ('ef', 'Extractor_Fan'), ('wm', 'Watering_Motor'), ('ns', 'Nutrient_Supply'), ('lc', 'Light_Control'), ('cc', 'Co2_Control'), ('dh', 'Dehumidifier'), ('hf', 'Humidifier'), ('ve', 'Valve_Equipment')], default='oc', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='snode',
            name='snode_type',
            field=models.CharField(choices=[('t', 'Temperature'), ('h', 'Humidity'), ('th', 'Temperature_Humidity'), ('l', 'Light'), ('ws', 'Wind_Speed'), ('wd', 'Wind_Direction'), ('rf', 'Rain_Fall'), ('st', 'Soil_Temperature'), ('sh', 'Soil_Humidity'), ('ph', 'pH'), ('ec', 'EC')], default='t', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='anode',
            name='comm_error_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='anode',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='anode',
            name='register_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='anode',
            name='serial_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='anode',
            name='service_error_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='anode',
            name='sw_ver',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='gcg',
            name='sensing_periode',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='snode',
            name='comm_error_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='snode',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='snode',
            name='register_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='snode',
            name='serial_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='snode',
            name='service_error_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='snode',
            name='sw_ver',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 2.0.7 on 2018-09-09 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('palm', '0003_auto_20180909_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='anodelog',
            name='anode',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='palm.Anode'),
            preserve_default=False,
        ),
    ]

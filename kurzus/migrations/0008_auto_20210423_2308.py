# Generated by Django 2.2.19 on 2021-04-23 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kurzus', '0007_auto_20210423_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurzus',
            name='teremCim',
            field=models.ForeignKey(blank=True, db_column='teremCim', null=True, on_delete=django.db.models.deletion.CASCADE, to='terem.Terem'),
        ),
    ]

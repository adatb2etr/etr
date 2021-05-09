# Generated by Django 2.2.19 on 2021-04-29 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kurzus', '0008_auto_20210423_2308'),
        ('kepzes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teljesitesfeltetel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kepzesId', models.OneToOneField(db_column='kepzesId', on_delete=django.db.models.deletion.CASCADE, to='kepzes.Kepzes')),
                ('kurzusKod', models.OneToOneField(db_column='kurzusKod', on_delete=django.db.models.deletion.CASCADE, to='kurzus.Kurzus')),
            ],
            options={
                'db_table': 'teljesitesfeltetel',
            },
        ),
    ]
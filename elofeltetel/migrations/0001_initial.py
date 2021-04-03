# Generated by Django 2.2.19 on 2021-03-22 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kurzus', '0002_auto_20210312_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elofeltetel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teljesitette', models.IntegerField(default=0)),
                ('elofeltetelKod', models.ForeignKey(db_column='elofeltetelKod', on_delete=django.db.models.deletion.CASCADE, related_name='elofeltetelKod', to='kurzus.Kurzus')),
                ('kurzusKod', models.ForeignKey(db_column='kurzusKod', on_delete=django.db.models.deletion.CASCADE, related_name='kurzusKod', to='kurzus.Kurzus')),
            ],
            options={
                'db_table': 'elofeltetel',
                'unique_together': {('kurzusKod', 'elofeltetelKod')},
            },
        ),
    ]
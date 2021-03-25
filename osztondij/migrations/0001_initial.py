# Generated by Django 2.2.19 on 2021-03-24 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_etradmin_hallgato_oktato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Osztondij',
            fields=[
                ('osztondijosszeg', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('hallgatoAzonosito', models.OneToOneField(db_column='hallgatoAzonosito', on_delete=django.db.models.deletion.CASCADE, to='user.Hallgato')),
            ],
            options={
                'db_table': 'osztondij',
            },
        ),
    ]

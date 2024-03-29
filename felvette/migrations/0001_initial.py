# Generated by Django 2.2.19 on 2021-04-29 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kepzes', '0001_initial'),
        ('user', '0003_remove_hallgato_kepzes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Felvette',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hallgatoAzonosito', models.OneToOneField(db_column='hallgatoAzonosito', on_delete=django.db.models.deletion.CASCADE, to='user.Hallgato')),
                ('kepzesId', models.OneToOneField(db_column='kepzesId', on_delete=django.db.models.deletion.CASCADE, to='kepzes.Kepzes')),
            ],
            options={
                'db_table': 'felvette',
            },
        ),
    ]

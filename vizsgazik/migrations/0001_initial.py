# Generated by Django 2.2.19 on 2021-03-25 16:02

from django.db import migrations, models
import django.db.models.deletion
import vizsgazik.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vizsga', '0002_auto_20210325_1652'),
        ('user', '0002_etradmin_hallgato_oktato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vizsgazik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kapottjegy', models.IntegerField(validators=[vizsgazik.models.validate_jegy])),
                ('vizsgaalkalom', models.IntegerField(validators=[vizsgazik.models.validate_alkalom])),
                ('hallgatoAzonosito', models.ForeignKey(db_column='hallgatoAzonosito', on_delete=django.db.models.deletion.CASCADE, to='user.Hallgato')),
                ('vizsgaID', models.ForeignKey(db_column='vizsgaID', on_delete=django.db.models.deletion.CASCADE, to='vizsga.Vizsga')),
            ],
            options={
                'db_table': 'vizsgazik',
                'unique_together': {('vizsgaID', 'hallgatoAzonosito')},
            },
        ),
    ]
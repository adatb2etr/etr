# Generated by Django 2.2.19 on 2021-03-25 15:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vizsga', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vizsga',
            name='vizsgaID',
            field=models.AutoField(db_column='vizsgaID', default=django.utils.timezone.now, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='vizsga',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='vizsga',
            name='id',
        ),
    ]

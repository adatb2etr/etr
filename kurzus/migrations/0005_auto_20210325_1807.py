# Generated by Django 2.2.19 on 2021-03-25 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kurzus', '0004_auto_20210325_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurzus',
            name='oktatoAzonosito',
            field=models.ForeignKey(blank=True, db_column='oktatoAzonosito', max_length=6, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Oktato'),
        ),
    ]

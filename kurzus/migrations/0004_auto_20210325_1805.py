# Generated by Django 2.2.19 on 2021-03-25 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kurzus', '0003_auto_20210322_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurzus',
            name='oktatoAzonosito',
            field=models.ForeignKey(db_column='oktatoAzonosito', max_length=6, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Oktato'),
        ),
    ]
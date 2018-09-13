# Generated by Django 2.1 on 2018-09-10 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20180910_1257'),
        ('register_contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registercontact',
            name='address_id',
        ),
        migrations.AddField(
            model_name='registercontact',
            name='address',
            field=models.ForeignKey(db_column='id_address', db_index=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='id_address', to='address.Address'),
        ),
        migrations.AlterField(
            model_name='registercontact',
            name='email',
            field=models.CharField(blank=True, db_column='email', max_length=500),
        ),
        migrations.AlterModelTable(
            name='registercontact',
            table='register_contact',
        ),
    ]